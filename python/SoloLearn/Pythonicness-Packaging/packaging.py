# SoloLearn/
#    LICENSE.txt
#    README.txt
#    setup.py
#    sololearn/
#       __init__.py
#       sololearn.py
#       sololearn2.py

# Embalagem

# A próxima etapa do empacotamento é escrever o arquivo setup.py .
# Ele contém as informações necessárias para montar o pacote para que ele possa ser carregado no PyPI e instalado com o pip (nome, versão etc.).
# Exemplo de um arquivo setup.py :

from distutils.core import setup

setup(
   name='SoloLearn', 
   version='0.1dev',
   packages=['sololearn',],
   license='MIT', 
   long_description=open('README.txt').read(),
)

# Por fim, instale um pacote com o python setup.py install .