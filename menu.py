import PySimpleGUI as sg

class menu:
    sg.theme('Light Blue 3')

    def button1(self=None):
        from zeroFuncao.Bissecao import TelaBissecao

    def button2(self=None):
        from zeroFuncao.Newton import Newton
    
    def button3(self=None):
        from sistemasLineares.diretos import diretos

    def button4(self=None):
        from sistemasLineares.iterativos import iterativos    
    

    dispatch_dictionary = {'Bisseção':button1, 'Newton':button2, 'Direto':button3, 'Iterativos':button4}
    layout = [[sg.Text('Zero de função', auto_size_text=True)],
            [sg.Button('Bisseção'), sg.Button('Newton')], 
            [sg.Text( )],

            [sg.Text('Sistemas Lineares')],
            [sg.Button('Direto'), sg.Button('Iterativos')],

            [sg.Text( )],
            [sg.Quit('Encerrar')]]



    window = sg.Window('Métodos', layout)
    while True:
        event, value = window.read()
        if event in ('Encerrar', sg.WIN_CLOSED):
            break
        if event in dispatch_dictionary:
            func_to_call = dispatch_dictionary[event]
            func_to_call()
        else:
            print('Event {} não encontrado'.format(event))

    window.close()
    sg.popup_ok('Menu finalizado!')
menu = menu()