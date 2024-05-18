def calcular(n1, n2, op):
  if op == "+":
    return n1 + n2
  elif op == "-":
    return n1 - n2
  if op == "*":
    return n1 * n2
  elif op == "/":
    return n1 / n2
    if n2 != 0:
      return n1 / n2
    else:
      return "Erro: Divisão por zero"
  else:
    return "Operarador Invalido"
  
def main():
    numero1 = float(input("digite o numero"))              
    numero2 = float(input("digite o numero"))
    operador = input()
    resultado = calcular(numero1,numero2, operador)
    print(resultado)

main()
