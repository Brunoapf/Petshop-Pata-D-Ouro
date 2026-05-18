# 🐾 Pata D’Ouro — Sistema de Gestão para Petshop

## 📌 Sobre o Projeto

O **Pata D’Ouro** é um sistema web desenvolvido com o objetivo de auxiliar no gerenciamento administrativo e operacional de um petshop, proporcionando maior organização, praticidade e eficiência nos processos internos.

O sistema permite controlar informações relacionadas a clientes, pets, serviços e agendamentos, facilitando o acompanhamento dos atendimentos realizados no estabelecimento.

Este projeto foi desenvolvido como parte do **Projeto Extensionista 2**.

---

# 👥 Equipe de Desenvolvimento

- Bruno De Araújo
- Alyere Targino
- Diogo Everton
- Fernando Neto
- João Victor
- Alyssa Hruby
- Marcelo Gomes
- Kaike Araújo
- Victor Gadelha
- Gabriele Gonçalves

---

# 🎯 Objetivo do Sistema

O sistema foi criado para oferecer uma solução de gerenciamento para petshops, permitindo:

- organização de clientes;
- gerenciamento de pets;
- controle de serviços;
- agendamento de atendimentos;
- atualização de informações;
- visualização de atendimentos diários;
- consulta rápida de dados.

A proposta do projeto é otimizar o fluxo de atendimento e melhorar a organização interna do estabelecimento.

---

# 🚀 Tecnologias Utilizadas

| Tecnologia | Finalidade |
|---|---|
| Python | Linguagem principal |
| Django | Framework web |
| PostgreSQL | Banco de dados |
| HTML5 | Estrutura das páginas |
| CSS3 | Estilização |
| Django ORM | Manipulação do banco |
| Django Authentication | Sistema de autenticação |

---

# 🗂️ Funcionalidades Principais

## 👤 Gerenciamento de Clientes

- cadastro de clientes;
- edição de informações;
- visualização de registros;
- remoção de clientes.

---

## 🐶 Gerenciamento de Pets

- cadastro de pets;
- vínculo com clientes;
- atualização de dados;
- exclusão de registros.

---

## 🛁 Gerenciamento de Serviços

- cadastro de serviços;
- atualização de informações;
- gerenciamento de serviços oferecidos;
- remoção de serviços.

---

## 📅 Controle de Agendamentos

- criação de agendamentos;
- edição de atendimentos;
- cancelamento de agendamentos;
- visualização dos serviços marcados.

---

## 📊 Visualização de Atendimentos

- consulta organizada dos atendimentos do dia;
- acompanhamento dos serviços agendados.

---

## 🔐 Sistema de Autenticação

- login seguro de usuários;
- proteção das funcionalidades administrativas;
- controle de acesso ao sistema.

---

# 🏗️ Estrutura do Projeto
# 🏗️ Estrutura do Projeto

```bash
PROJETO PATADOURO/
│
├── core/
│   │
│   ├── migrations/
│   │
│   ├── templates/
│   │   ├── agendamentos/
│   │   │   ├── deletar.html
│   │   │   ├── form.html
│   │   │   └── listar.html
│   │   │
│   │   ├── pets/
│   │   ├── servicos/
│   │   └── base.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── patadouro/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── templates/
│
├── venv/
│
├── .gitignore
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

---

## 📂 Organização das Pastas

| Pasta/Arquivo | Função |
|---|---|
| `core/` | Aplicação principal do sistema |
| `migrations/` | Controle das migrações do banco de dados |
| `templates/` | Arquivos HTML utilizados nas páginas |
| `agendamentos/` | Templates relacionados aos agendamentos |
| `pets/` | Templates relacionados ao gerenciamento de pets |
| `servicos/` | Templates relacionados aos serviços |
| `admin.py` | Configuração do painel administrativo |
| `forms.py` | Formulários Django utilizados no sistema |
| `models.py` | Modelos e estrutura do banco de dados |
| `views.py` | Regras de negócio e controle das páginas |
| `urls.py` | Rotas da aplicação |
| `settings.py` | Configurações principais do Django |
| `manage.py` | Arquivo principal de gerenciamento do projeto |
| `requirements.txt` | Dependências utilizadas no projeto |
| `db.sqlite3` | Banco de dados SQLite utilizado no desenvolvimento |


---

# ⚙️ Como Executar o Projeto

## 1️⃣ Clone o Repositório

```bash
git clone https://github.com/Brunoapf/Petshop-Pata-D-Ouro.git
```

---

## 2️⃣ Acesse a Pasta do Projeto

```bash
cd Petshop-Pata-D-Ouro
```

---

## 3️⃣ Crie um Ambiente Virtual

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Configure o Banco de Dados

Configure as informações do PostgreSQL no arquivo `.env` ou diretamente no `settings.py`.

Exemplo:

```env
DB_NAME=petshop
DB_USER=postgres
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
```

---

## 6️⃣ Execute as Migrações

```bash
python manage.py migrate
```

---

## 7️⃣ Crie um Superusuário

```bash
python manage.py createsuperuser
```

---

## 8️⃣ Inicie o Servidor

```bash
python manage.py runserver
```

---

# 🌐 Acesso ao Sistema

| Página | URL |
|---|---|
| Sistema | http://127.0.0.1:8000 |
| Admin Django | http://127.0.0.1:8000/admin |

---

# 🛡️ Segurança e Controle de Dados

O sistema possui mecanismos de autenticação e organização de dados para garantir:

- integridade das informações;
- controle de acesso;
- segurança dos registros;
- organização dos atendimentos.

---

# 📈 Benefícios do Sistema

- maior organização interna;
- otimização do fluxo de atendimento;
- facilidade no gerenciamento;
- centralização das informações;
- praticidade no acompanhamento dos serviços.

---

# 📚 Aprendizados do Projeto

Durante o desenvolvimento foram aplicados conhecimentos relacionados a:

- desenvolvimento web com Django;
- modelagem de banco de dados;
- autenticação de usuários;
- organização de projetos backend;
- operações CRUD;
- integração com PostgreSQL;
- gerenciamento de rotas e templates.

---

# 📄 Licença

Este projeto possui finalidade acadêmica e educacional.

---

# ✨ Desenvolvido por

Equipe do projeto **Pata D’Ouro — Sistema de Gestão para Petshop**
