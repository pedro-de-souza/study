CREATE DATABASE conta;

CREATE TABLE IF NOT EXISTS banco(
  numero INTEGER NOT NULL,
  nome VARCHAR(50) NOT NULL,
  ativo BOOLEAN NOT NULL DEFAULT TRUE,
  data_criacao TIMESTAMP NOT NULL DEFAULT, -- Valor  de tempo real
  PRIMARY KEY(numero)
);

CREATE TABLE IF NOT EXISTS agencia(
  banco_numero INTEGER NOT NULL,
  nomero INTEGER NOT NULL,
  nome VARCHAR(50) NOT NULL,
  ativo BOOLEAN NOT NULL DEFAULT TRUE,
  data_criacao TIMESTAMP NOT NULL DEFAULT,
  PRIMARY KEY(banco_numero,numero),
  FOREIGN KEY (banco_numero) REFERENCES banco(numero)
);

CREATE TABLE cliente(
  nomero BIGSERIAL PRIMARY KEY, -- BIGINT
  nome VARCHAR(55) NOT NULL,
  email VARCHAR(100) NOT NULL DEFAULT TRUE,
  ativo BOOLEAN NOT NULL DEFAULT TRUE,
  data_criacao TIMESTAMP NOT NULL DEFAULT,
);

CREATE TABLE conta_corrente(
  banco_nomero INTEGER NOT NULL,
  agencia_nomero INTEGER NOT NULL,
  nomero BIGINT NOT NULL,
  digito SMALLINT NOT NULL,
  cliente_numero BIGINT NOT NULL,
  ativo BOOLEAN NOT NULL DEFAULT TRUE,
  data_criacao TIMESTAMP NOT NULL DEFAULT,
  PRIMARY KEY(banco_numero,agencia_nomero,numero,digitocliente_numero),
  FOREIGN KEY (banco_numero,agencia_nomero) REFERENCES agencia(banco_numero,numero),
  FOREIGN KEY (cliente_numero) REFERENCES cliente(numero)
);

CREATE TABLE tipo_transacao(
  id SMALLSERIAL PRIMARY KEY,
  nome VARCHAR(50) NOT NULL,
  ativo BOOLEAN NOT NULL DEFAULT TRUE,
  data_criacao TIMESTAMP NOT NULL DEFAULT
 );

CREATE TABLE cliente_transacao(
  id BIGSERIAL PRIMARY KEY,
  banco_nomero INTEGER NOT NULL,
  agencia_nomero INTEGER NOT NULL,
  conta_corrente_numero BIGINT NOT NULL,
  conta_corrente_digito SMALLINT NOT NULL
  cliente_numero BIGINT NOT NULL,
  tipo_transacao_id SMALLINT NOT NULL,
  valor NUMERIC(15,2) NOT NULL,
  data_criacao TIMESTAMP NOT NULL DEFAULT,
  FOREIGN KEY(banco_nomero,agencia_nomero,conta_corrente_numero,conta_corrente_digito,cliente_numero) REFERENCES conta_corrente(banco_numero,agencia_nomero,numero,digito,cliente_numero) 
 );

-- https://github.com/drobcosta/digital_innovation_one