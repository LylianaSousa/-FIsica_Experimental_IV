# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 23:41:31 2021

@author: muh_b
"""

import numpy as np # Biblioteca para manipulação númerica
import matplotlib.pyplot as plt # Biblioteca para visualização e gráficos
import scipy as st # Biblioteca de funções estatísticas
from scipy.odr import *
import math

arquivos = ['Tomada_2',
            'Tomada_1']

arquivos1 = ['Tomada_2']

def func (a,x):
    x0 = x
    x1 = (x0/180)*math.pi
    return a[1]*(np.sin(a[0]*np.sin(x1))/(a[0]*np.sin(x1)))**2

for j in range (len(arquivos1)):
    dados_arq = open(arquivos[j], 'r')
    linhas = dados_arq.readlines()
    x = np.zeros(len(linhas))
    I = np.zeros(len(linhas))
    for i in range(len(linhas)):
        T = linhas[i].split()
        x[i] = float(T[0])
        I[i] = float(T[1])
    x = x - 21.8
    f = Model(func)
    data = Data(x, I, wd=1, we=1)
    myodr = ODR(data, f, beta0=[99, 16])
    myoutput = myodr.run()
    myoutput.pprint()
    popt = myoutput.beta
    # popt, pcov = st.optimize.curve_fit(func, x, I, p0=[99,18])
    # print(popt)
    start = x[0]
    stop = x[-1]
    steps = 5000
    size = (x[-1]-x[0])/steps
    xa = np.zeros(steps)
    Ia = np.zeros(steps)
    for h in range(steps):
        xa[h] = (h*size) + start
        Ia[h] = func(popt,(h*size) + start)
    plt.figure(figsize=(18, 12), dpi=400)
    plt.plot(xa,Ia,"-")
    plt.plot(x,I,"*",c='red')
    plt.ylabel('Intensidade relativa ( %)')
    plt.xlabel(' θ ( °)')
    plt.title('Gráfico da Intensidade em função de  θ para Tomada 2')