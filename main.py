from tkinter import *
import requests
import json

class MovieData:

    def __init__(self):

        self.window = Tk()
        self.window.title('MoviedataTK')
        self.window.geometry('500x250+300+50')
        self.window.resizable(0,0)



        self.frame = Frame(self.window)
        self.frame.pack()

        self.texto_entrada = Entry(self.frame, font='Arial 16 ', width=32)
        self.texto_entrada.grid(row=0, column=0)

        self.botao_pesquisa = Button(self.frame, text='Pesquisar', font='Arial 15', command=self.procurar)
        self.botao_pesquisa.grid(row=0, column=1)

        self.lista = Listbox(self.window)
        self.lista.pack(fill=BOTH, expand=YES)#expand faz o elemento se expalhar por toda a tela

        self.window.mainloop()

    def procurar(self):
        try:
            requisicao = requests.get('http://www.omdbapi.com/?t='+ self.texto_entrada.get()+ '&apikey=5f14eb2d')
            dict = json.loads(requisicao.text)
            #print(dict)
            self.lista.delete(0, END)
            self.lista.insert(END, (' O titulo da obra é:  ' + dict['Title']))
            self.lista.insert(END, (' Ano da obra :  ' + dict['Year']))
            self.lista.insert(END, (' Foi lançado em :  ' + dict['Released']))
        except:
            self.lista.delete(0, END)
            self.lista.insert(END, "Obra não encotrada")


MovieData()