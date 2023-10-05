#funcao de converter dec para binario baseado no algoritimo de Laires
def dectobin(dec):
    bin = ""
    while dec > 0:
        bin = bin + str(dec % 2)
        dec = dec // 2
    return(bin)

#algoritmo para dividir a string do binario em uma lista e reverte-la
def binsum (bin):
    splitedbin = ([*bin])[::-1] 
    count = 1
    sum = 0

    for i in range (0, (len(splitedbin))):
        if (splitedbin[i] == "1"):
            sum = sum + count
        count = count + count
    return(sum)

#loop para a interface no terminal
while True:
    print('Conversor e soma de binário.\nSelecione uma opção.\n[1] Converter binário para decimal.\n[2] Somar dois binários.')
    print('[3] Converter decimal para binário.\n[4] Sair.')
    choice = int(input(''))
    if (choice == 4):
        break
    if (choice == 3):
        decchoice = int(input('Digite o número decimal:\n>>'))
        print(str(dectobin(decchoice))[::-1])
        input('Pressione Enter para continuar.')
    if (choice == 1):
        binchoice = (input('Digite o binário: >>'))
        try:
            binchoice = int(binchoice)
        except ValueError:
            print('Número binário inválido.')
            input('Pressione enter para voltar.')
            continue
        binchoice = str(binchoice)
        print(binsum(binchoice))
        input('Pressione Enter para continuar.')
        
    if (choice == 2):
        sumbinchoice1 = (input('Digite o primeiro binário: >>\n'))
        sumbinchoice2 = (input('Digite o segundo binário: >>\n'))
        num1 = binsum(sumbinchoice1)
        num2 = binsum(sumbinchoice2)
        print(f'Resultado em decimal: {num1 + num2}')
        print(f'Resultado em binário: {(dectobin(num1 + num2))[::-1]}')
        input('Pressione Enter para continuar.')
