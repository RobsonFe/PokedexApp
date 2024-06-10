# Pokedex Application

## Descrição do Projeto

Este projeto é uma aplicação web completa que exibe uma lista de Pokémons, permitindo a ordenação alfabética e a exportação dos dados em formato XML. O backend é implementado usando FastAPI, e o frontend é desenvolvido em Angular com renderização do lado do servidor (SSR). Além disso, o projeto está configurado para CI/CD usando GitHub Actions.

## Tecnologias Utilizadas

### Backend

- **FastAPI**: Framework moderno e rápido para construir APIs com Python 3.6+ baseado em padrões OpenAPI e JSON Schema.
- **SQLAlchemy**: Biblioteca SQL para mapeamento objeto-relacional (ORM) em Python.
- **PostgreSQL**: Sistema de gerenciamento de banco de dados relacional.
- **Docker**: Plataforma para desenvolvimento, envio e execução de aplicações dentro de contêineres.
- **xmltodict**: Biblioteca Python para converter dicionários em XML.

### Frontend

- **Angular**: Framework para construção de aplicações web dinâmicas.
- **Angular Universal**: Para renderização do lado do servidor (SSR).

### CI/CD

- **GitHub Actions**: Plataforma de integração contínua e entrega contínua (CI/CD) integrada ao GitHub.

## Funcionalidades

- Exibição de uma lista de Pokémons ordenados alfabeticamente.
- Exportação da lista de Pokémons em formato XML.
- Renderização do lado do servidor para melhorar a performance e SEO.
- Pipeline de CI/CD para testes e implantação contínuos.

## Configuração do Projeto

### Pré-requisitos

- Docker
- Docker Compose

### Configuração do Backend

1. Clone o repositório:

   ```sh
   git clone https://github.com/seu-usuario/pokedex.git
   cd pokedex
   ```

2. Crie e ative um ambiente virtual:

   ```sh
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```sh
   pip install -r pokedex-backend/requirements.txt
   ```

4. Configure o banco de dados PostgreSQL e ajuste a URL do banco de dados em `pokedex-backend/app/database.py`.

5. Execute a aplicação:
   ```sh
   uvicorn pokedex-backend.app.main:app --reload
   ```

### Configuração do Frontend

1. Navegue até o diretório do frontend:

   ```sh
   cd pokedex-frontend
   ```

2. Instale as dependências:

   ```sh
   npm install
   ```

3. Execute a aplicação:
   ```sh
   npm run dev:ssr
   ```

### Configuração do Docker

1. Construa e inicie os contêineres:
   ```sh
   docker-compose up --build
   ```

### Configuração do CI/CD com GitHub Actions

1. Adicione as seguintes secrets ao seu repositório GitHub:

   - **SSH_PRIVATE_KEY**: Chave privada SSH para acessar a instância EC2.
   - **EC2_HOST**: Endereço IP público da instância EC2.
   - **DOCKER_USERNAME**: Seu nome de usuário do Docker Hub.
   - **DOCKER_PASSWORD**: Sua senha do Docker Hub.

2. O arquivo de configuração do GitHub Actions `.github/workflows/ci-cd.yml` já está configurado para executar testes, construir e implantar o projeto.

### Implantação na AWS EC2

1. Configure uma instância EC2 e instale Docker conforme instruções fornecidas no início deste README.
2. O pipeline CI/CD cuidará da implantação contínua na instância EC2 configurada.

## Uso

### Exibir Pokémons

1. Acesse a aplicação no seu navegador (geralmente disponível em `http://localhost:4200`).
2. Veja a lista de Pokémons ordenada alfabeticamente.

### Exportar Pokémons para XML

1. Clique no botão "Export to XML" na página principal da aplicação.
2. O download do arquivo `pokemons.xml` será iniciado automaticamente.

## Testes

### Backend

1. Navegue até o diretório do backend:
   ```sh
   cd pokedex-backend
   ```
2. Execute os testes:
   ```sh
   pytest
   ```

### Frontend

1. Navegue até o diretório do frontend:
   ```sh
   cd pokedex-frontend
   ```
2. Execute os testes:
   ```sh
   npm run test -- --watch=false
   ```

## Licença

Este projeto está licenciado sob os termos da licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor

[Robson Ferreira](https://github.com/RobsonFe)
