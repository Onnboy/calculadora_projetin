from operadores import Operacoes

class InterfaceCalculadora():
    @staticmethod
    def exibir_menu():
        print("<~~~ Calculadora ~~~>")
        print("1. Soma")
        print("2. Subtração")
        print("3. Divisão")
        print("4. Multiplicação")
        print("5. Potenciacão")
        print("6. Sair")

    @staticmethod
    def linha_pontilhada():
        print("-" * 30)

    @staticmethod
    def execucao():
        operacoes = {
            "1": Operacoes.somar,
            "2": Operacoes.subtrair,
            "3": Operacoes.dividir,
            "4": Operacoes.multiplicar,
            "5": Operacoes.pontenciar
        }
        
        while True:
            InterfaceCalculadora.exibir_menu()
            escolha = input("Digite o número da operação desejada: ")
            InterfaceCalculadora.linha_pontilhada()
            
            if escolha == '6':
                print("Saindo . . .")
                break
            
            if escolha in operacoes:
                    num1 = float(input("Digite o primeiro numero: "))
                    num2 = float(input("Digite o segundo numero: "))
                    
                    try:
                        resultado = operacoes[escolha](num1, num2)
                        print(f"Resultado = {resultado}")
                        InterfaceCalculadora.linha_pontilhada()
                    except ZeroDivisionError:
                        print("Error: Não é possivel dividir por zero!")
            else:
                print("Opção inválida. Tente novamente!")
                InterfaceCalculadora.linha_pontilhada()

InterfaceCalculadora.execucao()
