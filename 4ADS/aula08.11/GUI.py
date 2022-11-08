#interface grafica com BD

from tkinter import *
from tkinter import messagebox
import os
import sqlite3

path = os.path.dirname(__file__)

favicon = os.path+'\\4ADS\aula08.11\computer.ico'

app = Tk()
app.title('GUI com Banco de Dados')
app.iconbitmap(favicon)
app.geometry('400x200')

#banco de dados - SQLITE3
con = sqlite3.connect("banco.db")
c = con.cursor()

#criação da tabela
c.execute("CREATE TABLE IF NOT EXISTS banco(nome text, sobrenome text, ender text, cidade text, estado text, cep integer)")

#cria função botão de comando
def gravar():
    con = sqlite3.connect("banco.db")
    c = con.cursor()
    
    c.execute("INSERT INTO banco VALUES (:nome, :sobre, :ender, :cidade, :estado, :cep)", {
        'nome':vnome.get(),
        'sobre':vnome.get(),
        'ender':vnome.get(),
        'cidade':vnome.get(),
        'estado':vnome.get(),
        'cep':vnome.get(),
    })
    con.commit()
    con.close()
    
    messagebox.showinfo("MENSAGEM IMPORTANTE", "INFORMAÇÕES GRAVADAS COM SUCESSO1")
    
    vnome.delete(0,END)
    vsobre.delete(0,END)
    vender.delete(0,END)
    vcidade.delete(0,END)
    vestado.delete(0,END)
    vcep.delete(0,END)
    
    Entry.focus(vnome)

#váriaveis de entrada
vnome = Entry(app, width=30)
vnome.grid(row=0, column=1, padx=20)

vsobre = Entry(app, width=30)
vsobre.grid(row=1, column=1)

vender = Entry(app, width=30)
vender.grid(row=2, column=1)

vcidade = Entry(app, width=30)
vcidade.grid(row=3, column=1)

vsobre = Entry(app, width=30)
vsobre.grid(row=1, column=1)

vestado = Entry(app, width=30)
vestado.grid(row=4, column=1)

vcep = Entry(app, width=30)
vcep.grid(row=5, column=1)

#rotulos para entrada
nomel = Label(app, text='Nome:')
nomel.grid(row=0, column=0)

sobrel = Label(app, text='Sobre Nome:')
sobrel.grid(row=1, column=0)

enderl = Label(app, text='Endereço:')
enderl.grid(row=2, column=0)

cidadel = Label(app, text='Cidade:')
cidadel.grid(row=3, column=0)

estadol = Label(app, text='Estado:')
estadol.grid(row=4, column=0)

cepl = Label(app, text='CEP:')
cepl.grid(row=5, column=0)

#criando botao de comando
botao1 = Button(app, text='Adicionar registro', command=gravar)
botao1.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

con.commit()
con.close()

app.mainloop()
