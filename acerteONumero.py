from random import randint

print("\nBem-vindo ao Acerte o Número")
print("\nNeste jogo, o próprio sistema criará um número aleatório e você precisará acertar")
print("\nObservação: você terá 3 chances de acertar o número, que vão de 1 à 100. Além disso, poderá reiniciar quando quiser")
    
iniciar = input("\nPodemos iniciar o jogo (s/n): ")
while (iniciar == 's'):
    # Criação do número aleatório
    num = randint(1, 100)
    tentativas = 1 # tentativas do jogo - contador
    print("\nJogo iniciado e número aleatório criado")
    while (tentativas <= 3):
        num_user = int(input("\nInforme o número: "))
        if (num_user == num):
            print("\nMuito bem, você acertou!")
            break
        else:
            print("Número incorreto, tente novamente")
            tentativas = tentativas + 1
    print("\nJogo encerrado!")
    print("O número criado foi: ", num)
    iniciar = input("\nDeseja jogar novamente (s/n): ")