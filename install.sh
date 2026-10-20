#!/usr/bin/env bash
# Install the Brasileirão theme pack into Omarchy.
#
#   ./install.sh          symlink themes (regenerating the build updates them)
#   ./install.sh --copy   copy themes instead (portable, self-contained)
#   ./install.sh --menu   also add a "Brasileirão 2026" section to the Omarchy menu
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$HOME/.config/omarchy/themes"
MENU="$HOME/.config/omarchy/extensions/omarchy-menu.jsonc"
MODE="link"
ADD_MENU=0

for arg in "$@"; do
  case "$arg" in
    --copy) MODE="copy" ;;
    --link) MODE="link" ;;
    --menu) ADD_MENU=1 ;;
    *) echo "unknown option: $arg" >&2; exit 1 ;;
  esac
done

mkdir -p "$DEST"
count=0
for dir in "$ROOT"/themes/*/; do
  [ -d "$dir" ] || continue
  slug="$(basename "$dir")"
  if [ -e "$DEST/$slug" ] && [ ! -L "$DEST/$slug" ]; then
    echo "skip $slug (a non-symlink theme with that name already exists)"
    continue
  fi
  if [ "$MODE" = "link" ] && [ -L "$DEST/$slug" ] && [ "$(readlink -f "$DEST/$slug")" = "$(realpath "$dir")" ]; then
    count=$((count + 1))
    continue
  fi
  rm -rf "$DEST/$slug"
  if [ "$MODE" = "copy" ]; then
    cp -r "$dir" "$DEST/$slug"
  else
    ln -s "${dir%/}" "$DEST/$slug"
  fi
  count=$((count + 1))
done

rm -rf "${XDG_CACHE_HOME:-$HOME/.cache}/omarchy/theme-selector"
echo "Installed $count themes into $DEST ($MODE)."

if [ "$ADD_MENU" = "1" ]; then
  python3 - "$MENU" "$ROOT" <<'PY'
import json, os, re, shutil, sys, time

menu, root = sys.argv[1], sys.argv[2]
text = open(menu, encoding="utf-8").read() if os.path.exists(menu) else "{\n}\n"

themes_dir = os.path.join(root, "themes")
slugs = sorted(d for d in os.listdir(themes_dir) if os.path.isdir(os.path.join(themes_dir, d)))

rows = []
if '"clubes"' not in text:
    rows.append('"clubes": ' + json.dumps(
        {"icon": "\uf1e3", "label": "Clubes"}, ensure_ascii=True))
sys.path.insert(0, os.path.join(root, 'src'))
from teams import team
for slug in slugs:
    if json.dumps(f"clubes.{slug}") in text:
        continue
    label = team(slug)['display'].title()
    rows.append(json.dumps(f"clubes.{slug}") + ": " + json.dumps(
        {"icon": "\uf111", "label": label, "action": f"omarchy theme set {slug}"},
        ensure_ascii=True))
if not rows:
    print("Menu already contains every club theme")
    raise SystemExit(0)
block = ",\n  ".join(rows)

idx = text.rstrip().rfind("}")
if idx == -1:
    raise SystemExit("menu file has no closing brace; not touching it")

inner_raw = text[:idx].split("{", 1)[1] if "{" in text[:idx] else ""
inner = re.sub(r"//[^\n]*", "", inner_raw).strip()
lead = ",\n  " if inner else "\n  "
new = text[:idx].rstrip() + lead + block + "\n" + text[idx:]

try:
    json.loads(re.sub(r"//[^\n]*", "", new))
except json.JSONDecodeError as exc:
    raise SystemExit(f"refusing to write menu: JSONC would be invalid ({exc})")

if os.path.exists(menu):
    shutil.copy2(menu, f"{menu}.bak.{int(time.time())}")
with open(menu, "w", encoding="utf-8") as f:
    f.write(new)
print(f"Added/updated {len(rows)} menu entries to {menu}")
PY
fi

echo "Try: omarchy theme set santos"
