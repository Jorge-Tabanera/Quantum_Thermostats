#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:43:31 2022

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
    
    for muestras in range(3000):
            
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
            thetas.append( theta_f - theta_o )
            
            periods.append( (2*np.pi - theta_o + theta_oprima + theta_f - theta_fprima) )
            # print(theta_o)
        # except:
        #     'Owo'
    return thetas, energies, periods

 #%%   
# py.hist(thetas, bins = 100, density = True)
    


thetas_mean = []
thetas_std = []
Energies_mean = []
Energies_std = []

periods_mean = []
periods_std = []

Energies = []

for uve in np.linspace( 2 , 50 , 5 ):
    
    print(uve)
    
    E = Energy(uve, x_L, 0)
    thetas, energies, periods = evaluate(E)
    
    thetas_mean.append(np.mean(thetas))
    thetas_std.append(0.3*np.std(thetas))
    
    Energies_mean.append(np.mean(energies))
    Energies_std.append(.3*np.std(energies))
    
    periods_mean.append(np.mean(periods))
    periods_std.append(np.std(periods))
    
    Energies.append(E)
    

#%%    
py.errorbar(Energies,thetas_mean, yerr =  3*np.array(thetas_std)   ) 

py.twinx()
py.errorbar(Energies,Energies_mean, yerr =  np.array(Energies_std), color = 'r')   

py.figure()
py.errorbar(Energies, periods_mean, yerr =  300*np.array(periods_std), color = 'r')
















