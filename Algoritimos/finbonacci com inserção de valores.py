print ('-'*30)
print('Sequência de Fibonacci')
print ('-'*30)

numero = int(input('Quantos núnmeros você quer mostrar?')) # Cria o input da qtd de número a exibir da sequência

t1 = 0 # Inicia a sequência
t2 = 1

print ('-'*30)
print('{} => {}'.format(t1, t2), end='')
cont = 3 # O meu contador incia no 3 porque já tenho os 2 primeiros números
while cont <= numero:
    t3 = t1 + t2 # Aqui eu realizo a soma do 
    print(' => {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1 
print(' => FIM')
print ('~'*30)

