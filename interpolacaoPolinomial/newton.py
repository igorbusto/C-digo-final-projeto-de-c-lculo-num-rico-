import PySimpleGUI as sg


class newton:
    def __init__(self):
        #sg.change_look_and_feel('LightBrown4')
        layout = [
            #[sg.Text('                                         Método de Newton', size = (50,0))],
            [sg.Text(' ')],
            [sg.Text('Newton:', size = (7,0))],
            [sg.Output(size = (80,20))],
            [sg.Button('Executar'), sg.Quit('Sair')],
        ]
    
        self.janela = sg.Window("Interpolação Polinomial de Newton").layout(layout)
        
   
    
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
    
            if self.event in (None, 'Sair'):
                break
            #if self.event == 'Executar':
                #self.metodoNewton(formula, xZero, e)

        self.janela.Close()
        sg.popup_ok('Interpolação Polinomial de Newton finalizado!')
          

tela = newton()
tela.Iniciar()