from sympy import *
import PySimpleGUI as sg
import numpy as np  
from numpy import linalg  

class iterativos:
    def __init__(self):
        #sg.change_look_and_feel('LightBrown4')
        layout = [
            #[sg.Text('                                         Método de Newton', size = (50,0))],
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
            m = [[10,2,1],
                [1,5,1],
                [2,3,10]]
            
            b = [7,-8,6]

            x0 = [0.7, -1.6, 0.6]

            print('Original: \n', m[0][0],'|',m[0][1],'|',m[0][2], ' = ',b[0],'\n',
                                m[1][0],'|',m[1][1],'|',m[1][2],' = ',b[1],'\n',
                                m[2][0],'|',m[2][1],'|',m[2][2],' = ', b[2])
            print()

            print('x0: ', x0)
            print()

            print('Jacobi: ', self.jacobi(m,b,x0,3,0.1))
            print()
            print('Seidel: ', self.gauss_seidel(m,b,x0,3,0.1))

            if self.event in (None, 'Sair'):
                break
            #if self.event == 'Executar':
                #self.metodoNewton(formula, xZero, e)

        self.janela.Close()
        sg.popup_ok('Método iterativo finalizado!')
          

    ###############  JACOBI  #################
    def jacobi(self,A,b,x0,N,tol):  
        #preliminares  
        '''A = A.astype("double")  
        b = b.astype("double")  
        x0 = x0.astype("double")  '''
    
        n=np.shape(A)[0]  
        x = np.zeros(n)  
        it = 0  
        #iteracoes  
        while (it < N):  
            it = it+1  
            #iteracao de Jacobi  
            for i in np.arange(n):  
                x[i] = b[i]  
                for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
                    x[i] -= A[i][j]*x0[j]  
                x[i] /= A[i][i]  
            #tolerancia  
            if (np.linalg.norm(x-x0,np.inf) < tol):  
                return x  
            #prepara nova iteracao  
            x0 = np.copy(x)  
        raise NameError('num. max. de iteracoes excedido.')


    ############  SEIDEL  ###########
    def gauss_seidel(self,A,b,x0,N,tol):  
        #preliminares  
        '''A = A.astype('double')  
        b = b.astype('double')  
        x0 = x0.astype('double')  '''
    
        n=np.shape(A)[0]  
        x = np.copy(x0)  
        it = 0  
        #iteracoes  
        while (it < N):  
            it = it+1  
            #iteracao de Jacobi  
            for i in np.arange(n):  
                x[i] = b[i]  
                for j in np.concatenate((np.arange(0,i),np.arange(i+1,n))):  
                    x[i] -= A[i][j]*x[j]  
                x[i] /= A[i][i]  
            #tolerancia  
            if (np.linalg.norm(x-x0,np.inf) < tol):  
                return x  
            #prepara nova iteracao  
            x0 = np.copy(x)  
        raise NameError('num. max. de iteracoes excedido.')


tela = iterativos()
tela.Iniciar()