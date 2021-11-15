from time import sleep

nome = str(input('Por favor informe o seu nome: '))
it = str(input('sr {} informe o que o senhor quer comprar:'.format(nome)))
v = float(input('Sr {} informe o valor da(o) {} R$'.format(nome, it)))
s = float(input('Sr {} informe o seu salário R$'.format(nome)))
finan = int(input('Sr {} quantos anos de financeamento: '.format(nome)))


c = v / (finan*12)
j = (s*30) / 100

print('sr {} para pagar um(a) {} de R${:.2f} em {} anos a prestação será de R${:.2f} por mes !'
      .format(nome, it, v, finan, c))

if c > j:
    sleep(2)
    print('EMPRESTIMO NEGADO !!')
else:
    sleep(2)
    print('EMPRESTIMO APROVADO !!')
