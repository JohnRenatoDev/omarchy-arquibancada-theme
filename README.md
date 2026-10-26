# Arquibancada

[English](README.md) | [Português (Brasil)](README.pt-BR.md)

Omarchy themes for the 20 clubs in the 2026 Brazilian Série A. Each club has its
own interface and terminal palette, three 3840×2160 wallpapers, a preview,
icons and a keyboard color.

I made this collection for the Brazilian Omarchy community and for supporters
who want their club's colors on the desktop. None of the images represents my
personal club preference. The order of the clubs and the default theme do not
indicate which team I support.

![Arquibancada on an Omarchy desktop, using the Santos variant](docs/desktop.png)

[View all 20 mascot wallpapers](docs/mascotes-serie-a-2026.jpg).

## Installation

Install the default Santos variant through Omarchy:

```bash
omarchy theme install https://github.com/JohnRenatoDev/omarchy-arquibancada-theme.git
```

It appears as `arquibancada` in the theme picker. Use `omarchy theme bg next`
to cycle its three wallpapers.

The other club variants are in `themes/<slug>/`, each with its own palette,
wallpapers and preview. The optional [Arquibancada tools](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools#install-the-club-themes)
can install all 20 clubs from a local clone and add them to the Omarchy menu.
The installer and build tools live in that separate repository.

## Clubs

The club list was checked against the [CBF team list](https://www.cbf.com.br/futebol-brasileiro/times/campeonato-brasileiro/serie-a/2026)
and ESPN's team feed on October 19, 2026. The artwork has no season or championship
numbers, so it can still be used beyond 2026.

| Command / theme | Club | Mascot |
|---|---|---|
| `santos` | Santos | Baleia |
| `corinthians` | Corinthians | Mosqueteiro |
| `palmeiras` | Palmeiras | Periquito |
| `sao-paulo` | São Paulo | Santo Paulo |
| `athletico-paranaense` | Athletico | Fura-Cão |
| `atletico-mineiro` | Atlético-MG | Galo |
| `bahia` | Bahia | Homem de Aço |
| `botafogo` | Botafogo | Bira |
| `chapecoense` | Chapecoense | Guerreiro Condá |
| `coritiba` | Coritiba | Vovô Coxa |
| `cruzeiro` | Cruzeiro | Raposão |
| `flamengo` | Flamengo | Urubu |
| `fluminense` | Fluminense | Guerreiro |
| `gremio` | Grêmio | Mosqueteiro |
| `internacional` | Internacional | Saci |
| `mirassol` | Mirassol | Leão |
| `red-bull-bragantino` | Bragantino | Toro Loko |
| `remo` | Remo | Leão Azul |
| `vasco` | Vasco da Gama | Almirante |
| `vitoria` | Vitória | Leão |

## Wallpapers

1. `1-arte.jpg`: an abstract composition with the club's colors, monogram and typography.
2. `2-escudo.jpg`: the club crest, with lighting and colors from the theme.
3. `3-mascote.jpg`: a cinematic sports poster with the club's kit and shirt emblem.

The mascot illustrations were generated with AI. We took care with each club's
uniforms and symbols, using references to make artwork its supporters could
recognize and enjoy. Each mascot has its own design, in a shared cinematic,
semirealistic cartoon style. Internacional's Saci stands on his single leg and
holds the ball in his arm.

The base illustrations are 1672×941, proportionally enlarged to 3840×2160 without
cropping the character or ball. Typography and original club badges are added
separately at the final resolution.

See the [wallpaper catalog](docs/preview.png), [kit references](docs/uniformes-2026.md)
and [stadium sources](docs/estadios.md). The [artwork and build notes](docs/development.md)
explain the composition and list the source files.

## Contributing

Anyone is welcome to open a pull request to fix or improve a theme. A misplaced
crest, a kit detail or a color that looks wrong is worth correcting. Wallpaper
contributions are welcome here. Changes to the installer or
compositor belong in the [tools repository](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools).

If you support one of these clubs, your eye for its details helps. Include a
reference image or a before-and-after preview when you can.

## Development

The [tools repository](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools) contains the artwork sources, compositor,
installer and validation checks. It writes finished files to a separate theme
checkout or export directory. See its [build notes](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/docs/development.md)
for the commands and dependencies.

This repository distributes the finished themes and their documentation.

## Rights and credits

Club names, crests, mascots and other marks belong to their respective clubs and
rights holders. Arquibancada is an independent community project, not an official
release. It is not sponsored or endorsed by the clubs, ESPN or Omarchy.

The original palettes use the MIT license. Code and scripts are maintained
under MIT in the [tools repository](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools). That license does
not grant rights to third-party marks, characters, photographs or other materials
in the package. Their own terms still apply, including when an illustration was
generated with AI. The derivative artwork is intended for personal use; that does
not amount to permission from the rights holders. See [LICENSE](LICENSE) and
[NOTICE.md](NOTICE.md).

Anton, Oswald and Archivo Black are from Google Fonts under the SIL Open Font
License 1.1, with their font files and licenses in the [tools repository](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/tree/main/assets/fonts). Earlier crests came from
Wikimedia/Wikipedia; the added crests came from ESPN's graphics feed.
[Club identity references](docs/serie-a-2026-fontes.md) and source URLs are recorded
in the project.
