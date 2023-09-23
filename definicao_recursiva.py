def mostra(f_valor,calcula,n): #função que facilita a reutilização de linhas de códigos comuns
    f_valor.append(calcula)
    print(f_valor[n])

def primeiro_slide():
    f = [0]
    f_valor = [3]
    n = 1
    while n <= 15:
        f.append(n)
        calcula = 2*f_valor[f[n] - 1] + 3
        mostra(f_valor,calcula,n)
        n += 1
#primeiro_slide()

def segundo_slide():
    f = [0]
    f_valor = [1]
    n = 1
    while n <= 10:
        f.append(n)
        calcula = 10 * f_valor[f[n] - 1]
        mostra(f_valor,calcula,n)
        n +=1
#segundo_slide()

def quarto_slide():
    f = [0,1]
    f_valor = [1,1]
    n = 2
    while n <= 20:
        f.append(n)
        calcula = f_valor[f[n] - 1] + f_valor[f[n] - 2]
        mostra(f_valor,calcula,n)
        n += 1

quarto_slide()