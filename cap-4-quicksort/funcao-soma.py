arr = [2, 4, 6]

def sum(lista):
   if lista == []:
      return 0
   return lista[0] + sum(lista[1:])

print(sum(arr))