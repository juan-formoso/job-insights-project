# Job Insights Project :briefcase:

# Contexto :open_book:
O objetivo do projeto é implementar análises a partir de um conjunto de dados sobre empregos. As implementações foram incorporadas a um aplicativo Web desenvolvido com **Flask**. Além de escrever testes para a implementação de uma análise de dados. Por fim, o desenvolvimento de rotas e views para a aplicação web! 💻

Os dados foram extraídos do site [Glassdoor](https://www.glassdoor.com.br/) e obtidos através do [Kaggle](https://www.kaggle.com/atharvap329/glassdoor-data-science-job-data), uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

## Tecnologias usadas :telescope:

Desenvolvido usando:
> Python, Flask

## Habilidades treinadas 🚵

* Utilizar o terminal interativo do **Python**.
* Utilizar estruturas condicionais e de repetição.
* Utilizar funções built-in do **Python**.
* Utilizar tratamento de exceções.
* Realizar a manipulação de arquivos.
* Escrever funções em **Python**.
* Escrever testes com **Pytest**.
* Escrever meus próprios módulos e importá-los em outros códigos.

## Clonando o repositório :dna:

1. Faça a clonagem
  - Use o comando: `git clone git@github.com:juan-formoso/job-insights-project.git`.
  - Entre na pasta do repositório clonado:
    - `cd job-insights-project`

2. Crie o ambiente virtual para o projeto
  - `python3 -m venv .venv && source .venv/bin/activate`
  
3. Instale as dependências
  - `python3 -m pip install -r dev-requirements.txt`
  
4. Crie uma branch a partir da branch `main`
  * `git checkout -b my-new-branch`

5. Se divirta para fazer o que quiser. ;)

### Estrutura do projeto :building_construction:

  ```
  .
  ├── README.md
  ├── Dockerfile
  ├── docker-compose.yml
  ├── dev-requirements.txt
  ├── requirements.txt
  ├── src
  │   ├── app.py
  │   ├── brazilian_jobs.py
  │   ├── counter.py
  │   ├── insights.py
  │   ├── jobs.csv
  │   ├── jobs.py
  │   ├── more_insights.py
  │   ├── routes_and_views.py
  │   ├── sorting.py
  │   └── templates
  │       ├── base.jinja2
  │       ├── includes
  │       │   └── nav.jinja2
  │       ├── index.jinja2
  │       ├── job.jinja2
  │       └── list_jobs.jinja2
  ├── tests
  │   ├── __init__.py
  │   ├── conftest.py
  │   ├── marker.py
  │   ├── brazilian
  │   │   ├── __init__.py
  │   │   ├── conftest.py
  │   │   ├── mocks.py
  │   │   ├── test_brazilian_jobs.py
  │   ├── counter
  │   │   ├── __init__.py
  │   │   ├── conftest.py
  │   │   ├── mocks.py
  │   │   ├── test_counter.py
  │   ├── mocks
  │   │   ├── job_1.html
  │   │   ├── jobs.csv
  │   │   ├── jobs_with_industries.csv
  │   │   ├── jobs_with_salaries.csv
  │   │   └── jobs_with_types.csv
  │   ├── sorting
  │   │   ├── __init__.py
  │   │   ├── conftest.py
  │   │   ├── mocks.py
  │   │   └── test_sorting.py
  │   ├── test_flask_app.py
  │   ├── test_insights.py
  │   ├── test_jobs.py
  │   ├── test_more_insights.py
  │   └── test_routes_and_views.py
  ```

### Ambiente Virtual 🏕️
O **Python** oferece um recurso chamado de ambiente virtual, onde permite a máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. **Criar o ambiente virtual**
  ```bash
  $ python3 -m venv .venv
  ```

2. **Ativar o ambiente virtual**
  ```bash
  $ source .venv/bin/activate
  ```

3. **Instalar as dependências no ambiente virtual**
  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

Com o ambiente virtual ativo, as dependências serão instaladas neste ambiente.
Para **desativar** o ambiente virtual execute o comando: `deactivate`.

O arquivo `dev-requirements.txt` contém todas as dependências utilizadas no projeto.


### Executando os testes 🛠
Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

- **Executar os testes**
  ```bash
  $ python3 -m pytest
  ```

- O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:
  ```bash
  python3 -m pytest -s -vv
  ```

- Caso precise executar apenas um arquivo de testes basta executar o comando:
  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

- Caso precise executar apenas uma função de testes basta executar o comando:
  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

- Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`
  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
- Para executar um teste específico de um arquivo, basta executar o comando:
  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

**OBS: Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1). :grinning:**
  
### Rodando o App :hot_pepper:
Para rodar a aplicação **Flask**, digite o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`.
