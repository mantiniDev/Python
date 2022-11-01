from tkinter import*
from tkinter import messagebox
import os


#define caminho do arquivo texto
c = os.path.dirname(__file__)

#cria o arquivo texto
arqtext = c+'\\dados.txt'

def botao():
    arquivo = open(arqtext, 'a')
    arquivo.write('Nome......: %s'% vnome.get())
    arquivo.write('\nTelefone..: %s'% vtelef.get())
    arquivo.write('\nE-mail....: %s'% vemail.get())
    arquivo.write('\nObservação: %s'% vobs.get(1.0, END))
    arquivo.write('\n')
    arquivo.close()
    
    messagebox.showinfo('MENSAGEM IMPORTANTE', 'Informações Gravadas com sucesso!')
    
    #limpa campos
    vnome.delete(0,END)
    vtelef.delete(0,END)
    vemail.delete(0,END)
    vobs.delete(1.0,END)
    #direciona o foco de entrada para VNOME
    Entry.focus(vnome)   
   
    
#criando janela

app = Tk()
app.title('Curso de RAD em Python') #Define o Título
app.geometry('500x350')#Define o Tamanho da Janela
app.configure(background ='light grey') #define cor de fundo

Label(app, text='Nome', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=10, width=100, height=20)
vnome = Entry(app)
vnome.place(x =10, y=30, width=200, height=20)

Label(app, text='Telefone', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=60, width=100, height=20)
vtelef = Entry(app)
vtelef.place(x =10, y=80, width=100, height=20)

Label(app, text='E-mail', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=110, width=100, height=20)
vemail = Entry(app)
vemail.place(x =10, y=130, width=250, height=20)

Label(app, text='Observação', background='light grey', foreground='midnight blue', anchor=W).place(x=10, y=160, width=100, height=20)
vobs = Text(app)
vobs.place(x =10, y=180, width=300, height=80)

Button(app, text='Gravar', command=botao).place(x=10, y=270, width=100, height=30)




    

#execute aqui
app.mainloop()