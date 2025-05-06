#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:00:39 2022

@author: jorge
"""

import numpy as np


dt = 0.0001 
sqrtdt = np.sqrt(dt)

m = 12e-3 #eV/nm**2/Ghz**2


#DYNAMICAL PARAMETERS

Omega = 1 #GHz
k = m * Omega**2 #eV/nm OSCILLATOR CONSTANT

Q = 10000
gamma = 1.248e-1/Q #eV/nm2/GHz# 1.248e-4/Q #eV/nm2/GHz
 
g0 = 1e-2 #eV/nm #1.8e6 #eV/m

# f0 = 3e-3

omega_force = 1*Omega


#TRANSPORT EQUATION

epsilon_01 = 0#  g0_eV * 1e-11

# Gamma_L = 500
# Gamma_R = 500

# mu = [ 1, 1.5, 2, 3 ]
mu = 1
mu_L =  mu * g0
mu_R = - mu * g0


#THERMAL NOISE

Kb = 8.6e-5 #eV/K
T = 1e-20 #K de los lead
T_diff = 1e-20

D = T_diff#Kb*T #Diffusion coef
sigma = np.sqrt( 2*D*m**2 )


