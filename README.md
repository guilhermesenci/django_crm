# django_crm
# LiderDeSi

## Descrição

LiderDeSi é um projeto desenvolvido com Django para gerenciamento de clientes, leads e perfis de usuários.

## Requisitos

- Python 3.12.4
- Django 5.0.7
- Um ambiente virtual Python (recomendado)

## Instalação

### Backend

1. Clone o repositório:
    ```bash
    git clone https://github.com/guilhermesenci/liderDeSi.git
    cd liderDeSi
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv liderDeSi_env
    source liderDeSi_env/bin/activate # No Windows use `liderDeSi_env\Scripts\activate`
    ```

3. Instale as dependências do backend:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute as migrações do banco de dados:
    ```bash
    python manage.py migrate
    ```

5. Crie um superusuário:
    ```bash
    python manage.py createsuperuser
    ```

6. Inicie o servidor de desenvolvimento:
    ```bash
    python manage.py runserver
    ```

### Frontend

2. Inicie o servidor de desenvolvimento do frontend:
    ```bash
    npm run dev
    ```

## Estrutura do Projeto

liderDeSi/
│ ├── liderDeSi/
│ │ ├── client/
│ │ ├── core/
│ │ ├── dashboard/
│ │ ├── lead/
│ │ ├── liderDeSi/
│ │ ├── misc/
│ │ ├── userprofile/
├── .gitignore
├── README.md
└── Scripts

## Prints Screens

  ![dashboard](./misc/Captura%20de%20tela%202024-07-24%20172029.png)
  ![leads list with no leads](./misc/Captura%20de%20tela%202024-07-24%20172053.png)
  ![Add a lead](./misc/Captura%20de%20tela%202024-07-24%20172028.png)
  ![lead list](./misc/Captura%20de%20tela%202024-07-24%20172137.png)
  ![lead details](./misc/Captura%20de%20tela%202024-07-24%20172147.png)
  ![lead deleted](./misc/Captura%20de%20tela%202024-07-24%20172208.png)
  ![lead edited msg](./misc/Captura%20de%20tela%202024-07-24%20172245.png)
  ![client](./misc/Captura%20de%20tela%202024-07-24%20172259.png)
  ![home](./misc/Captura%20de%20tela%202024-07-24%20172309.png)
  ![login](./misc/Captura%20de%20tela%202024-07-24%20172321.png)
  ![sign in](./misc/Captura%20de%20tela%202024-07-24%20172350.png)

## Uso extra

Acesse o painel administrativo do Django em `http://127.0.0.1:8000/admin/` e faça login com as credenciais do superusuário criado.
