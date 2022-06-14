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

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Se desejar que os testes parem de ser executados quando acontecer o primeiro erro, use o parâmetro `-x`

  ```bash
  python3 -m pytest -x tests/test_jobs.py
  ```
  
  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

  Se quiser saber mais sobre a instalação de dependências com `pip`, veja esse [artigo](https://medium.com/python-pandemonium/better-python-dependency-and-package-management-b5d8ea29dff1).

  <p align="center">
    <img src="/.images/flask-logo.png" alt="Logo Flask" width="200"/>
  </p>

  Além dos testes com o Pytest, você pode (e vai ser bem bacana) rodar a aplicação flask para visualizar no navegador o resultado do desenvolvimento das funções.
  Para isso, digite o comando `flask run`, e acesse o site gerado pelo Flask em `http://localhost:5000`. No começo do desenvolvimento, você verá que muitas coisas não funcionam, mas conforme você for implementando os requisitos, perceberá que a aplicação web começa a utilizar suas implementações e passa a ganhar vida.

  <p align="center">
    <img src="/.images/sistema.png" alt="Tela Aplicação" width="800"/>
  </p>

</details>


<details>
  <summary><strong>🤝 Depois de terminar o desenvolvimento (opcional)</strong></summary><br />

  Para sinalizar que o seu projeto está pronto para o _"Code Review"_, faça o seguinte:

  - Vá até a página **DO SEU** _Pull Request_, adicione a label de _"code-review"_ e marque seus colegas:

    - No menu à direita, clique no _link_ **"Labels"** e escolha a _label_ **code-review**;

    - No menu à direita, clique no _link_ **"Assignees"** e escolha **o seu usuário**;

    - No menu à direita, clique no _link_ **"Reviewers"** e digite `students`, selecione o time `tryber/students-sd-014-b`.

  Caso tenha alguma dúvida, [aqui tem um video explicativo](https://vimeo.com/362189205).

</details>

<details>
  <summary><strong>🕵🏿 Revisando um pull request</strong></summary><br />

  Use o conteúdo sobre [Code Review](https://course.betrybe.com/real-life-engineer/code-review/) para te ajudar a revisar os _Pull Requests_.

</details>

<details>
  <summary><strong>🗣 Nos dê feedbacks sobre o projeto!</strong></summary><br />

Ao finalizar e submeter o projeto, não se esqueça de avaliar sua experiência preenchendo o formulário. 
**Leva menos de 3 minutos!**

[FORMULÁRIO DE AVALIAÇÃO DE PROJETO](https://be-trybe.typeform.com/to/ZTeR4IbH)

</details>

<details>
  <summary><strong>🗂 Compartilhe seu portfólio!</strong></summary><br />

  Você sabia que o LinkedIn é a principal rede social profissional e compartilhar o seu aprendizado lá é muito importante para quem deseja construir uma carreira de sucesso? Compartilhe esse projeto no seu LinkedIn, marque o perfil da Trybe (@trybe) e mostre para a sua rede toda a sua evolução.

</details>
