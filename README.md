# Testes Automatizados — Login (Automation Practice)

Este projeto contém testes automatizados da tela de login do site Automation Practice, criados como parte de um teste prático.

🔗 URL da página testada: http://automationpractice.pl/index.php?controller=authentication&back=my-account

📌 Tecnologias Utilizadas

- Python 3.8+
- Selenium WebDriver
- Pytest

📂 Estrutura de Diretórios
```
.
├── pages/                 # Page Object Models
│   └── login_page.py      # Página de login
├── tests/                 # Arquivos de testes
│   └── test_login.py      # Casos de teste
├── conftest.py            # Setup do Selenium WebDriver
├── requirements.txt       # Dependências do projeto
└── README.md              # Este arquivo
```

📋 Cenários de Teste (em Gherkin)

Scenario: Login com e-mail e senha válidos
  Dado que o usuário está na página de login
  Quando ele insere um e-mail válido e uma senha válida
  E clica no botão "Sign in"
  Então ele deve ser redirecionado para a página da conta pessoal

Scenario: Login com e-mail inválido
  Dado que o usuário está na página de login
  Quando ele insere um e-mail inválido e uma senha qualquer
  E clica no botão "Sign in"
  Então uma mensagem de erro deve ser exibida informando que o e-mail não é válido

Scenario: Login com campos vazios
  Dado que o usuário está na página de login
  Quando ele clica no botão "Sign in" sem preencher e-mail e senha
  Então uma mensagem de erro deve ser exibida indicando que os campos são obrigatórios

Scenario Bonus: Criação de conta com e-mail já cadastrado
  Dado que o usuário está na página de login
  Quando ele insere um e-mail já registrado no campo de criação de conta
  E clica no botão "Create an account"
  Então uma mensagem de erro deve ser exibida informando que o e-mail já está cadastrado

🧰 Instalação

1. Clone o repositório
```
git clone https://github.com/seu-usuario/automation-practice-login-tests.git
```
```
cd automation-practice-login-tests
```
2. Criação e ativação um ambiente virtual
```
python -m venv venv
```

```
source venv/bin/activate   # Linux/macOS
```

```
venv\Scripts\activate.bat  # Windows
```

3. Instalação de dependências

```
pip install -r requirements.txt
```

🚀 Execução de testes

Com o ambiente ativado, é possível executar os testes com:

```
pytest tests/test_login.py -v
```

🧪 Pré-requisitos

- Python (versão 3.8 ou superior)
- Navegador Chrome
- WebDriver do Chrome (chromedriver) compatível com sua versão do navegador, e disponível no PATH

💡 Observação

É possível adaptar os testes para Firefox ou outro navegador modificando o conftest.py.
