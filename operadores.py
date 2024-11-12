class Operacoes():
    @staticmethod
    def somar(a, b):
        return a + b
    
    @staticmethod
    def subtrair(a, b):
        return a - b
    
    @staticmethod
    def multiplicar(a, b):
        return a * b
    
    @staticmethod
    def dividir(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Divisão por zero não é permitida!"
    
    @staticmethod
    def pontenciar(a, b):
        return a ** b
    