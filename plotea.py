#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 20:19:43 2022

@author: jorge
"""


import numpy as np
import pylab as py
from parameters import *

Gamma_L = 300
x_L = mu_L / g0

def ve(E, x):
    
    return np.sqrt(2/m*(E - k * x** 2 / 2))

def theta(v,x):
    
    return np.arctan2(v,(Omega*x))
    
def Energy(v,x, disp):
    
    return 0.5 * m * v ** 2 + 0.5 * k * (x - disp) ** 2

def p_poisson(E,x):
    
    v_L = ve(E, x_L)
    
    return  np.exp( -Gamma_L * x / v_L )

def choose_poisson(E):
    
    v_L = ve(E, x_L)
    ref = Gamma_L * x_L/v_L
    esto = False
    
    while esto == False:
            
        xx = 1.5 * x_L * np.random.uniform()
        a = np.random.uniform()
        
        po = p_poisson(E, xx)
        
        if po > a:
            
            esto = True
            return xx
    
    
    
def evaluate(E):
    
    #E_lim = 0.0006
    

    periods = []
    energies = []
    thetas = []
    
    
    theta_in = []
    theta_out = []
    
    for muestras in range(10000):
            
        # try:
            x_in = x_L + choose_poisson(E)
            x_out = x_L - choose_poisson(E)
            
            v_in = ve(E,x_in)
            theta_o = theta(v_in , x_in)
            theta_oprima = theta(v_in , x_in - g0/k)
            
            E_new = Energy(v_in, x_in, + g0/k * 0.5)
            v_new = ve(E_new, x_out)
            # theta_new = theta(v_new, x_out)
            
            theta_f = - theta(v_new , x_out)
            theta_fprima =  - theta(v_new , x_out - g0/k)
            dE =  Energy(v_new, x_out, 0) - E
            
            energies.append(dE)
            thetas.append( theta_f  - theta_o )
            
            theta_in.append(theta_o)
            theta_out.append(theta_f)
            
            periods.append( (2*np.pi - theta_o + theta_oprima + theta_f - theta_fprima) )
            # print(theta_o)
        # except:
        #     'Owo'
    return thetas, energies, periods, theta_in, theta_out

 #%%   

A = evaluate(.1)

# py.figure()
py.subplot(1,2,1)
py.hist(A[3],bins = 100, density = True, color = 'b')
py.xlabel('$\\theta_{in}$')

py.subplot(1,2,2)
py.hist(A[4],bins = 100, density = True, color = 'r')
py.xlabel('$\\theta_{out}$')

py.figure()

py.hist(A[0],bins = 100, density = True, color = 'b')
py.xlabel('$\Delta\\theta$')


py.figure()

py.hist(A[1],bins = 100, density = True, color = 'orange')
py.xlabel('$\Delta E$')

py.figure()

py.hist(A[2],bins = 100, density = True, color = 'r')
py.xlabel('$\\tau$')











