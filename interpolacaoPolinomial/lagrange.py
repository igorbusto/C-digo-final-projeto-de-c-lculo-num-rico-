import PySimpleGUI as sg
from itertools import product

class lagrange:
    def __init__(self):
        layout = [
            [sg.Text(' ')],
            [sg.Text('f(x):', size = (3,0)), sg.Input(size = (15,0))],

            [sg.Output(size = (80,20))],
            [sg.Button('Executar'), sg.Quit('Sair')],
        ]
    
        self.janela = sg.Window("Interpolação Polinomial de Lagrange").layout(layout)
        
   
    
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            fx = float(self.values[0])

            x = ([-1,0,2])
            y = ([4,1,-1])

            print('x',x)
            print('y',y)
            
            final = 0 
            for j in range(0, len(x)):
                L = 1
                M = 1
                for i in range(0, len(x)): 
                    if(i != j):
                        if(i == 0):
                            L = (fx - x[i])
                            print('cima  ', fx, '-', x[i], '=', L)
                            M = (x[j] - x[i])
                            print('baixo   ', x[j], '-', x[i], '=', M)
                         
                        else:
                            L = L * (fx - x[i])  
                            print('cima  ', fx, '-', x[i], '=', L)    
                            M = M * (x[j] - x[i])
                            print('baixo   ', x[j], '-', x[i], '=', M)
                instancia = float(L / M)
                print('resultado: ', instancia)
                print()

                final = y[j]*instancia + final
            print('Resultado final: ', final)
                
            if self.event in (None, 'Sair'):
                break

        self.janela.Close()
        sg.popup_ok('Interpolação Polinomial de Lagrange finalizado!')


tela = lagrange()
tela.Iniciar()