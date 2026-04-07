lista = []          #Lista Vazia para armazenar dados novos
producao_total = 0  #variavel do total da produção
queda_producao = 0  #variavel da queda da produção

for i in range (16):          #Loop para pedir uma certa quantidade de informações desejadas
    producao = int(input("Digite a produção da hora "))     #input para colocar dados
    lista.append (producao)           #Adiciona a informação ao final da lista

    producao_total += producao        #Ele soma na produção total que igual a produção

    media = producao_total / len(lista)        #Média da produção total
    
hora_mais_produtiva = lista[0]    #Pega os maiores valores da lista e conta como hora mais produtiva
hora_menos_produtiva = lista[0]   #Pega os menores valores da lista e conta como hora menos produtiva

for producao in lista:                  #Lista da produção, onde estão guardados os valores
    if producao > hora_mais_produtiva:  #Se a produção for maior que a hora mais produtiva, então ela é igual a produção (horário)
        hora_mais_produtiva = producao
    
    if producao < hora_menos_produtiva:  #Se a produção for menor que a hora menos produtiva, então ela é igual a produção (horário)
        hora_menos_produtiva = producao
        
for i in range(1, len(lista)):   #Esse documenta a quantidade de queda da produção dos dados informados da lista produção
    if lista[i] < lista[i - 1]:
        queda_producao += 1

print(f"A produção total foi de: {producao_total}")         #Mostra o Total de horas na produção
print(f"A média da produção é de: {media}")                #A média de horas da produção
print(f"A hora mais produtiva teve o valor de: {hora_mais_produtiva}") #Mostra o valor anotado da lista da produção da hora mais produtiva
print(f"A hora menos produtiva teve o valor de: {hora_menos_produtiva}") #Mostra o valor anotado da lista da produção da hora menos produtiva
print(f"A quantidade de quedas de produção foi de: {queda_producao}") #Mostra a quantidade de quedas na produção
