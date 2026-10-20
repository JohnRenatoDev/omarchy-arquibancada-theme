# Artes e desenvolvimento

[README](../README.pt-BR.md) | [English](development.md) | [Português (Brasil)](development.pt-BR.md)

Os caminhos abaixo são relativos à raiz do repositório.

## Três wallpapers por clube

Os nomes dos estádios foram conferidos em fontes primárias em 19/10/2026.
[docs/estadios.md](estadios.md) reúne as referências e as observações sobre
mandos temporários. Palmeiras usa Nubank Parque; São Paulo usa MorumBIS. As
legendas de Palmeiras, São Paulo, Bahia e Mirassol têm os nomes atualizados.

Os 20 uniformes foram revistos com fotografias das camisas de 2026, registradas em
[docs/uniformes-2026.md](uniformes-2026.md). A revisão de 20/10 usa os arquivos
originais dos brasões projetados sobre a superfície de cada camisa, acompanhando
a perspectiva e a curvatura do peitoral, com luz e trama de tecido. Letras e
estrelas conservam o desenho original. Posição, escala e folgas foram revistas
em todos os clubes. São Paulo e Coritiba usam escudo central; os demais seguem
o peitoral esquerdo de quem veste. Flamengo usa CRF, Cruzeiro as cinco estrelas
e Vasco a cruz dentro da faixa branca. A composição ao redor mantém o escudo
completo do clube.

O Saci do Internacional mantém sua única perna apoiada no gramado e segura a bola
no braço. Athletico usa Fura-Cão; Botafogo usa Bira; Bahia usa Homem de Aço;
Fluminense usa Guerreiro. Leões, aves e personagens humanos têm uniforme, anatomia
e cores próprios. As camisas seguem fotografias dos modelos atuais, e os símbolos
usam os arquivos originais separados. Não foram adicionados patrocinadores.

## Arquivos e prévias

- `themes/<slug>/`: paleta, três JPEGs, prévia e arquivos extras do Omarchy.
- `assets/mascotes-generated/<slug>.png`: 20 artes-base independentes.
- `assets/mascotes-generated/prompts.json`: prompts dos quatro primeiros clubes.
- `assets/mascotes-generated/serie-a-2026-prompts.json`: prompts dos outros 16 e
  correções de enquadramento de Atlético-MG, Chapecoense, Cruzeiro e Fluminense.
- `assets/mascotes-generated/uniformes-2026-prompts.json`: prompts e referências
  das 20 edições de camisa feitas com a ferramenta integrada `image_gen`.
- `assets/crests/serie-a-2026-sources.json`: URLs dos 16 escudos adicionados.
- `assets/kit-badges/`: variantes dos símbolos de camisa, com fontes em `sources.json`.
- `src/badge_surface.py`: projeção do símbolo original sobre a superfície da camisa.
- `src/mascotes-layout.json`: modelo de camisa, posição anatômica, fontes e hashes
  da arte e do símbolo de cada clube, com os quatro pontos da superfície da camisa
  e sua curvatura para projetar o desenho original conforme a pose.
- [Camisas atuais e referências da revisão](uniformes-2026.md).
- [Estádios e fontes oficiais](estadios.md).
- [Revisão ampliada das camisas](uniformes-revisao.jpg).
- [Prévia dos 20 pôsteres](mascotes-cartoon.png).
- [Catálogo dos 60 wallpapers](preview.png), com uma linha por clube e três colunas.
- [Status e revisão](mascotes-status.md).
- [Verificação de integridade](serie-a-2026-verificacao.json).
- [Fontes das identidades](serie-a-2026-fontes.md).

## Geração por IA e resolução

As ilustrações foram geradas com a ferramenta integrada `image_gen`, usando a arte
Santos aprovada como referência comum de estilo, câmera e iluminação. O serviço
não expõe seed, número de passos ou versão interna do modelo. Os PNGs nativos têm
1672×941; os JPEGs 3840×2160 são ampliações proporcionais com a imagem inteira
contida no quadro. Não são gerações nativas em 4K.

A tipografia e os escudos da composição são montados separadamente em resolução
final. Os emblemas das camisas também usam os arquivos originais em uma camada
separada. As bases PNG em `assets/mascotes-generated/` contêm o tecido sem brasão;
o compositor produz o wallpaper final.

## Reproduzir o build

Você precisa de Python 3, ImageMagick, `rsvg-convert` e das fontes Anton, Oswald e
JetBrains Mono. As artes geradas fazem parte do pacote, então o build dispensa
gerador de imagens, GPU ou token. A falta de uma arte gera um erro, sem retorno
a SVG simplificado.

```bash
python3 src/build.py --mascotes-only  # só pôsteres e previews dos 20
python3 src/build.py flamengo gremio    # todos os wallpapers desses clubes
python3 src/build.py                    # pacote completo
```

`src/teams.py` mantém os dados dos quatro clubes originais e carrega os demais de
`src/serie_a_2026.json`. Para acrescentar um clube, inclua seus dados, escudo real
e uma arte de mascote própria, gerada e revisada. Não basta mudar a cor do mascote
de outro clube.

As folhas de prévias usam miniaturas intermediárias para evitar carregar os 60
wallpapers 4K ao mesmo tempo na memória. As exportações preservam a textura
pintada das ilustrações, sem adicionar ruído sintético pesado.

## Estrutura dos temas

O repositório segue a convenção `omarchy-arquibancada-theme`. A raiz contém a
variante do Santos, com `colors.toml`, `backgrounds/`, `preview.png` 16:9,
`icons.theme`, `keyboard.rgb` e `shell.lock.toml`. Cada clube, incluindo o Santos,
também tem a mesma estrutura de tema em `themes/<slug>/`.

Os exemplos de instalação usam Git e a CLI do GitHub (`gh`). A etapa opcional
`--menu` precisa de Python 3. O modo de links acompanha mudanças futuras no
checkout. O modo de cópia mantém uma versão independente; uma nova execução
preserva essa cópia existente, sem atualizá-la automaticamente.
