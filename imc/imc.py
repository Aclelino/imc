#!/usr/bin/env python
# coding: utf-8

# Autor : Aclelino Damião <br>
# E-mail: aclelino@gmail.com <br>
# GitHub: https://github.com/Aclelino<br>
# 
# Python 3.8.8 <br>
# 
# '''<br>
# Calculadora de imc <p>
# cálculo simples que permite medir se alguém está ou não com o peso ideal. Ele aponta se o peso está adequado ou se está abaixo ou acima
# <br>
# '''

# In[1]:



from PyQt5 import uic,QtWidgets


# In[2]:


def acao():
    peso =float(windows.lineKg.text())
    altura = float(windows.lineMt.text())
    
    print(peso)
    imc = peso / altura ** 2
    #imc = str(imc)
    resultado = windows.label_Resultado
    inf = windows.label_Inf
    
    inf.setText('O seu IMC e igual a {:.2f}\n'.format(imc))

    if imc < 16:
        resultado.setText("Magreza grau III😐")
    elif imc > 16.0 and imc < 16.9 :
        resultado.setText("Magreza grau II🤨")
    elif imc > 17.0 and imc < 18.4 : 
        resultado.setText("Magreza grau I🤔")
    elif imc > 18.5 and imc < 24.9 :
        resultado.setText("Adequado 😊")
    elif imc > 25.0 and imc < 29.9:
        resultado.setText("Pré-obeso😏")
    elif imc > 30.0 and imc < 34.9 :
        resultado.setText("Obesidade grau I😣")
    elif imc > 35.0 and imc < 39.9:
        resultado.setText("Obesidade grau II😥")
    elif imc >=40.0:
        resultado.setText("Obesidade grau III😫")



# In[3]:


app =QtWidgets.QApplication([])
windows = uic.loadUi('imc.ui')
windows.pushButton.clicked.connect(acao)
windows.show()
app.exec_()


# In[ ]:




