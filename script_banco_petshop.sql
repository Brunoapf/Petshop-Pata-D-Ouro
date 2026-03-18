-- TABELA DE CLIENTES
CREATE TABLE clientes (
    id_cliente SERIAL PRIMARY KEY,
    nome_cliente VARCHAR(150), -- Nome completo
    cpf_cliente VARCHAR(20) UNIQUE, -- CPF com espaço para máscara
    tel_cliente VARCHAR(20),
    email_cliente VARCHAR(100)
);

--  TABELA DE PETS
CREATE TABLE pets (
    id_pet SERIAL PRIMARY KEY,
    nome_pet VARCHAR(100),
    especie_pet VARCHAR(50),
    cor_pet VARCHAR(30),
    peso_pet DECIMAL(5,2), -- Suporta até 999.99 kg
    dono_id INTEGER REFERENCES clientes(id_cliente)
);

--  TABELA DE SERVIÇOS
CREATE TABLE servicos (
    id_servico SERIAL PRIMARY KEY,
    tipo_servico VARCHAR(100),
    valor_servico DECIMAL(10,2),
    data_hora_agenda TIMESTAMP
);

--  TABELA DE PRODUTOS
CREATE TABLE produtos (
    id_produto SERIAL PRIMARY KEY,
    nome_produto VARCHAR(100),
    categoria_produto VARCHAR(50),
    valor_produto DECIMAL(10,2)
);
