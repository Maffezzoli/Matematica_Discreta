def mostra(f_valor,calcula,n): #função que facilita a reutilização de linhas de códigos comuns
    f_valor.append(calcula)
    print(f_valor[n])

def primeiro_slide():
    f_valor = [3]
    n = 1
    while n <= 15:
        calcula = 2*f_valor[n- 1] + 3
        mostra(f_valor,calcula,n)
        n += 1
primeiro_slide()

def segundo_slide():
    f_valor = [1]
    n = 1
    while n <= 10:
        calcula = 10 * f_valor[n - 1]
        mostra(f_valor,calcula,n)
        n +=1
segundo_slide()

def quarto_slide():
    f_valor = [1,1]
    n = 2
    while n <= 20:
        calcula = f_valor[n - 1] + f_valor[n - 2]
        mostra(f_valor,calcula,n)
        n += 1

quarto_slide()

def somatorio():
    soma = 0
    n = 1
    lista = [0]
    while n < 10:
        calcula = 2 * n + 1
        lista.append(calcula)
        n += 1
    for num in lista:
        soma += num
    print(lista)
    print("Soma: ",soma)
somatorio()

def produtorio():
    produto = 1
    n = 1 
    lista = [1]
    while n < 5:
        calcula = 2 * n + 1
        lista.append(calcula)
        n += 1
    for num in lista:
        produto *= num
    print(lista)
    print("Produto: ",produto)
produtorio()