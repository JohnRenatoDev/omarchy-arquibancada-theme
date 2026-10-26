# Revisão dos brasões e dos mascotes

Revisão 5 de 20/10/2026. O pacote contém 20 temas e 60 wallpapers em 3840×2160,
com exatamente `1-arte.jpg`, `2-escudo.jpg` e `3-mascote.jpg` por clube.

## Atualização do Saci

A versão aprovada em 20/10/2026 substitui a pose anterior do Internacional.
O Saci mantém sua única perna apoiada no gramado e segura uma bola no braço
direito. O uniforme, a identidade do personagem e o estádio foram mantidos.
O símbolo original da camisa continua separado da pintura e usa a mesma
superfície de aplicação revista. O prompt e os hashes estão em
[assets/mascotes-generated/internacional-pose-revisao.json](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/assets/mascotes-generated/internacional-pose-revisao.json).

O wallpaper do Internacional e as prévias do clube e do pacote foram atualizados.
Os demais pôsteres e os dois primeiros wallpapers de todos os clubes foram
preservados.

## Correção da aplicação

A aplicação plana anterior girava o arquivo sem representar a perspectiva do
peito. Esta revisão usa uma superfície individual em cada mascote, ajustada
pela gola, esterno, cava da manga e dobra peitoral. O arquivo original é
projetado nessa superfície: letras, monogramas e estrelas mantêm seu desenho,
enquanto o conjunto acompanha a posição da câmera e o volume da camisa.

A projeção usa uma malha contínua, curvatura suave, luz, trama e suavização de
borda. O arquivo real continua separado da pintura; a IA não redesenha os brasões.
O código está em [src/badge_surface.py](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/src/badge_surface.py) e os pontos em [src/mascotes-layout.json](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/src/mascotes-layout.json).

Foram revistos os 20 encaixes, inclusive as aplicações centrais de São Paulo e
Coritiba. Santos e Palmeiras receberam o encaixe no peitoral afastado da câmera;
Corinthians mantém folga em relação à dobra da axila. A cruz do Vasco foi
reposicionada dentro da faixa branca. O CRF do Flamengo foi reduzido e elevado
para a faixa vermelha, com a estrela dourada na parte preta acima, como na foto. As demais posições também foram revistas em
ampliação, com folga em relação à gola, à manga e às costuras.

São Paulo recebeu duas edições de camisa com a ferramenta integrada `image_gen`:
redução da área branca central e correção da altura das faixas. A área branca
acompanha o tecido da camisa de referência. As cinco estrelas seguem a disposição
fotografada: uma vermelha acima da linha dourada/vermelha/vermelha/dourada.
Na revisão 5 dos brasões, as outras 19 bases PNG permaneceram iguais à revisão 4.
A base do Internacional foi substituída depois pela pose aprovada descrita acima.

## Conferência

A conferência visual usa detalhes ampliados dos 20 clubes e a galeria completa.
O comparativo `brasoes-antes-depois.jpg` mostra seis aplicações antes e depois
desta revisão: Santos, Corinthians, Palmeiras, São Paulo, Flamengo e Vasco.

Além da inspeção, [scripts/validate_badge_regions.py](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/scripts/validate_badge_regions.py) verifica os pixels reais
do tecido sob a cruz do Vasco, o monograma CRF e sua estrela dourada, para
detectar invasão da região errada. Os testes de `badge_surface` verificam projeção, continuidade
e rejeição de superfícies espelhadas ou dobradas. Essas verificações complementam
a revisão visual.

Os 40 fundos de arte e escudo foram preservados byte a byte em relação ao commit
`c1734e32de29944a4204ee091c60344da14364ef`. A revisão dos brasões preservou paletas,
estádios, mascotes, corpo inteiro, bola e enquadramento. A atualização posterior
do Internacional muda apenas sua pose e a posição da bola.

## Arquivos

- `uniformes-revisao.jpg`: as 20 aplicações após a composição final.
- `brasoes-antes-depois.jpg`: comparativo entre as revisões 4 e 5.
- `mascotes-cartoon.png` e `mascotes-serie-a-2026.jpg`: galeria dos 20 pôsteres.
- `preview.png`: catálogo com os três fundos de cada clube.
- `mascotes-verificacao.json` e `serie-a-2026-verificacao.json`: integridade e fontes.
- `uniformes-2026.md`: fotografias e versões dos símbolos usadas como referência.
- `estadios.md` e [src/estadios.json](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/src/estadios.json): fontes dos nomes dos estádios, preservadas.

As bases têm 1672×941. As saídas 4K são ampliações proporcionais com a imagem
inteira contida no quadro; os símbolos e a tipografia são compostos na resolução
final. Prompts e histórico: [assets/mascotes-generated/uniformes-2026-prompts.json](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools/blob/main/assets/mascotes-generated/uniformes-2026-prompts.json).
O serviço não expõe seed, passos ou versão interna do modelo.

A reprodução e as verificações são executadas no [repositório de ferramentas](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools).
Os comandos recebem o checkout do tema como destino ou entrada. A composição
usa as artes salvas e não exige gerador, GPU ou token.

Em 26/10/2026, as ferramentas e os arquivos de entrada foram separados da
distribuição para atender ao pedido do catálogo. Os wallpapers e as paletas
foram preservados.
