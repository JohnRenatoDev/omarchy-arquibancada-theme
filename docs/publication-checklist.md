# Conferência da publicação

A distribuição foi reorganizada em 26/10/2026 para atender ao pedido no
[PR do catálogo](https://github.com/omacom/omarchy-site/pull/593#issuecomment-6385084239).

## Distribuição do tema

Este repositório contém os temas prontos e a documentação. A raiz é a variante
Santos instalável por `omarchy theme install`; os 20 clubes ficam em `themes/`.
Cada clube mantém três wallpapers 3840×2160, paleta e prévia próprios.

Os programas, os arquivos de entrada e a automação de validação ficam no
[Arquibancada tools](https://github.com/JohnRenatoDev/omarchy-arquibancada-tools).
O repositório do tema não contém instaladores, geradores, testes ou workflows,
inclusive em subpastas. As ferramentas usam caminhos explícitos para o checkout
do tema e mantêm os intermediários fora dele.

Os 176 arquivos visuais e de configuração foram preservados byte a byte,
incluindo os 60 wallpapers dos clubes, as prévias, as paletas e o espelho do Santos
na raiz. As ilustrações-base e os arquivos originais dos símbolos das camisas
foram preservados no repositório de ferramentas. A revisão do Saci continua na
pose aprovada, com uma única perna apoiada no gramado e a bola no braço.

## Verificações da separação

- Validação da distribuição sem código e dos 20 temas.
- Conferência das dimensões, dos hashes das artes-base e das superfícies dos brasões.
- Testes de instalação a partir de uma pasta externa, links, cópias, backup do
  menu, repetição sem duplicar entradas e preservação de temas independentes.
- Testes que rejeitam código em subpastas, workflows, arquivos executáveis,
  scripts com extensão de documentação e links simbólicos na distribuição.
- Reconstrução do Santos e das galerias em uma pasta isolada, sem alterar os
  arquivos distribuídos nem o tema ativo do usuário.
- Verificação das regiões de tecido do Vasco e do Flamengo.

Os comandos de validação e o workflow ficam no repositório de ferramentas.

## Catálogo e documentação

O PR do site mantém apenas a captura WebP e a entrada do Arquibancada em ordem
alfabética. A captura real do desktop permanece igual: 1200×675, 98.556 bytes,
com terminal e editor, sem dados pessoais e com metadados removidos.

Os READMEs em inglês e PT-BR mostram a instalação nativa primeiro e apontam para
a ferramenta opcional de instalação dos 20 clubes. Prompts, fontes e detalhes
de composição continuam acessíveis por links para o repositório de ferramentas.
A inclusão no catálogo depende da avaliação dos mantenedores.

## Direitos e histórico

As paletas originais usam MIT; o código e os scripts mantêm a licença MIT no
repositório de ferramentas. As licenças das fontes acompanham os arquivos de
entrada. Nomes, escudos, mascotes e demais marcas continuam pertencendo aos
respectivos titulares. O projeto é independente e as imagens são geradas por IA,
sem indicar preferência clubística do autor. Consulte [NOTICE.md](../NOTICE.md).

A separação usa commits normais e preserva o histórico público. O antigo histórico
privado de desenvolvimento continua no arquivo privado, fora dos dois repositórios
públicos. Fotografias usadas apenas como referência não são distribuídas.
