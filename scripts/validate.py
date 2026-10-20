#!/usr/bin/env python3
"""Validate Arquibancada's native root theme and all 20 club packages offline."""
import json
import hashlib
import re
import struct
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from badge_surface import validate_surface
REQUIRED = {'accent', 'background', 'foreground', 'red', 'yellow', 'green', 'cyan', 'blue', 'magenta'}
WALLPAPERS = ('1-arte.jpg', '2-escudo.jpg', '3-mascote.jpg')


def dimensions(path):
    with path.open('rb') as f:
        header = f.read(24)
        if header[:8] == b'\x89PNG\r\n\x1a\n':
            return struct.unpack('>II', header[16:24])
        f.seek(0)
        if f.read(2) != b'\xff\xd8':
            raise ValueError(f'Unsupported image: {path}')
        while True:
            if f.read(1) != b'\xff':
                raise ValueError(f'Invalid JPEG marker: {path}')
            marker = f.read(1)
            while marker == b'\xff':
                marker = f.read(1)
            if marker in (b'\xd8', b'\xd9', b'\x01'):
                continue
            length = struct.unpack('>H', f.read(2))[0]
            if marker[0] in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                _, height, width = struct.unpack('>BHH', f.read(5))
                return width, height
            f.seek(length - 2, 1)


def validate_theme(directory, native=False):
    assert {p.name for p in (directory / 'backgrounds').iterdir()} == set(WALLPAPERS), f'Expected exactly three wallpapers: {directory}'
    colors = tomllib.loads((directory / 'colors.toml').read_text())
    assert REQUIRED <= colors.keys(), f'Missing palette keys: {directory}'
    assert colors.get('mode') in ('dark', 'light'), f'Missing/invalid mode: {directory}'
    assert all(re.fullmatch(r'#[0-9a-fA-F]{6}', value) for key, value in colors.items() if key != 'mode'), directory
    width, height = dimensions(directory / 'preview.png')
    assert width >= 1000 and abs(width / height - 16 / 9) < 0.005, directory
    if native:
        assert width * 9 == height * 16, 'Root preview must be exactly 16:9'
    for name in WALLPAPERS:
        path = directory / 'backgrounds' / name
        assert path.is_file() and not path.is_symlink(), path
        assert dimensions(path) == (3840, 2160), path
        assert path.stat().st_size <= 50 * 1024 * 1024, path
    for name in ('icons.theme', 'keyboard.rgb', 'shell.lock.toml'):
        assert (directory / name).is_file(), directory / name


def main():
    validate_theme(ROOT, native=True)
    additions = json.loads((ROOT / 'src/serie_a_2026.json').read_text())
    expected = {'santos', 'corinthians', 'palmeiras', 'sao-paulo'} | {row['slug'] for row in additions}
    actual = {path.name for path in (ROOT / 'themes').iterdir() if path.is_dir()}
    assert len(expected) == 20 and actual == expected, 'Club roster mismatch'
    layouts = json.loads((ROOT / 'src/mascotes-layout.json').read_text())
    stadiums = json.loads((ROOT / 'src/estadios.json').read_text())
    assert set(layouts) == set(stadiums) == expected, 'Every club needs an explicit badge placement and stadium source'
    for slug in sorted(expected):
        validate_theme(ROOT / 'themes' / slug)
        source = ROOT / 'assets/mascotes-generated' / f'{slug}.png'
        assert source.is_file(), slug
        assert dimensions(source) == (1672, 941), f'Badge coordinates require the reviewed source frame: {slug}'
        assert (ROOT / 'assets' / layouts[slug]['badge']).is_file(), slug
        kit = layouts[slug]
        assert kit['application'] == 'native-shirt-surface', f'Unreviewed shirt pipeline: {slug}'
        assert kit['placement'] == ('central' if slug in ('sao-paulo', 'coritiba') else 'wearer-left'), slug
        assert kit['reference'].startswith('https://') and kit['reference_image'].startswith('https://'), slug
        assert kit['verified'] == '2026-10-20' and kit['visual_review'] is True, slug
        assert hashlib.sha256(source.read_bytes()).hexdigest() == kit['source_sha256'], f'Shirt art changed since visual review: {slug}'
        badge = ROOT / 'assets' / kit['badge']
        assert hashlib.sha256(badge.read_bytes()).hexdigest() == kit['badge_sha256'], f'Badge artwork changed since review: {slug}'
        surface = kit['shirt_surface']
        assert set(surface) == {'corners', 'curve'}, f'Explicit shirt surface required: {slug}'
        validate_surface(surface)
        assert 'badge_frame' not in kit, f'Flat sticker placement is obsolete: {slug}'
        assert not {'box', 'surface', 'cloth_shading'} & kit.keys(), f'Obsolete badge overlay: {slug}'
        assert stadiums[slug]['sources'] and stadiums[slug]['verified'] == '2026-10-19', slug
    for name in WALLPAPERS:
        assert (ROOT / 'backgrounds' / name).read_bytes() == (ROOT / 'themes/santos/backgrounds' / name).read_bytes(), 'Default mirror differs from Santos'
    assert (ROOT / 'colors.toml').read_bytes() == (ROOT / 'themes/santos/colors.toml').read_bytes()
    print('PASS: native root layout, exact 16:9 preview, 20 palettes, exactly 60 club wallpapers, 20 garment/native badge hashes and valid shirt projections, sourced stadiums and default Santos mirror. Visual fidelity requires the separate image review.')


if __name__ == '__main__':
    main()
