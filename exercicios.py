import math



class Exercicios:
    def __init__(self):
        self.num = 0
        self.num1 = 0
        self.num2 = 0

    def coletar(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def coletarr(self, num):
        self.num = num

    def somar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 + self.num2

    def subtrair(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 - self.num2

    def multiplicar(self, num1, num2):
        self.coletar(num1, num2)
        return self.num1 * self.num2

    def dividir(self, num1, num2):
        self.coletar(num1, num2)
        if self.num2 <= 0:
            return "impossivel dividir"
        else:
            return self.num1 / self.num2

    def tabuada(self, num1):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{num1} * {i} = {num1 * i}'
        return resultado

    def potencia(self, base, expoente):
        return pow(base, expoente)

    def raiz(self, num1):
        return math.sqrt(num1)

    def exercicio01(self):
        resultado = ""
        for i in range(1, 10, 11):
            resultado += f'\n{i}'
        return resultado

    def exercicio02(self):
        pares = ""
        for i in range(1, 21, 1):
            if i % 2 == 0:
                pares += f'\n{i}'
        return pares

    def exercicio03(self):
        resultado = 0
        for i in range(1, 101):
            resultado += i
        return resultado

    def exercicio04(self):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{5} * {i} = {5 * i}'
        return resultado

    def exercicio05(self, num):
        self.coletarr(num)
        if num % 2 == 0:
            return "par"
        else:
            return "impar"

    def exercicio06(self, num):
        resultado = ""
        self.coletarr(num)
        if num < 0:
            return "numero negativo"
        elif num > 0:
            return "numero positivo"
        else:
            return "numero zero"

    def exercicio07(self, num):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'\n{num} * {i} = {num * i}'
        return resultado

    def exercicio08(self, num):
        self.coletarr(num)
        for i in range(1, num + 1):
            print(i)

    def exercicio09(self, num):
        resultado = ""
        self.coletarr(num)
        for i in range(1, num + 1):
            resultado += f'\n{num} + {i} = {num + i}'
        return resultado

    def exercicio10(self):
        primo = "1\n2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                primo += f'\n{i}'
        return primo

    def exercicio11(self, num):
        if num == 2 or num == 3 or num == 5:
            return f'O {num} é primo!'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
            return f'O {num} é primo'
        return f'O {num} não é primo'

    def exercicio12(self, num):
        fatorial = 1
        self.coletarr(num)
        for i in range(1, num + 1):
            fatorial *= i
        return fatorial

    def exercicio13(self):
        resultado = ""
        n1 = 0
        n2 = 1
        conta = 10
        while conta != 0:
            n3 = n1 + n2
            print(n3)
            n1 = n2
            n2 = n3
            conta = conta - 1

    def exercicio14(self, num):
        resultado = ""
        n1 = 0
        n2 = 1
        conta = 10
        self.coletarr(num)
        while conta != 0:
            n3 = n1 + n2
            print(n3)
            n1 = n2
            n2 = n3
            conta = conta - 1

    def exercicio15(self, num):
        soma = ""
        resultado = ""
        n = num
        self.coletarr(num)
        while (n > 0):
            resultado = n % 10
            n = (n - resultado) / 10
            soma += resultado
        return soma


    def exercicio16(self):
        numero = int(input("Digite um número: "))

        if numero <= 0:
            print("Por favor, digite um número maior que 0.")
        else:
            #
            print("Números pares de 1 até", numero, ":")
            for i in range(1, numero + 1):
                if i % 2 == 0:
                    print(i, end=' ')

            print()

            print("Números ímpares de 1 até", numero, ":")
            for i in range(1, numero + 1):
                if i % 2 != 0:
                    print(i, end=' ')

            print()



    def exercicio17(self):
        def eh_primo(num):

            if num <= 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            i = 3
            while i * i <= num:
                if num % i == 0:
                    return False
                i += 2
            return True

        numero = int(input("Digite um número: "))

        if numero <= 1:
            print("Não há números primos menores que 2.")
        else:
            print("Números primos de 1 até", numero, ":")
            for i in range(2, numero + 1):
                if eh_primo(i):
                    print(i, end=' ')
            print()

    def exercicio18(self, num):
        for i in range(1, num):
            if 0 == 2:
                return 0
            elif i % 2 == 0:
                print(1 + i // 2)
            else:
                print(1 + (3 * i + 1))


    def exercicio19(self, num):
        somapar = 0
        somaimpar = 0
        for i in range(1, num + 1, 1):
            if i % 2 == 0:
                somapar += i
            else:
                somaimpar += i
        return f'a soma dos pares é {somapar} e a dos ímpares é {somaimpar}.'

    def exercicio20(self,num):
        soma_divisores = 0

        for i in range(1, num):
            if num % i == 0:
                soma_divisores += i

        if soma_divisores == num:
            print(f"{num} é um número perfeito!")
        else:
            print(f"{num} não é um número perfeito.")

    def exercicio21(self, num1, num2):
        num1 = 10
        num2 = 20
        return num1 + 10, num2 - 10

    def exercicio22(self, num):
        resultado = ""

        resultado += f'\n {num - 1}'
        print("o antecessor é:")
        return resultado

    def exercicio23(self, base,altura):
        return base * altura

    def exercicio24(self, anos,meses,dias):
        resultado = anos * 365 + meses * 30 + dias
        return resultado

    def exercicio25(self, num):

        totaleleitores = int(input("Digite o total de eleitores: "))
        votosbrancos = int(input("Digite o número de votos brancos: "))
        votosnulos = int(input("Digite o número de votos nulos: "))
        votosvalidos = int(input("Digite o número de votos válidos: "))

        if totaleleitores > 0:
            percentualbrancos = (votosbrancos / totaleleitores) * 100
            percentualnulos = (votosnulos / totaleleitores) * 100
            percentualvalidos = (votosvalidos / totaleleitores) * 100

            print(f"Percentual de votos brancos: {percentualbrancos:.2f}%")
            print(f"Percentual de votos nulos: {percentualnulos:.2f}%")
            print(f"Percentual de votos válidos: {percentualvalidos:.2f}%")
        else:
            print("O total de eleitores deve ser maior que zero.")

    def exercicio26(self, mensal, porcentual):
        novo = ""
        novo = (porcentual / 100) * mensal + mensal
        return novo

    def exercicio27(self, num):
        valfab = num
        pd = valfab * 0.28
        i = valfab * 0.45
        vt = valfab + pd + i
        return f'O custo final ao consumidor é: {vt}'

    def exercicio28(self,nota1, nota2, nota3):
        media = ""
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7:
            return "Você passou na média"
        else:
            print("De recuperação!")

    def exercicio29(self, macas):
        if macas < 12:
            return macas * 1.30
        else:
            return macas * 1
    print("o valor total de maças é:")

    def exercicio30(self, num):
        maior = ""
        for i in range(1, 11, 1):
            num = int(input("Informe um número: "))
            if i == 1:
                maior = num
            if num > maior:
                maior = num

    def exercicios31(self, salarioF, vendas):
        if vendas < 1500:
            return ((vendas * 0.03) + salarioF)
        else:
            return ((vendas * 0.05) + salarioF)

    def exercicio32(self):
        numconta = int(input("Digite o número da conta do cliente: "))
        saldo = float(input("Digite o saldo: "))
        debito = float(input("Digite o valor do débito: "))
        credito = float(input("Digite o valor do crédito: "))

        saldo_atual = saldo - debito + credito

        print(f"O saldo atual é: {saldo_atual:.2f}")
        if saldo_atual >= 0:
            print("Saldo Positivo")
        else:
            print("Saldo Negativo")

    def exercicio33(self, num):
        resultado = ""
        if num > 10:
            return "Não é possível fazer cálculo"
        else:
            for i in range(1, 11, 1):
                resultado += f'\n{num} * {i} = {num * i}'
            return resultado







































