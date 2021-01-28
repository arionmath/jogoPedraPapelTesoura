import random
from tkinter import *
#1=pedra|2=papel|3=tesoura

def NumparaPalavra(num):
    if num == 1 :
        return "pedra"
    elif num == 2 :
        return "papel"
    elif num == 3 :
        return "tesoura"
    else:
        print("número inválido")

def main(resposta,janela):
    nummeroAleatorio = random.randint(1,3)
    
    if nummeroAleatorio - resposta == -1 or nummeroAleatorio - resposta == 2 :
        msg=f"A cpu escolheu {NumparaPalavra(nummeroAleatorio)},Voce ganhou"
    elif nummeroAleatorio==resposta:
        msg = "Vocês escolheram a mesma opcao"
    else:
        msg=f"A cpu escolheu {NumparaPalavra(nummeroAleatorio)},Voce perdeu"

    Label(janela,text=msg).pack()



app= Tk()
app.title("Pedra papel ou tesoura")
app.geometry("500x200")
app.config(background="#bbf")

res=StringVar()

pedra   = Radiobutton(app,text="pedra",value="1", variable=res)
papel   = Radiobutton(app,text="papel",value="2", variable=res)
tesoura = Radiobutton(app,text="tesoura",value="3",variable=res)

pedra.pack(padx=20,pady=5, fill=X)
papel.pack(padx=20,pady=5, fill=X)
tesoura.pack(padx=20,pady=5, fill=X)

jogar = Button(app,text="Fazer jogada",command=lambda: main(int(res.get()),app) )
jogar.pack(pady=15)

app.mainloop()