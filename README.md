# Invoice Challenge
Escrever uma API RESTful que permita gerenciar um recurso chamado Invoice (Nota Fiscal).

#### Requisitos
  - O desenvolvimento da API deve ser realizado utilizando a linguagem Python
  - Não é permitido a utilização de nenhum tipo de ORM para acesso ao banco de dados
  - A API deve ser coberta por testes de unidade
  - Atenção para utilizar os status codes do HTTP corretamente de acordo com cada operação da API
  - A API deve possuir um mecanismo de autenticação baseado em token
  - Sobre a listagem de **Invoices**:
  - - Deve ser possível filtrar por mês, ano ou documento
  - - Deve ser possível realizar a ordenação por mês, ano, documento ou combinações entre eles
  - - Deve ser paginada
  - O método **DELETE** não executa uma deleção física, somente uma deleção lógica
  - - Ou seja, só deverá ser possível desativar uma **Invoice**
  - O código final deve estar versionado e publicado em um repositório no GitHub
  - - Este repositório deve conter um arquivo `README.md` com as instruções necessárias para a execução da API

Domínio da entidade Invoice:
```sh
{
    Id: UUID,
    Document: STRING,
    Description: STRING,
    Amount: CURRENCY,
    ReferenceMonth: DATETIME,
    ReferenceYear: INT,
    CreatedAt: DATETIME,
    IsActive: BOOL,
    DeactiveAt: DATETIME
}
```
#### Bônus
  - API rodando em container
#### Critérios de avaliação
  - Arquitetura e organização do projeto
  - Legibilidade do código
  - Utilização de padrões e boas práticas de programação

## Installation
The following installation instructions are meant for Ubuntu distros

#### Requirements
  - Docker
  - Docker Compose

#### Setup
Export the following environment variables:
```zsh
export MYSQL_HOST=localhost
export MYSQL_ROOT_PASSWORD=password
export MYSQL_DATABASE=invoice_challenge
export MYSQL_PORT=3306
export MYSQL_ROOT_USER=root
export SECREAT_KEY=a_random_secret_key
```

#### Preparing environment

1. Clone Repo
```zsh
git clone git@github.com:rlobotech/invoice-challenge.git
```

2. Install Docker Engine [Link](https://docs.docker.com/engine/install/ubuntu/)
3. Install Docker Compose [Link](https://docs.docker.com/compose/install/)
4. Run Docker Compose on the root directory of the repo `../invoice-challenge`
```zsh
docker-compose up
```
5. **You are ready to go!**

## Using the API
By default, the API server will run on port 5000 (it may be changed on the docker-compose.yml file).

```zsh
http://localhost:5000/api/v1/invoices
http://localhost:5000/api/v1/invoices/{id}
http://localhost:5000/api/v1/users
http://localhost:5000/api/v1/login
```

#### For route http://localhost:5000/api/v1/invoices [GET, POST]
#### For route http://localhost:5000/api/v1/invoices/{id} [GET, PUT, DELETE]
#### For route http://localhost:5000/api/v1/users [GET, POST]
#### For route http://localhost:5000/api/v1/login [GET, POST]

##### Obs:
  - The user table already contains an admin user which:
  - - email: `admin@admin`
  - - password: `admin`
  - To get the `auth-token` do a POST request on `../api/v1/login` route passing as params `email` and `password`.
  - To acess any other route it will need to pass as authentication an API KEY:
  - - key: token
  - - value: `auth-token`

### Filters, Paging and Sorting
**Generals Rules:**
  - Start any query with the `?` operator
  - Split query args with the `&` operator

##### Filter
In order to filter by a specific column, use the following examples:
```zsh
.../api/v1/table_name?column_a='column_a_value'&column_b='column_b_value'&...
.../api/v1/invoices?document='newspaper'&amount=10
.../api/v1/invoices?amount=11
```
**Filter rules:**
  - Any string value should be in 'quotes' or "double quotes"

##### Paging
In order to page or limit the page size, use the following examples:
```zsh
.../api/v1/table_name?pageSize=number&page=number
.../api/v1/invoices?page=43&pageSize=100
.../api/v1/invoices?pageSize=32
.../api/v1/invoices?page=3
```

##### Sorting
In order to sorting, use the following examples:
```zsh
.../api/v1/table_name?oder_by_asc=column_a,column_b&order_by_desc=column_c
.../api/v1/invoices?oder_by_asc=amount,description&order_by_desc=document
.../api/v1/invoices?order_by_desc=document
```
**Sorting rules:**
  - It will always order by desc first then by asc (It will ignore the order of ASC and DESC in the URL)

##### Final Obs:
  - It is possible, but not necessary, to create a user passing as params `email` and `password`.
  - It is possible to login using the default admin user by accessing the `../api/v1/login` url.
  - - This is just for testing the session on the URL. By production this route should not exist.
