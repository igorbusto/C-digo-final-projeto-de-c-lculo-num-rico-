from sympy import *
import PySimpleGUI as sg
import time

class Newton:
    def __init__(self):
        #sg.change_look_and_feel('LightBrown4')
        layout = [
            #[sg.Text('                                         Método de Newton', size = (50,0))],
            [sg.Text(' ')],
            [sg.Text('Formula:', size = (7,0)), sg.Input(size = (15,0)), sg.Text('X0:', size = (3,0)), sg.Input(size = (15,0)), sg.Text('E:', size = (2,0)), sg.Input(size = (15,0))],
            [sg.Output(size = (80,20))],
            [sg.Button('Executar'), sg.Quit('Sair')],
        ]
    
        self.janela = sg.Window("Metodo de Newton").layout(layout)
        
   
    
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            formula = self.values[0]
            xZero = self.values[1]
            e = self.values[2]

            if self.event in (None, 'Sair'):
                break
            if self.event == 'Executar':
                self.metodoNewton(formula, xZero, e)

        self.janela.Close()
        sg.popup_ok('Método de Newton finalizado!')
        
    def metodoNewton(self, formula, xZero, e):
        x = Symbol('x')
        flx = str(eval(formula).diff(x))

        k = 0
        contaa = 0
        erro = float(10)
        e = float(e)
        x = float(xZero)


        while(erro > e):
            print('K: ', k)
            print('Xk: %.4f' % x)

            #fx = x ** 2 + x - 6      # f(x) formula original
            print('f(x): %.4f' % eval(formula))
            # Faz a conta substituindo o valor de x


            #flx = 2 * x + 1         # derivada f'(x) linha      
            print('fl(x): %.4f' % eval(flx))
            # Faz a conta da derivada substituindo o valor de x


            conta = x - (eval(formula) / eval(flx))     # faz a conta final
            x = conta
            print('Conta: %.4f' % conta)


            if(contaa != 0):
                erro = contaa - conta
                print('Erro: %.4f' % erro)  # faz a diferença do resultado final
                                            #  com o resultado final da iteração anterior
                contaa = conta
            else:
                print('Erro: ', 0)
                contaa = conta

            k = k + 1

            print()
            
        print('Fim   :)')
        
        

tela = Newton()
tela.Iniciar()