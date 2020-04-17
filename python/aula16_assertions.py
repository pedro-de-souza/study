# Uma asserção é uma verificação de integridade que você pode ativar ou desativar quando terminar de testar o programa.
# Uma expressão é testada e, se o resultado for falso, é gerada uma exceção .
# As asserções são realizadas através do uso da declaração de asserção .

print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)

# 

temp = -10
assert (temp >= 0), "Colder than absolute zero!/Mais frio que zero absoluto!"
