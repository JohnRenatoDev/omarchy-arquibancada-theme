# Conferência da publicação

Preparação autorizada em 20/10/2026 para publicar o Arquibancada e submetê-lo ao
catálogo de temas do Omarchy.

## Pacote distribuído

- A raiz contém a variante Santos instalável, com paleta, três wallpapers e
  prévia 16:9. Os 20 clubes também têm suas próprias pastas em `themes/`.
- São 60 wallpapers em 3840×2160. As ilustrações nativas têm 1672×941 e são
  ampliadas proporcionalmente; a tipografia e os símbolos originais dos clubes
  são compostos na resolução final.
- O Saci do Internacional usa a pose aprovada, segurando a bola no braço,
  com sua única perna apoiada no gramado.
- O README está em inglês e PT-BR, com instalação, captura do desktop, galeria,
  convite para contribuições e os avisos de direitos e de geração por IA.
- A validação dos 20 temas, os quatro testes de projeção, a conferência das
  regiões de tecido e a sintaxe do instalador passaram localmente.
- O teste isolado do instalador conferiu links, cópias, backup do menu,
  repetição sem duplicar entradas e preservação de temas locais independentes.

## Captura para o catálogo

`desktop.png` mostra uma sessão real do Omarchy com a variante Santos, um
terminal e o Neovim. As janelas foram abertas apenas com dados do projeto.
A captura foi conferida visualmente, sem cursor, notificações ou dados pessoais.

A versão destinada ao site tem 1200×675, formato WebP, metadados removidos e
menos de 100 KB. A entrada do Arquibancada aponta para o repositório do pacote
nos dois links e foi inserida após Archwave.

As exigências foram conferidas no [guia oficial de submissão](https://github.com/omacom/omarchy-site#adding-your-theme).
O PR adiciona apenas a imagem em `assets/themes/arquibancada.webp` e a entrada
em `themes/index.html`. A inclusão no catálogo depende da revisão dos mantenedores.

## Privacidade e histórico

A distribuição pública começa com um histórico novo. O histórico privado de
desenvolvimento foi preservado fora dela, incluindo os arquivos antigos que
continham um caminho da estação e uma resposta de erro com dados de conexão.
Esses arquivos não fazem parte da publicação.

Fotografias e obras baixadas apenas para pesquisa dos protótipos também foram
retiradas. A pasta de pesquisa `assets/mascots/` fica ignorada pelo Git. As URLs
de referência continuam registradas; os temas usam as artes geradas e revisadas.

Todos os PNGs e JPEGs distribuídos tiveram seus formatos conferidos. Os arquivos
de código executável e CI permaneceram iguais aos da revisão de segurança.
A análise não apontou credenciais ou vulnerabilidade explorável no código
revisado. Ela não certifica componentes externos, conteúdo comprimido de imagens
ou programas internos das fontes.

## Direitos e instalação

`LICENSE` cobre o código, os scripts e as paletas originais sob MIT. `NOTICE.md`
preserva os créditos e distingue os materiais dos respectivos titulares.
As licenças das fontes acompanham os arquivos. Este é um projeto independente,
sem patrocínio ou endosso dos clubes, da ESPN ou do Omarchy. A publicação e o
uso de IA não concedem direitos sobre marcas ou personagens de terceiros.

O formato nativo foi conferido com a [documentação de temas do Omarchy](https://github.com/omacom/omarchy/blob/quattro/docs/theming.md).
A instalação por URL oferece a variante padrão; o instalador do pacote oferece
os 20 clubes. O acesso anônimo ao repositório será conferido antes da submissão.
