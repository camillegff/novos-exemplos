print("este é um programa que verifica se um número é maior que outro")
numero1 = int(input("digite o primeiro numero"))
numero2 = int(input("digite o segundo numero"))
if numero1.isdigit() and numero2.isdigit():
    if numero1 > numero2:
     print("o numero: ",numero1," é maior que o numero", numero2)
elif numero1 == numero2:
    print("o numero: ",numero1, " é igual ao ",numero2)
elif numero1 < numero2:
    print("o numero: ",numero1," é menor que o numero: ",numero2)
else:
   print("voce digitou uma letra")