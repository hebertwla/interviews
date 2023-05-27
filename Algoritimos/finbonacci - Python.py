def fibonacci():
    primeiro = 0  # Inicializa a variável primeiro com o valor 0
    segundo = 1  # Inicializa a variável segundo com o valor 1
    print(primeiro)  # Imprime o valor de primeiro (0)
    print(segundo)  # Imprime o valor de segundo (1)

    for _ in range(8):  # Loop que se repete 8 vezes
        proximo = primeiro + segundo  # Calcula o próximo número da sequência somando os dois últimos
        print(proximo)  # Imprime o valor do próximo número
        primeiro = segundo  # Atualiza o valor de primeiro com o valor de segundo
        segundo = proximo  # Atualiza o valor de segundo com o valor do próximo número

fibonacci()  # Chama a função fibonacci