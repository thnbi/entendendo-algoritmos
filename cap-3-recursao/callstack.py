def sauda(nome):
   print("Olá, {}!".format(nome))
   sauda2(nome)
   print("preparando para dizer tchau...")
   tchau()

def sauda2(nome):
   print("Como vai {}?".format(nome))

def tchau():
   print("ok, tchau!")

sauda("jordanna")