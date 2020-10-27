from sympy import *
import PySimpleGUI as sg
import time

class iterativos:
    def __init__(self):
        #sg.change_look_and_feel('LightBrown4')
        layout = [
            #[sg.Text('                                         Método de Newton', size = (50,0))],
            [sg.Text(' ')],
            [sg.Text('Iterativos:', size = (7,0))],
            [sg.Output(size = (80,20))],
            [sg.Button('Executar'), sg.Quit('Sair')],
        ]
    
        self.janela = sg.Window("Metodo iterativos").layout(layout)
        
   
    
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            #formula = self.values[0]
            #xZero = self.values[1]
            #e = self.values[2]

            if self.event in (None, 'Sair'):
                break
            #if self.event == 'Executar':
                #self.metodoNewton(formula, xZero, e)

        self.janela.Close()
        sg.popup_ok('Método iterativo finalizado!')
          

tela = iterativos()
tela.Iniciar()