user = open('usuarios.txt', 'r')
rel = open('relatorio.txt', 'w')
soma = 0

def convert(num):
    n = float(num)/1024
    return n

def porcentagem(num, soma):
    p = (num/soma)*100
    return p

for linha in user:
    nome, numero = linha.split()
    num = float(numero)
    soma+=num

i = 0
user.seek(0)

for linha in user:
    nome, numero = linha.split()
    num = float(numero)
    n = convert(num)
    p = porcentagem(num, soma)
    rel.write(str(i) + ' ' + nome + ' ' + str(n) + 'MB' + ' ' + str(p) + '%' + '\n')
    i+=1

media = soma/20
rel.write('\n' + 'Espaço total ocupado: ' + ' ' + str(soma) + 'MB')
rel.write('\n' + 'Espaço médio ocupado: ' + ' ' + str(media) + 'MB')

user.close()

rel.close()
