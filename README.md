# 🐾 Petshop Pata D'Ouro



## 🛠️ Tecnologias
- **Python & Django** (Lógica e Painel Admin)
- **PostgreSQL** (Banco de Dados Relacional)
- **DBeaver** (Gestão visual dos dados)

## ✅ Status Atual
- Banco de dados PostgreSQL configurado.
- Tabelas criadas: Clientes, Pets, Serviços e Agendamentos.
- Relacionamentos entre os dados funcionando perfeitamente.
- Painel Administrativo ativo para testes de fluxo.

## 🚀 Como rodar
1. Clone o repositório e ative o ambiente virtual (`venv`).
2. Instale as dependências: `pip install -r requirements.txt`.
3. Ajuste a senha do PostgreSQL no arquivo `settings.py`.
4. Rode as migrações: `python manage.py migrate`.
5. Inicie o servidor: `python manage.py runserver`.