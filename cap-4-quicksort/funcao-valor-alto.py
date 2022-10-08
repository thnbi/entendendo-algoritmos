def max(lista):
   if len(lista) == 2:
      return lista[0] if lista[0] > lista[1] else lista[1]
   sub_max = max(lista[1:])
   return lista[0] if lista[0] > sub_max else sub_max

numeros = [2, 8, 4, 64, 32, 16]
print(max(numeros))