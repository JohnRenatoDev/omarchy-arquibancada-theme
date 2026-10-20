# Arquibancada

[English](README.md) | [Português (Brasil)](README.pt-BR.md)

Temas do Omarchy para os 20 clubes da Série A de 2026. Cada clube tem sua própria
paleta de interface e terminal, três wallpapers 3840×2160, prévia, ícones e cor
de teclado.

Criei este pacote para a comunidade brasileira do Omarchy e para quem quer levar
as cores do seu clube para o desktop. Nenhuma das imagens representa minha
preferência clubística. A ordem dos clubes e o tema padrão também não indicam
o time para o qual torço.

![Arquibancada em uma sessão do Omarchy, com a variante Santos](docs/desktop.png)

[Veja os 20 wallpapers de mascotes](docs/mascotes-serie-a-2026.jpg).

## Instalação

Clone o pacote e instale os temas dos clubes:

```bash
gh repo clone JohnRenatoDev/omarchy-arquibancada-theme
cd omarchy-arquibancada-theme
./install.sh --link --menu
```

O instalador acrescenta os temas dos clubes ao Omarchy. A opção de menu adiciona
as entradas ausentes e faz um backup do menu antes de alterá-lo. Temas locais que
já existam como diretórios independentes são preservados; rodar o instalador
novamente com as mesmas opções não duplica entradas no menu.

```bash
./install.sh --link --menu   # instala os 20 e completa o menu Clubes
omarchy theme set flamengo  # exemplo; use qualquer slug da tabela
omarchy theme bg next       # alterna os três wallpapers
```

Use `./install.sh --copy` se preferir uma cópia autocontida. Cada clube tem sua
própria prévia no seletor de temas do Omarchy.

Para instalar apenas a variante padrão do Santos pelo Omarchy, execute:

```bash
omarchy theme install https://github.com/JohnRenatoDev/omarchy-arquibancada-theme.git
```

Isso instala um único tema chamado `arquibancada`. Para ter os 20 clubes, use
`install.sh` a partir do repositório clonado.

## Clubes

A lista de clubes foi conferida na [lista de times da CBF](https://www.cbf.com.br/futebol-brasileiro/times/campeonato-brasileiro/serie-a/2026)
e no feed de equipes da ESPN em 19/10/2026. As artes não trazem números de temporada
ou campeonato e continuam utilizáveis fora de 2026.

| Comando / tema | Clube | Mascote |
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

1. `1-arte.jpg`: composição abstrata com cores, monograma e tipografia do clube.
2. `2-escudo.jpg`: escudo do clube, com luz e cores do tema.
3. `3-mascote.jpg`: pôster esportivo cinematográfico com uniforme e símbolo do clube.

As ilustrações dos mascotes foram geradas por IA. Cuidamos dos uniformes e dos
símbolos de cada clube, usando referências para chegar a imagens que seus
torcedores reconheçam e tenham vontade de usar. Cada mascote tem seu próprio
desenho, com o mesmo estilo cartoon semirrealista e cinematográfico. O Saci do
Internacional fica apoiado em sua única perna e segura a bola no braço.

As artes-base têm 1672×941 e são ampliadas proporcionalmente para 3840×2160,
sem cortar o personagem ou a bola. A tipografia e os arquivos originais dos
símbolos dos clubes são aplicados separadamente na resolução final.

Veja o [catálogo de wallpapers](docs/preview.png), as [referências dos uniformes](docs/uniformes-2026.md)
e as [fontes dos estádios](docs/estadios.md). As [notas de artes e desenvolvimento](docs/development.pt-BR.md)
explicam a composição e listam os arquivos de origem.

## Contribuições

Qualquer pessoa é bem-vinda para abrir um pull request e corrigir ou melhorar um
tema. Um escudo fora do lugar, um detalhe do uniforme ou uma cor que ficou
estranha merecem correção. Contribuições para os wallpapers e o instalador
também são bem-vindas.

Se você torce por um desses clubes, seu olhar para os detalhes ajuda. Inclua uma
imagem de referência ou uma prévia do antes e depois quando puder.

## Desenvolvimento

Você precisa de Python 3, ImageMagick, `rsvg-convert` e das fontes Anton, Oswald e
JetBrains Mono. As artes já fazem parte do pacote; o build dispensa gerador de
imagens, GPU ou token.

```bash
python3 src/build.py --mascotes-only  # só pôsteres e previews dos 20
python3 src/build.py flamengo gremio    # todos os wallpapers desses clubes
python3 src/build.py                    # pacote completo
```

As [notas de desenvolvimento](docs/development.pt-BR.md) e o [status da revisão](docs/mascotes-status.md)
detalham a composição e as verificações.

## Direitos e créditos

Os nomes dos clubes, escudos, mascotes e demais marcas pertencem aos respectivos
clubes e titulares. O Arquibancada é um projeto independente da comunidade, sem
caráter oficial. Ele não é patrocinado nem endossado pelos clubes, pela ESPN ou
pelo Omarchy.

A licença MIT cobre o código, os scripts e as paletas originais. Ela não concede
direitos sobre marcas, personagens, fotografias ou outros materiais de terceiros
presentes no pacote. As condições desses materiais continuam valendo, inclusive
quando uma ilustração foi gerada por IA. A arte derivada foi pensada para uso
pessoal; isso não equivale a uma autorização dos titulares. Consulte [LICENSE](LICENSE)
e [NOTICE.md](NOTICE.md).

As fontes Anton, Oswald e Archivo Black vêm do Google Fonts, sob a SIL Open Font
License 1.1, com os textos da licença incluídos. Os escudos anteriores vieram de
Wikimedia/Wikipédia; os adicionados vieram do feed gráfico da ESPN.
As [referências das identidades](docs/serie-a-2026-fontes.md) e as URLs de origem
estão registradas no projeto.
