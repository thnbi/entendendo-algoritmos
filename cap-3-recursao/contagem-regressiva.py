def regressiva(i):
   print(i)
   if i <= 0:
      return
   else:
      regressiva(i - 1)

regressiva(10)