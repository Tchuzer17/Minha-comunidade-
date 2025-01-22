idade= float(input('Digite a idade do atleta: '))
if(idade>18):
    print(f'Categoria Senior')
elif(5<=idade<=7):
    print(f'Categoria Infantil')
elif(8<=idade<=10): 
     print(f'Categoria Iniciado')
elif(11<=idade<=13):
     print(f'Categoria Juvenil')
elif(14<=idade<=17):
     print(f'Categoria Junior')
elif(idade<5):
     print(f'Naõ tem idade suficiente para ser atleta, necessita de ter pelo menos 5 anos ou mais para competir')