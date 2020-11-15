import numpy as np
import PySimpleGUI as sg
import time
from math import fabs
#from matrix import newLine
#from sympy import *

class diretos:
    def __init__(self):
        layout = [
            #[sg.Text(' ')],
            [sg.Text('Direto:', size = (7,0))],
            [sg.Output(size = (80,20))],
            [sg.Button('Executar'), sg.Quit('Sair')],
        ]
    
        self.janela = sg.Window("Metodo direto").layout(layout)
        
   
    
    def Iniciar(self):
        while True:
            self.event, self.values = self.janela.Read()
            
            '''m = [[3,2,4],
                [1,1,2],
                [4,3,-2]]'''
            m = [[2,3,-1],
                [4,4,-3],
                [2,-3,1]]
            
            b = [5,3,-1]

            print('Original: \n', m[0][0],'|',m[0][1],'|',m[0][2], ' = ',b[0],'\n',
                                m[1][0],'|',m[1][1],'|',m[1][2],' = ',b[1],'\n',
                                m[2][0],'|',m[2][1],'|',m[2][2],' = ', b[2])
            print()
            print('LU:')
            self.decompositionLU(m,b)
            print()
            
            print('Gauss: ')
            self.soluciona_sem_pivotamento(m,b)

            if self.event in (None, 'Sair'):
                break

        self.janela.Close()
        sg.popup_ok('Método direto finalizado!')
          
    def soluciona_sem_pivotamento(self, M, b):
        """ 
        M : matriz nxn formada pelos coeficientes do sistema de equações
        b : vetor nx1 de valores associados a cada equação
        """
        # tamanho das linhas e colunas da matriz quadrada M
        n = len(M)
        '''if b.size != n:
            raise ValueError(f"Inválido: b deve ser n x 1 e M deve ser n x n. Recebido: b {b.size}x1 e M {n}x{n}")
        '''

        for linha_pivot in range(n-1):
            for linha in range(linha_pivot+1, n):
                # coeficiente m = razao entre primeiros valores das linhas escolhidas
                m = M[linha][linha_pivot]/M[linha_pivot][linha_pivot]

                # rodando as colunas
                for col in range(linha_pivot+1, n):
                    M[linha][col] = M[linha][col] - m*M[linha_pivot][col]
                # coluna de solução da equação
                b[linha] = b[linha] - m*b[linha_pivot]

        x = np.zeros(n)
        k=n-1
        x[k] = b[k]/M[k][k]
        while k >= 0:
            x[k] = (b[k] - np.dot(M[k][k+1:], x[k+1:]))/M[k][k]
            k-=1

    
        #return x
        print(x)


    def decompositionLU(self, a, b_list):
        # Variáveis
        L = []      # Matriz L    
        U = a       # Matriz U
        #P = 1

        # Geração da matriz L: gera uma matriz identidade de ordem n que será preenchida posteriormente
        for i in range (len(U)):
            line = self.newLine(len(U))
            for j in range (len(U[i])):
                if i == j:
                    line[j] = 1
            L.append(line)

        for k in range(len(U) - 1):
            # Pivô começa como o primeiro elemento da primeira linha
            pivot = U[k][k]
            print('pivô: ', pivot)

            # Salvo a linha do pivo para realizar a operação de troca
            #pivot_line = k

            for i in range(k+1, len(U)):
                # Verifico se o pivô é o maior elemento da coluna
                if fabs(U[i][k]) > fabs(pivot):
                    pivot = U[i][k]
                    pivot_line = i
            
            # Se o pivô for 0: saímos da iteração
            if pivot == 0:
                break
            
            # Se a linha do pivô não for a linha atual: troco as linhas
            '''if pivot_line != k:
                for j in range (len(U)):
                    swap = U[k][j]
                    U[k][j] = U[pivot_line][j]
                    U[pivot_line][j] = swap
                    P = P * (-1)

                # Troca os elementos da matriz de segundo termo
                for b in b_list:
                    swap = b[k]
                    b[k] = b[pivot_line]
                    b[pivot_line] = swap
            '''
            # Realiza pivoteamento parcial              
            #partialPivoting(U,k)

        # Popula matriz L
        for col in range(len(U)):
            for row in range(col+1, len(U)):
                mij = U[row][col]
                L[row][col] = mij
                U[row][col] = 0
                
        #return L, U, b_list
        print('Matriz L: ', L)
        print('Matriz U: ', U)
        print(b_list)

    def newLine(self, n):
        line = []
        for i in range(n):
            line.append(0)
        return line

tela = diretos()
tela.Iniciar()