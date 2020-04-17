
# Módulos são partes de código que outras pessoas escreveram para executar tarefas comuns, como gerar números aleatórios, executar operações matemáticas etc.

# A maneira básica de usar um módulo é adicionar a importação module_name na parte superior do seu código e, em seguida, usar module_name .var para acessar funções e valores com o nome var no módulo.
# Por exemplo, o exemplo a seguir usa o módulo aleatório para gerar números aleatórios:

import random

for i in range(5):
   value = random.randint(1, 6)
   print(value)

# Você pode importar um módulo ou objeto com um nome diferente usando o como palavra-chave. Isso é usado principalmente quando um módulo ou objeto tem um nome longo ou confuso.

from math import sqrt as square_root
print(square_root(100))




