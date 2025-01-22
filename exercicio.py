while True:  
    blocos = int(input("Digite o número de blocos: "))  
    altura = 0  
    blocos_camadas = 1  

    while blocos >= blocos_camadas:  
        blocos -= blocos_camadas  # Aqui remove os blocos usados para a camada atual  
        altura += 1               # Aqui aumenta a altura porque uma camada completa foi construída  
        blocos_camadas += 1       # Aqui passa para a próxima camada que requer mais blocos  

    print("A altura da pirâmide:", altura)  

    # Usei essa parte para dar mais estrutura na aplicação, aqui pergunta ao usuário se deseja repetir ou sair  
    continuar = input(" Deseja calcular a altura de outra pirâmide? (s/n): ").lower()  
    if continuar != 's':  
        print("Saindo da aplicação.")  
        break
    
    # By: José da Silva