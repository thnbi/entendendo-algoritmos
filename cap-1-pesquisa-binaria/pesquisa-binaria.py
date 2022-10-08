import math

def pesquisa_binaria(lista, item):

   #o menor e o maior valor da que podem ser de acordo com a sua pesquisa
   baixo = 0
   alto = len(lista) - 1

   #enquanto não tiver só um elemento
   while baixo <= alto:

      #chuta o valor do meio
      meio = math.ceil((baixo + alto) / 2)
      chute = lista[meio]

      #se o chute é o item que buscamos
      if chute == item:
         return meio
      
      #se o chute foi maior que o item
      if chute > item:
         alto = meio - 1

      #se o chute foi menor que o item
      else:
         baixo = meio + 1

   #item não existe
   return None

minha_lista = [146, 161, 193, 217, 266, 276, 460, 487, 585, 756, 842, 889, 954, 985, 1061, 1114, 1169, 1256, 1509, 1533, 1680, 1829, 1917, 1995, 2013, 2085, 2134, 2182, 2249, 2261, 2306, 2499, 2543, 2723, 2731, 3196, 3253, 3271, 3351, 3514, 3557, 3629, 3755, 3884, 3935, 4163, 4236, 4296, 4298, 4420, 4661, 4764, 4901, 4912, 4943, 5043, 5224, 5247, 5444, 5485, 5569, 5742, 5778, 5862, 6064, 6096, 6122, 6425, 6455, 6472, 6493, 6656, 6764, 6778, 6946, 7126, 7165, 7208, 7211, 7283, 7407, 7584, 7675, 7827, 7992, 8155, 8309, 8439, 8482, 9180, 9198, 9292, 9335, 9383, 9509, 9537, 9631, 9727, 9780, 9795]

print(pesquisa_binaria(minha_lista, 5043))