#!/usr/bin/env python
# coding: utf-8

# # Analog Electronics and Circuits
# 
# ```{admonition} power is absorbed in case of semiconductor devices
# :class: dropdown
# current direction should oppose voltage to make power -ve for example breakdown voltage should oppose the direction of flow of current
# ```
# ```{dropdown} Here's my dropdown
# And here's my dropdown content
# 
# ```{dropdown} Here's my dropdown
# And here's my dropdown content
# ```
# 
# ```
# 
# - measuring devices
#     - iron voltmeter
#         
#         RMS 
#         
#     - magnetic
# - capacitors
#     
#     `voltage and current across capacitor is zero` → `short circuit`
#     
#     capacitors doesn't allow abrupt changes : $V_c(t^+)=V_c(t^-) = V_c(t)$ 
#     
# - inductors
#     
#     `voltage and current across inductor is zero` → `open circuit`
#     
# - diodes
#     - clampers
#         - negative clamper
#             
#             $V_{in_{max}} > 0$  for diode to conduct  
#             
#         - positive clamper
#             
#             $V_{in_{min}} < 0$ for diode to conduct
#             
#     - rectifiers
#         
#         $\text{form-factor} = \dfrac{x_{rms}}{x_{avg}}$ 
#         
# - transistor
#     - transistor biasing
#         
#         $S = \dfrac{\partial I_C}{\partial I_{C_O}} = \dfrac{\beta + 1}{1 - \beta\dfrac{\partial I_B}{ \partial I_C}}$
#         
#         $I_{E} = I_C+I_B$
#         
#         $I_C = \beta I_B + (1+\beta) I_{C_{O}}$
#         
#         $\beta = \frac{I_C}{I_B}$ ; common emitter gain (base as input and collector as output)
#         
#         $\alpha = \frac{I_C}{I_E}$ ; common base gain 
#         
#         If $\beta$ is high,  $I_C = I_E$ and  $I_B = 0$
#         
#         - collector with base bias with RE
#             
#         - voltage divider bias with RE
#             
#            
#             
#     - small signal analysis
#         - steps
#             1. turn off all dc sources and short all capacitors (small signal equivalent)
#             2. calculate parameters such as $r_\pi, r_e, g_m$
#             3. replace by model 
#             - calculate
#                 - $r_i, R_i$
#                 - $r_o, R_o$  by putting $v_s = 0$
#                 - $A_v = \dfrac{v_o}{v_s}$
#                 - $A_I = \dfrac{i_l}{i_i}$
#         
#         $g_m = \dfrac{I_c}{V_T}$
#         
#         $r_\pi = \dfrac{\beta}{g_m}$
#         
#         $r_o= \dfrac{V_A}{I_C} = \dfrac{1}{\lambda I_C}$
#         
#         $\boxed{\dfrac{v_{be}}{i_b} = h_{ie} = (1+\beta)r_e = r_\pi}$
#         
#         $\boxed{\dfrac{i_{c}}{i_b} = h_{fe} = \beta = g_mr_\pi}$
#         
#         - h - parameter
#             
#             $v_{be} \approx h_{ie} i_b$
#             
#             $i_c \approx h_{fe} i_b$
#             
#         - $r_e$ - model
#             
#             $r_e = \dfrac{V_T}{I_E}$
#             
#             $v_{be} = i_b (1+\beta) r_e$
#             
#             $r_i = \dfrac{v_{be}}{i_b} = (1+\beta)r_e$
#             
#         - $\pi$ -model
#             
#             $i_c = \dfrac{I_C}{V_T} v_{be} = g_m v_{be}$
#             
#             $\boxed{\dfrac{v_{be}}{i_b} = \dfrac{\beta}{g_m} = r_\pi}$
#             
#         - CE with $R_{E}$
#             
#             $R_i = (r_{\pi} + \beta R_E) || R_B$ 
#             
#             $A_v = \dfrac{-g_m R_C}{1 + g_m R_E}$
#             
#     - multistage
#         - CE-CE and CE-CC → cascade
#         - CE-CB → cascode
#         - CC-CC → Darlington pair
#         
# - op-amp
#     - differential amplifier
#         - differential mode
#             
#             $A_{v_1} = A_{v_2} = -g_m R_c$
#             
#             $A_d = \dfrac{v_o}{v_{id}} = g_m R_c$
#             
#         - common mode
#             
#             $A_{v_1} = A_{v_2} = A_c =\dfrac{-g_m R_c}{1 + 2 g_m R_E}$
#             
#         
#         $\text{CMRR} = \biggm\vert \dfrac{A_d}{A_c} \biggm\vert = 1 + 2\cdot g_m R_E$
#         
#         $v_{c} = \dfrac{v_1 + v_2 }{2}$
#         
#         $v_{id} = v_1 - v_2$
#         
#         $v_o = A_d\cdot v_{id} + A_c \cdot v_{c}$

# ```{admonition} Click the button to reveal!
# :class: dropdown
# Some hidden toggle content!
# ```
