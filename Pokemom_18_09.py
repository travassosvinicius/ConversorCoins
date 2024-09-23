import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from cProfile import label
from tkinter import font
from tkinter import ttk

tela = tk.Tk()
tela.title("Pokemon")
tela.geometry("500x400")

def busca_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=1302"
    lista_pokemon = requests.get(url)
    lista_pokemon = lista_pokemon.json()
    pokemons = lista_pokemon['results']
    pokedex = []
    for pokemon in pokemons:
        pokedex.append(pokemon['name'])
    return pokedex




def pegar_pokemon(pokemon):
    url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
    qual_pokemon = requests.get(url)
    qual_pokemon = qual_pokemon.json()
    imagem = qual_pokemon['sprites']['front_shiny']
    return imagem

def pega_imagem(link_da_imagem):
    resposta_site = requests.get(link_da_imagem)
    imagem_site = BytesIO(resposta_site.content)
    imagem = Image.open(imagem_site)
    imagem = imagem.convert("RGB")
    return imagem

def converter(imagem):
    with BytesIO() as output:
        imagem.save(output, format= "PPM")
        ppm_imagem = output.getvalue()
    return ppm_imagem

def abrir_imagem(url_imagem):
    nova_imagem = pega_imagem(url_imagem)
    nova_imagem_ppm = converter(nova_imagem)
    nova_imagem = tk.PhotoImage(data=nova_imagem_ppm)
    canva.itemconfig(imagem_canvas, image=nova_imagem)
    canva.image = nova_imagem

def poke():
    pokemon_digitado = caixa_texto.get()
    url_image = pegar_pokemon(pokemon_digitado)
    abrir_imagem(url_image)

def poke_combobox(event):
    pokemon_digitado = box.get()
    url = pegar_pokemon(pokemon_digitado)
    abrir_imagem(url)


canva = tk.Canvas(tela, width=350, height=300)
canva.pack(pady=1)

imagem_canvas = canva.create_image(182, 182)

caixa_texto = tk.Entry(tela)
caixa_texto.pack(pady=5)

pokedex = busca_pokemon()
box = ttk.Combobox(tela, values=pokedex)
box.bind("<<ComboboxSelected>>", poke_combobox)
box.pack(pady=4)


botao = tk.Button(tela, text="Gerar Pokemon", command= poke)
botao.pack(pady=5)

tela.mainloop()