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
    
    def button5(self=None):
        from interpolacaoPolinomial.lagrange import lagrange

    def button6(self=None):
        from interpolacaoPolinomial.newton import newton



    dispatch_dictionary = {'Bisseção':button1, 'Newton':button2, 'LU e Gauss':button3, 'Jacobi e Gauss-Seidel':button4, 'de Lagrange':button5, 'de Newton':button6}
    layout = [[sg.Text('Zero de função', auto_size_text=True)],
            [sg.Button('Bisseção'), sg.Button('Newton')], 
            [sg.Text( )],

            [sg.Text('Sistemas Lineares')],
            [sg.Button('LU e Gauss'), sg.Button('Jacobi e Gauss-Seidel')],

            [sg.Text( )],

            [sg.Text('Interpolação Polinomial')],
            [sg.Button('de Lagrange'), sg.Button('de Newton')],
            
            [sg.Text( )],
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