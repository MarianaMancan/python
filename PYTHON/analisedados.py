tot18 = totMasc = totMulh20 = 0

while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: [M/F]")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totMasc += 1
    if idade <= 20 and sexo == "F":
        totMulh20 += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if resp == "N":
        break
print(f"O total de pessoas maiores de idade é {tot18}")
print(f"O total de homens é {totMasc}")
print(f"O total de mulheres menores de 20 anos é {totMulh20}")
print("Acabou!")
