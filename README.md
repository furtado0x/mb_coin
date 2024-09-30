# Coin Price API

Este projeto é uma API para obter informações de preço de moedas, construída com **FastAPI** e utilizando a **Arquitetura Hexagonal**.

## Arquitetura Hexagonal

A arquitetura hexagonal, também conhecida como **Ports and Adapters**, foi usada para manter o núcleo da aplicação independente de detalhes de implementação. Isso significa que as regras de negócio (casos de uso) estão desacopladas de elementos como repositórios, APIs externas ou serviços de cache.

### Estrutura do Projeto

- **Domain**: Contém as entidades e o núcleo do domínio.
- **Ports**: Define as abstrações (interfaces) para interagir com o núcleo, como os gateways e repositórios.
- **Adapters**: Contém as implementações dessas abstrações, como integrações com APIs externas ou caches.

## Como Rodar a API

Para rodar a API localmente, siga os passos abaixo:

### 1. Instalação de Dependências

Certifique-se de ter o **Docker** e o **Docker Compose** instalados na sua máquina.

### 2. Executar a API

No diretório raiz do projeto, basta rodar o comando abaixo para construir e iniciar os containers necessários:

\`\`\`bash
make api
\`\`\`

Isso irá subir a aplicação, juntamente com todos os serviços necessários, como o Redis.

A API estará disponível em: \`http://localhost:8008\`.

### 3. Autenticação

Para testar as rotas protegidas da API, você precisará utilizar o seguinte usuário e senha para autenticação:

- **Usuário**: \`user_1\`
- **Senha**: \`senha123\`


## Testando a API

Você pode testar a API utilizando ferramentas como o **Postman** ou **cURL**. Abaixo está um exemplo de como realizar uma chamada autenticada:

\`\`\`bash
curl --location 'http://localhost:8008/coin_infos' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic dXNlcl8xOnNlbmhhMTIz' \
--data '{
    "symbol": "BTC"
  }'
\`\`\`

### Estrutura do Projeto

O projeto está organizado da seguinte forma:

\`\`\`
/src
  /domain      # Contém as entidades e regras de negócio
  /ports       # Contém as interfaces que definem como as camadas externas interagem com o núcleo
  /adapters    # Implementações das interfaces, como gateways de APIs externas e caches
Dockerfile     # Definição da imagem Docker
docker-compose.yml  # Arquivo de configuração do Docker Compose
Makefile       # Arquivo Makefile para automatização de tarefas
\`\`\`