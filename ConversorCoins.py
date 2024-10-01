from doctest import master
import customtkinter as Conversor
from customtkinter import set_appearance_mode, CTkLabel

moedas = {'USD': 5.46,
          'BRL': 1,
          'EUR': 6.09,
          'GBP': 7.24,
          'JPY': 0.0038,
          'CHF': 6.45
          }


def Resultado(event):
    escolha = caixaselecao.get()
    conta = moedas[escolha[0:3]]
    resultado = float(valordigitado.get()) / conta
    variavelConvertida.set(resultado)

def mudar(choice):
    set_appearance_mode(choice)


#Criação da tela
tela = Conversor.CTk()
tela.title('Conversor de Moedas')
tela.configure(background='lightblue')
tela.geometry('600x600')



#Criação primeira lable
conversor = Conversor.CTkLabel(tela,text='Converta sua Moeda')
conversor.place(x= 250, y= 5)

#Criação segunda lable
DigiteValor = Conversor.CTkLabel(tela,text='Digite um valor em BRL')
DigiteValor.place(x=-1,y=120)

ValorConvertido = Conversor.CTkLabel(tela,text='Valor Convertido')
ValorConvertido.place(x=-1,y=280)

escolhamoeda = Conversor.CTkLabel(tela,text='Escolha a Moeda')
escolhamoeda.place(x=-1,y=195)

valordigitado = Conversor.CTkEntry(tela)
valordigitado.place(x= 250, y= 125)

variavelConvertida = Conversor.StringVar()
valormoeda = Conversor.CTkEntry(tela, textvariable=variavelConvertida)
valormoeda.place(x= 250, y= 285)

caixaselecao = Conversor.CTkComboBox(master)
values= ('USD - Dolar Americano', 'BRL - Real', 'EUR - Euro', 'GBP - Libra', 'JPY - Iene', 'CHF - Franco Suiço')
caixaselecao.configure(values=values, command=Resultado, width=160)
caixaselecao.set('Escolha uma moeda')

caixaselecao.place(x=250 , y= 200)

escolhaAparencia = CTkLabel(tela, text='Escolha uma aparência para a janela')
escolhaAparencia.place(x=220 , y=450)

aparencia = Conversor.CTkComboBox(tela,)
aparenciaValores = ('light' , 'dark')
aparencia.configure(values=aparenciaValores, command=mudar, width=160)
aparencia.set('Escolha um tema')
aparencia.place(x=250 , y=500)


tela.mainloop()
