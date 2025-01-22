def cal_percentagem (votos, total):
    return (votos/ total) * 100 

total_votos=float(input('Digite o número total de eleitores: '))
votos_brancos=float(input('Digite o número de votos em branco: '))
votos_nulos= float(input('Digite o número de votos nulos: '))
votos_validos=float(input('Digite o número de votos válidos: '))

percentagem_brancos=cal_percentagem(votos_brancos, total_votos)
percentagem_nulos=cal_percentagem(votos_nulos, total_votos)
percentagem_validos=cal_percentagem(votos_validos, total_votos)
print(f' A percentagem de votos em branco é: {percentagem_brancos:.2f}%')
print(f' A percentagem de votos nulos é: {percentagem_nulos:.2f}%')
print(f' A percentagem de votos válidos é: {percentagem_validos:.2f}%')
