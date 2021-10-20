#!/usr/bin/env python
# coding: utf-8

# # h-parameters

# In[1]:


import schemdraw
import schemdraw.elements as elm

d1 = schemdraw.Drawing()
d1.push()
d1 += elm.Gap().down().label(['+', '$v_{be}$', '–'])
d1.pop()
d1 += (r1 := elm.Resistor().label('$ h_{ie} $', loc ="bot"))
d1.labelI(r1, '$i_b $')
d1 += elm.SourceControlledV().down().reverse().label('$ h_{re} v_{ce} $', loc ="bot")

d1.push()
d1 += elm.Line().left()
d1.pop()

d1 += elm.Line().right()
d1 += elm.SourceControlledI().up().reverse().label('$ h_{fe} i_b $', loc ="bot")
d1 += elm.Line().right()

d1.push()
d1 += (L1:= elm.Line().right()) 
d1.labelI(L1, '$i_c$',reverse=True)
d1 += elm.Gap().down().label(['+', '$v_{ce}$', '–'])
d1.pop()

d1 += elm.Resistor().down().label('$ \\dfrac{1}{h_{oe}} $', loc ="bot")

d1.push()
d1 += elm.Line().left()
d1.pop()

d1 += elm.Line().right() 

d1.draw()


# $$ v_{be} = h_{ie}i_b + h_{re}v_{ce}  \\
# 
#  i_{c} = h_{fe}i_b + \dfrac{v_{ce}}{\dfrac{1}{h_{oe}}}$$

# In[2]:


import schemdraw
import schemdraw.elements as elm
import matplotlib.pyplot as plt
plt.xkcd()

d1 = schemdraw.Drawing()
d1.push()
d1 += elm.Gap().down().label(['+', '$v_{be}$', '–'])
d1.pop()
d1 += (r1 := elm.Resistor().label('$ h_{ie} $', loc ="bot"))
d1.labelI(r1, '$i_b $')
d1 += elm.SourceControlledV().down().reverse().label('$ h_{re} v_{ce} $', loc ="bot")

d1.push()
d1 += elm.Line().left()
d1.pop()

d1 += elm.Line().right()
d1 += elm.SourceControlledI().up().reverse().label('$ h_{fe} i_b $', loc ="bot")
d1 += elm.Line().right()

d1.push()
d1 += (L1:= elm.Line().right()) 
d1.labelI(L1, '$i_c$',reverse=True)
d1 += elm.Gap().down().label(['+', '$v_{ce}$', '–'])
d1.pop()

d1 += elm.Resistor().down().label('$ \\dfrac{1}{h_{oe}} $', loc ="bot")

d1.push()
d1 += elm.Line().left()
d1.pop()

d1 += elm.Line().right() 

d1.draw()


# In[ ]:




