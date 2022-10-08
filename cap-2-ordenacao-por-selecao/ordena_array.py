#procura o menor valor em um array
def buscaMenor(arr):
   #guarda o menor valor
   menor = arr[0]
   #guarda o indíce do menor valor
   menor_indice = 0
   for i in range(1, len(arr)):
      if(arr[i] < menor):
         menor = arr[i]
         menor_indice = i
   return menor_indice

#cria array ordenado
def ordenacaoporSelecao(arr):
   novoArr = []
   for i in range(len(arr)):
      #procura o menor elemento em um array e coloca ele no novo array
      menor = buscaMenor(arr)
      novoArr.append(arr.pop(menor))
   return novoArr

print(ordenacaoporSelecao([5, 3, 6, 2, 10, 68, 16, 0, 32, 13, 18]))