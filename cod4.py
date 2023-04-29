ni=int(input('Digite um número: '))
sus=ni+1
ant=ni-1
print ('O número é {}, seu sucessor é {} e seu antecessor é {}'.format(ni, sus, ant))

ni=int(input('Digite um número: '))
print('O número é {}, seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.0f}'.format(ni, ni*2, ni*3, ni**(1/2)))

prod=float(input('Digite o valor do produto: '))
desc=int(input('Digite o valor do desconto: '))
vf=prod*((100-desc)/100)
print('O valor do produto com o desconto é de R${:.2f}'.format(vf))

num=float(input('Digite uma medida em metros: '))
cm=num*100
dm=num*1000
print('{} m corresponde a {:.1f} cm e {:.1f} mm'.format(num, cm, dm))