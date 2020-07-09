

def escrever_arquivo(texto):
    arquivo = open('arq.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo = open('arq.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_nota():
    arquivo =  open('arq.txt', 'r')
    aluno_nota  = arquivo.read()
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_not = x.split(',')
        nome_aluno = lista_not[0]
        lista_not.pop(0)
        media = lambda notas: sum([int(i)for i in notas])/len(lista_not)
        print(f'{nome_aluno} média: {media(lista_not)}')

import shutil
def copiar_arquivo():
    shutil.copy('Nome do arquivo', 'Pra onde vai')
def mover_arquivo():
    shutil.move('Nome do arquivo', 'Pra onde vai')

if __name__ == '__main__':
    escrever_arquivo('Pedro, 5,6,9,9')
    atualizar_arquivo('\nZuckerberg, 9,6,7,5')
    atualizar_arquivo('\nDamião, 8,6,8,7')
    # ler_arquivo('arq.txt')
    media_nota()