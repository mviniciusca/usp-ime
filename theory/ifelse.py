agua = 100

if agua >= 100:
    aguaFerve = True
    evaporacao = "muito rápida"
else:
    aguaFerve = False
    evaporacao = "lenta"

a = 0
b = 2
c = 1

if (a > 0):
    if (b > 0):
        print("Tudo ok para decolagem!")
    else:
        print("Tanque principal vazio; voando com combustível reserva!")
else:
    if (c > 0):
        print("Foguete não tem piloto, mas há outros foguetes disponíveis!")


idade = 18


if (idade < 18):
    print("Não pode tirar carteira de habilitação")
else:
    print("Pode tirar a carteira de habilitação")

texto = "computação"
if len(texto) > 10:
    print("texto com mais de 10 caracteres")
else:
    print("texto com 10 ou menos caracteres")
