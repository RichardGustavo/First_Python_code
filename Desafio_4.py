Menu = """

Digite a operção desejada:

[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

  opcao = input(Menu)



  if opcao == "D":

    deposito = (float(input("Valor desejado para depósito: R$ ")))

    if deposito > 0:

      saldo += deposito
      print("Depósito realizado com sucesso!")
      extrato += (f"\nDepósito: R$ {deposito:.2f}")

    else:

      print("Opção inválida. Digite uma opção válida!")



  elif opcao == "S":

    sacar = (float(input("Valor desejado para saque: R$ ")))

    #Verificações para saque
    #Aqui cria-se variáveis para o saque, note que essas variáveis serão utilizadas somente para o saque.

    excedeu_saldo = sacar > saldo
    excedeu_limite = sacar > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:

      print("Saldo insuficiente.")

    elif excedeu_limite:

      print ("Limite para saque excedido.")

    elif excedeu_saques:

      print("Quantidade de saques excedido.")

    elif sacar > 0:

      saldo -= sacar
      print("Saque realizado com sucesso.")
      extrato += (f"\nSaque: R$ {sacar:.2f}")
      numero_saques += 1

    else:

      print("Valor inválido, tente novamente.")      



  elif opcao == "E":

    deposito = saldo

    EXTRATO, fim = "EXTRATO", "FIM"

    print(EXTRATO.center(30, "="))
    print("Você não realizou transações no momento." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print(fim.center(30, "="))



  elif opcao == "Q":

    break

  else:

    print("Opção inválida, escolha uma opção válida.")


# Essa porra desse código me deu uma dor de cabeça, o código está rodando limpo, então NÃO MEXA EM NADA NESSA COISA!!!
# Mensagem para o futuro Richard aí.