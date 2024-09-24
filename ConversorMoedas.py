import tkinter
import tkinter as Conversor
import requests
from PIL import Image
from io import BytesIO
from tkinter import ttk
from xml.etree import ElementTree
from PIL.Image import ElementTree
from colorama import Fore, Style, init
from tkinter import font

moedas = {'USD': 5.46,
          'BRL': 1,
          'EUR': 6.09,
          'GBP': 7.30,
          'JPY': 0.0038,
          'CHF': 6.45
          }

def teste(event):
    escolha = caixaselecao.get()
    conta = moedas[escolha[0:3]]
    resultado = float(valordigitado.get()) * conta
    variavelConvertida.set(resultado)

#Criação da tela
tela = Conversor.Tk()
tela.title('Conversor de Moedas')
tela.configure(background='lightblue')
tela.geometry('600x600')

fonte1 = font.Font(family= "Times New Roman", size= 30)
fonte2 = font.Font(family= "Times New Roman", size= 16)

#Criação primeira lable
ConversordeMoeda = Conversor.Label(text='Converta sua Moeda', font=fonte1)
ConversordeMoeda.place(x= 130, y= 5)

#Criação segunda lable
DigiteValor = Conversor.Label(text='Digite um valor em BRL', font=fonte2)
DigiteValor.place(x=-1,y=120)

ValorConvertido = Conversor.Label(text='Valor Convertido', font=fonte2)
ValorConvertido.place(x=-1,y=280)

escolhamoeda = Conversor.Label(text='Escolha a Moeda', font=fonte2)
escolhamoeda.place(x=-1,y=195)

valordigitado = Conversor.Entry(tela)
valordigitado.place(x= 250, y= 125)

variavelConvertida = tkinter.StringVar()
valormoeda = Conversor.Entry(tela, textvariable=variavelConvertida)
valormoeda.place(x= 250, y= 285)

caixaselecao = ttk.Combobox(tela)
caixaselecao['values']= ('USD - Dolar Americano', 'BRL - Real', 'EUR - Euro', 'GBP - Libra', 'JPY - Iene', 'CHF - Franco Suiço')
caixaselecao.current()
caixaselecao.place(x=250 , y= 200)
caixaselecao.bind("<<ComboboxSelected>>", teste)


tela.mainloop()
