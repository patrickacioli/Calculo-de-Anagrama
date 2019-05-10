from tkinter import*
from tkinter import filedialog
from functools import partial
from anagrama import anagrama

class Janela:

        def __init__(self, janela = None):

                janelaPrincipal = janela
                janelaPrincipal.title("Calculadora de Permutações")
                janelaPrincipal.geometry("370x150")
                janelaPrincipal.resizable(False, False)

                global inserir_dado, comparacao
                
                info_inserir = Label(janelaPrincipal, text = "Insira um número ou nome", font = ("Arial", 10))
                inserir_dado = Entry(janelaPrincipal, justify = 'center', font = ('Arial', 12), bd = 3.5)
                info_comparar = Label(janelaPrincipal, text = "Achar o que você digitou nos anagramas (opcional)", font = ("Arial", 10))
                comparacao = Entry(janelaPrincipal, justify = 'center', font = ('Arial', 12), bd = 3.5)
                confirmar = Button(janelaPrincipal, text = "Calcular", foreground = 'black',
                                        command = PageCalculate)

                info_inserir.pack()
                inserir_dado.pack()
                info_comparar.pack()
                comparacao.pack()
                confirmar.pack()

class PageCalculate:

        def __init__(self):
                self.windowResult = Tk()
                self.frame_result = Frame(self.windowResult)
                self.frame_result.pack()
                self.windowResult.title("Resultado")
                self.exibirPermutacao(self.calcularPermutacao(inserir_dado.get()))

        def calcularPermutacao(self, numero):
                calc = anagrama(numero)
                return calc

        def exibirPermutacao(self, callback):
                text = ""
                const = len(list(inserir_dado.get()))
                
                for valor in range(len(callback)):

                        if valor % const == 0:
                                subframe = Frame(self.frame_result)
                                subframe.pack()

                        lb = Label(subframe, text = callback[valor] + " |")
                        text += callback[valor] + " |"
                        
                        if callback[valor] == comparacao.get():
                                lb['foreground'] = 'green'
                                lb['bg'] = 'white'
                                
                        lb.pack(side = 'left')

                inserir_dado.delete(0, END)
                comparacao.delete(0, END)
                
                save = Button(self.windowResult, text = "Salvar Anagramas", command = partial(self.save, text))
                sair = Button(self.windowResult, text = "Fechar", command = lambda: self.windowResult.destroy())
                
                save.pack(side = 'right')
                sair.pack(side = 'left')
        
        def save(self, text):

                opcoes = {'defaultextension':'.txt', 'title':"Escolha um diretorio para salvar o Anagrama"}

                try:
                        arquivo = filedialog.asksaveasfile(mode = 'w', **opcoes)
                        arquivo.write(text)
                        arquivo.close()
                except:
                        pass
