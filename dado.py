import random
import PySimpleGUI as sg


class dado():


    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Girar? '
        #layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'), sg.Button('não')]
        ]


    def iniciar(self):
        #janela
        self.janela = sg.Window('Dado',layout=self.layout)
        #ler valores
        self.eventos, self.valores = self.janela.Read()

        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.ValorDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Até mais!')
            else:
                print('Favor escolher uma opção! ')
        except:print('Ocorreu um erro ao receber sua resposta')


    def ValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

dados = dado()
dados.iniciar()        

