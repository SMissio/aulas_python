#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui as pm

pm.sleep(4)


pm.moveTo(x=19, y=750)
pm.click(x=19, y=750)

pm.sleep(6)

#Point(x=740, y=462)
#print (pm.position())

pm.typewrite('calc')
pm.sleep(2)
pm.moveTo(x=149, y=197)
pm.click(x=149, y=197)


# In[ ]:


import pyautogui as pm

pm.sleep(6)

print (pm.position())


# In[2]:


import pyautogui as posicaoabrirGoogle
posicaoabrirGoogle.sleep(6)
#print (pm.position())
posicaoabrirGoogle.doubleClick(x=119, y=526)
posicaoabrirGoogle.sleep(4)
posicaoabrirGoogle.typewrite('https://www.google.com/')
posicaoabrirGoogle.sleep(4)
posicaoabrirGoogle.press('enter')
posicaoabrirGoogle.sleep(5)
posicaoabrirGoogle.typewrite('Dolar Hoje')
posicaoabrirGoogle.sleep(4)
posicaoabrirGoogle.press('enter')


# In[ ]:




