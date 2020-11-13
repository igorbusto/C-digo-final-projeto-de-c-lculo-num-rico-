import PySimpleGUI as sg
import numpy as np

class newton:
    def __init__(self):
        layout = [
            [sg.Text(' ')],
            [sg.Text('f(x):', size = (3,0)), sg.Input(size = (15,0))],

            [sg.Output(size = (80,20))],
            [sg.Button('Executar'), sg.Quit('Sair')],
        ]
    
        self.janela = sg.Window("Interpolação Polinomial de Newton").layout(layout)
        
   
    
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            fx = float(self.values[0])

            x = np.array([-1,0,2], dtype="double")
            y = np.array([4,1,-1], dtype="double")

            print('x',x)
            print('y',y)
            print()

            T = np.zeros((3,3))

            T[:,0]=y

            #segunda coluna  
            T[1,1]=(T[1,0]-T[0,0])/(x[1]-x[0]);  
            T[2,1]=(T[2,0]-T[1,0])/(x[2]-x[1]);  
            
            #terceira coluna  
            T[2,2]=(T[2,1]-T[1,1])/(x[2]-x[0]); 

            d0 = T[0,0]
            d1 = T[1,1]
            d2 = T[2,2]

            print('d1: ', d0)
            print('d2: ', d1)
            print('d3: ', d2)

            print()
            print(T)
            print()

            final = d0 + d1*(fx+1) + d2*(fx+1)*(fx-0)
            print('valor final: ', final)



            if self.event in (None, 'Sair'):
                break
           

        self.janela.Close()
        sg.popup_ok('Interpolação Polinomial de Newton finalizado!')
          

tela = newton()
tela.Iniciar()