# O Switch é uma estrutura de controle que é utilizada para verificar múltiplas condições. Em Python, entretanto, damos outro nome: match.

# Exemplo:
cidade = input("Digite uma cidade: ")

match cidade:
  case "Vitória":
    print("Vitória é a capital do Espírito Santo")
  case "São Paulo":
    print("São Paulo é a capital de São Paulo")
  case "Rio de Janeiro":
    print("Rio de Janeiro é a capital do Rio de Janeiro")
  case "Belo Horizonte":
    print("Belo Horizonte é a capital de Minas Gerais")
  case _:
    print("Capital não encontrada")