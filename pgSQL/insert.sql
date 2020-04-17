INSERT (campos da tabela) values (valores);
INSERT (campos da tabela) select (valores);

INSERT INTO tabela (campos da tabela) values (0);

INSERT INTO tabela (campos da tabela) SELECT (0)
  where not exists (SELECT * from tabela where campo = 0);

INSERT INTO tabela(campos da tabela) values (valores) 
  on conflict (primarekey) do nothing; 