SELECT column_list FROM table_nameWHERE condition;

SELECT column_name(s)FROM table_name WHERE column_name BETWEEN value1 AND value2; -- BETWEEN seleciona valores dentro de um intervalo

SELECT ID, FirstName, LastName FROM customers WHERE Age >= 30 AND Age <= 40;

SELECT * FROM customers WHERE City = 'New York' AND (Age=30 OR Age=35);

SELECT * FROM customers WHERE City = 'New York' OR City = 'Los Angeles' OR City = 'Chicago';

SELECT * FROM customers WHERE City IN ('New York', 'Los Angeles', 'Chicago');

SELECT * FROM customers WHERE City NOT IN ('New York', 'Los Angeles', 'Chicago');

SELECT CONCAT(FirstName,', ', City) AS new_column FROM customers;

SELECT FirstName, UPPER(LastName) AS LastName FROM employees; 
-- A função UPPER converte todas as letras da string especificada em maiúsculas. A função LOWER converte a string em minúsculas.

SELECT Salary, SQRT (Salary) FROM funcionários; --A função SQRT retorna a raiz quadrada de um determinado valor no argumento.

SELECT Salary, AVG (Salary) FROM funcionários; -- a função AVG retorna o valor médio de uma coluna numérica:

SELECT  SUM (Salary) FROM funcionários; 

SELECT  MIN (salário) como salário dos funcionários;

SELECT  MAX (salário) como salário dos funcionários; 

SELECT nome_da_coluna FROM nome_tabela WHERE nome_da_coluna LIKE pattern ; 

SELECT * FROM employee WHERE FirstName LIKE 'A%' ;


--  Uma subconsulta é uma consulta dentro de outra consulta.
-- Vamos considerar um exemplo. Podemos precisar da lista de todos os funcionários cujos salários são maiores que a média.
-- SELECT AVG(Salary) FROM employees;
-- Como já sabemos a média, podemos usar um simples WHERE para listar os salários que são maiores que esse número.
SELECT FirstName, Salary FROM employees WHERE  Salary > (SELECT AVG(Salary) FROM employees) ORDER BY Salary DESC;

SELECT ct.ID, ct.Name, ord.Name, ord.Amount FROM customers AS ct, orders AS ord WHERE ct.ID=ord.Customer_ID ORDER BY ct.ID;

SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name=table2.column_name;

SELECT customers.Name, items.Name FROM customers LEFT OUTER JOIN items ON customers.ID=items.Seller_id;

SELECT customers.Name, items.Name FROM customers RIGHT OUTER JOIN items ON customers.ID=items.Seller_id;

-- O operador UNION é usado para combinar os conjuntos de resultados de duas ou mais instruções SELECT .
SELECT nome_da_coluna FROM tabela1 UNION SELECT nome_da_coluna FROM tabela2; 

-- UNION ALL seleciona todas as linhas de cada tabela e as combina em uma única tabela.
SELECT ID, Nome, Sobrenome, Cidade FROM First UNION ALL SELECT ID, Nome, Sobrenome, Cidade FROM Second; 

INSERT INTO nome_tabela VALUES (valor1, valor2, valor3, ...); 

INSERT INTO table_name (coluna1, coluna2, coluna3, ..., colunaN)  VALUES (valor1, valor2, valor3, ... valorN); 

UPDATE  nome_tabela SET coluna1 = valor1, coluna2 = valor2, ... WHERE condição; 

DELETE FROM table_name WHERE condição; 

CREATE TABLE table_name
(
    column_name1 data_type(size),
    column_name2 data_type(size),
    column_name3 data_type(size),
    ....
    columnN data_type(size)
);

/*
    A seguir, são comumente usadas restrições SQL:
NOT NULL - indica que uma coluna não pode conter nenhum valor NULL .
UNIQUE  - Não permite inserir um valor duplicado em uma coluna. A restrição UNIQUE mantém a exclusividade de uma coluna em uma tabela. Mais de uma coluna UNIQUE pode ser usada em uma tabela.
PRIMARY KEY - Força a tabela a aceitar dados exclusivos para uma coluna específica e essa restrição cria um índice exclusivo para acessar a tabela mais rapidamente.
CHECK - Determina se o valor é válido ou não de uma expressão lógica.
DEFAULT - Ao inserir dados em uma tabela, se nenhum valor for fornecido a uma coluna, a coluna obterá o valor definido como PADRÃO.
*/

ALTER TABLE People ADD DateOfBirth date;
ALTER TABLE People CHANGE FirstName name varchar(100);

RENAME TABLE People TO Users;

DROP TABLE People;

CREATE VIEW view_name AS SELECT column_name(s) FROM table_name WHERE condition;