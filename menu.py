from exercicios import Exercicios


class Menu:
    def __init__(self):
        self.opcao = -1
        self.exer = Exercicios()
        self.num = 0
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0

    def mostrarMenu(self):
        print('\n----MENU----\n\n'
              'Escolha uma das opções abaixo: '
              '\n0.Sair' +
              '\n1.Somar' +
              '\n2.Subtrair' +
              '\n3.Dividir' +
              '\n4.Mutiplicar' +
              '\n5.Pontencia' +
              '\n6.Raiz' +
              '\n7.Tabuada' +
              '\n8.exercicio01' +
              '\n9.exercicio02' +
              '\n10.exercicio03' +
              '\n11.exercicio04' +
              '\n12.exercicio05' +
              '\n13.exercicio06' +
              '\n14.exercicio07' +
              '\n15.exercicio08' +
              '\n16.exercicio09' +
              '\n17.exercicio10' +
              '\n18.exercicio11' +
              '\n19.exercicio12' +
              '\n20.exercicio13' +
              '\n21.exercicio14' +
              '\n22.exercicio15'
              '\n23.exercicio16'
              '\n24.exercicio17'
              '\n25.exercicio18'
              '\n26.exercicio19'
              '\n27.exercicio20'
              '\n29.exercicio22'
              '\n30.exercicio23'
              '\n31.exercicio24'
              '\n32.exercicio25'
              '\n33.exercicio26'
              '\n34.exercicio27'
              '\n35.exercicio28'
              '\n36.exercicio29'
              '\n37.exercicio30'
              '\n38.exercicio31'
              '\n39.exercicio32'
              '\n40.exercicio33'
              '\n41.exercicio34'
              '\n42.exercicio35'
              '\n43.exercicio36'
              '\n44.exercicio37'
              '\n45.exercicio38')

    def coletar(self):
        self.num1 = int(input('informe o primeiro numero: '))
        self.num2 = int(input('informe o segundo numero: '))

    def colect(self):
        self.num1 = int(input('informe o primeiro numero: '))
        self.num2 = int(input('informe o segundo numero: '))
        self.num3 = int(input('informe o segundo numero: '))

    def coletarr(self):
        self.num = int(input('informe um numero: '))

    def operacao(self):
        while self.opcao != 0:
            self.mostrarMenu()
            self.opcao = int(input('escolha uma das opções acima:'))
            if self.opcao == 0:
                print('Obrigado!!')
            if self.opcao == 1:
                self.coletar()  # chamando o input
                self.num1 = int(input('informe o primeiro numero: '))
                self.num2 = int(input('informe o segundo numero: '))

                print(f'a soma dos numeros é: {self.exer.somar(self.num1, self.num2)}')
            elif self.opcao == 2:
                self.coletar()
                print(f'a subtração dos numeros digitados é: {self.exer.subtrair(self.num1, self.num2)}')

            elif self.opcao == 3:
                self.coletar()
                print(f'a divisão dos numeros digitados é: {self.exer.dividir(self.num1, self.num2)}')

            elif self.opcao == 4:
                self.coletar()
                print(f'a multiplicação dos numeros digitados é: {self.exer.multiplicar(self.num1, self.num2)}')

            elif self.opcao == 5:
                self.coletar()
                print(f'A pontencia dos numeros digitados é: {self.exer.potencia(self.num1, self.num2)}')

            elif self.opcao == 6:
                self.coletar()
                print(f'a raiz dos numeros digitados é: {self.exer.raiz(self.num1)}')
                print(f'a raiz dos numeros digitados é: {self.exer.raiz(self.num2)}')

            elif self.opcao == 7:
                self.coletar()
                print(f'a taboada dos numeros digitados é: {self.exer.tabuada(self.num1)}')
                print(f'a taboada dos numeros digitados é: {self.exer.tabuada(self.num2)}')


            elif self.opcao == 8:
                print(self.exer.exercicio01())


            elif self.opcao == 9:
                print(self.exer.exercicio02())

            elif self.opcao == 10:
                print(self.exer.exercicio03())

            elif self.opcao == 11:
                print(self.exer.exercicio04())


            elif self.opcao == 12:
                self.coletarr()
                print(self.exer.exercicio05(self.num))

            elif self.opcao == 13:
                self.coletarr()
                print(self.exer.exercicio06(self.num))

            elif self.opcao == 14:
                self.coletarr()
                print(self.exer.exercicio07(self.num))

            elif self.opcao == 15:
                self.coletarr()
                print(self.exer.exercicio08(self.num))

            elif self.opcao == 16:
                self.coletarr()
                print(self.exer.exercicio09(self.num))

            elif self.opcao == 17:
                self.coletarr()
                print(self.exer.exercicio10())

            elif self.opcao == 18:
                self.coletarr()
                print(self.exer.exercicio11(self.num))

            elif self.opcao == 19:
                self.coletarr()
                print(self.exer.exercicio12(self.num))

            elif self.opcao == 20:
                self.coletarr()
                print(self.exer.exercicio13())

            elif self.opcao == 21:
                self.coletarr()
                print(self.exer.exercicio14())

            elif self.opcao == 22:
                self.coletarr()
                print(self.exer.exercicio15(self.num))

            elif self.opcao == 23:
                self.coletarr()
                print(self.exer.exercicio16())

            elif self.opcao == 24:
                self.coletarr()
                print(self.exer.exercicio17())

            elif self.opcao == 25:
                self.coletarr()
                print(self.exer.exercicio18(self.num))

            elif self.opcao == 26:
                self.coletarr()
                print(self.exer.exercicio19(self.num))

            elif self.opcao == 27:
                self.coletarr()
                print(self.exer.exercicio20(self.num))

            elif self.opcao == 28:
                self.coletar()
                print(self.exer.exercicio21(self.num1, self.num2))

            elif self.opcao == 29:
                self.coletarr()
                print(self.exer.exercicio22(self.num))

            elif self.opcao == 30:
                self.coletar()
                print(f'A área do retângulo é: {self.exer.exercicio23(self.num1, self.num2)}')

            elif self.opcao == 31:
                self.colect()
                print(f'O calculo da idade expressa em dias é: {self.exer.exercicio24(self.num1, self.num2,self.num3)}')

            elif self.opcao == 32:
                self.coletarr()
                print(self.exer.exercicio25(self.num))

            elif (self.opcao == 33):
                self.coletar()
                print(f'Seu novo salário é: {self.exer.exercicio26(self.num1, self.num2)}')

            elif self.opcao == 34:
                self.coletarr()
                print(self.exer.exercicio27(self.num))

            elif self.opcao == 35:
                self.colect()
                print(f'sua nota final é: {self.exer.exercicio28(self.num1, self.num2, self.num3)}')

            elif self.opcao == 36:
                self.coletarr()
                print(self.exer.exercicio29(self.num))

            elif self.opcao == 37:
                self.coletarr()
                print(self.exer.exercicio30(self.num))

            elif self.opcao == 37:
                self.coletarr()
                print(self.exer.exercicio31(self.num))

            elif self.opcao == 39:
                print(self.exer.exercicio32())

            elif self.opcao == 40:
                self.coletarr()
                print(self.exer.exercicio33(self.num))
            else:
                print("codigo escolhido não é válido!")





















