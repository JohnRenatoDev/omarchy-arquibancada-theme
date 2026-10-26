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

Instale a variante padrão do Santos pelo Omarchy:

```bash
omarchy theme install https://github.com/JohnRenatoDev/omarchy-arquibancada-theme.git
```

Ela aparece como `arquibancada` no seletor de temas. Use `omarchy theme bg next`
para alternar entre os três wallpapers.

As variantes dos outros clubes ficam em `themes/<slug>/`, cada uma com paleta,
wallpapers e prévia próprios. As [ferramentas opcionais do Arquibancada](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/README.pt-BR.md#instalar-os-temas-dos-clubes)
permitem instalar os 20 clubes de um clone local e adicioná-los ao menu do Omarchy.
O instalador e as ferramentas de geração ficam nesse repositório separado.

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
estranha merecem correção. Contribuições para os wallpapers são bem-vindas aqui.
Mudanças no instalador e no compositor pertencem ao
[repositório de ferramentas](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools).

Se você torce por um desses clubes, seu olhar para os detalhes ajuda. Inclua uma
imagem de referência ou uma prévia do antes e depois quando puder.

## Desenvolvimento

O [repositório de ferramentas](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools) reúne as artes-base, o compositor,
o instalador e as verificações. Ele grava os arquivos finais em um checkout do
tema ou em uma pasta de exportação separada. As [notas de desenvolvimento](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/docs/development.pt-BR.md)
explicam os comandos e as dependências.

Este repositório distribui os temas prontos e sua documentação.

## Direitos e créditos

Os nomes dos clubes, escudos, mascotes e demais marcas pertencem aos respectivos
clubes e titulares. O Arquibancada é um projeto independente da comunidade, sem
caráter oficial. Ele não é patrocinado nem endossado pelos clubes, pela ESPN ou
pelo Omarchy.

As paletas originais usam a licença MIT. O código e os scripts ficam no
[repositório de ferramentas](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools), também sob MIT. A licença não concede
direitos sobre marcas, personagens, fotografias ou outros materiais de terceiros
presentes no pacote. As condições desses materiais continuam valendo, inclusive
quando uma ilustração foi gerada por IA. A arte derivada foi pensada para uso
pessoal; isso não equivale a uma autorização dos titulares. Consulte [LICENSE](LICENSE)
e [NOTICE.md](NOTICE.md).

As fontes Anton, Oswald e Archivo Black vêm do Google Fonts, sob a SIL Open Font
License 1.1, com os arquivos e as licenças no
[repositório de ferramentas](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/tree/main/assets/fonts). Os escudos anteriores vieram de
Wikimedia/Wikipédia; os adicionados vieram do feed gráfico da ESPN.
As [referências das identidades](docs/serie-a-2026-fontes.md) e as URLs de origem
estão registradas no projeto.
