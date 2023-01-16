from tkinter import *
import random
import time 

def sorteio():
    lista = ['abacaxi', 'pera', 'bola', 'azeitona', 'garrafa', 'girafa', 'touro', 'morango', 'mix', 'caneta']
    index = random.randint(0, len(lista) -1)
    return lista[index]
ppmn = 0
def ppm():
    global ppmn
    ppmn = ppmn  + 1
    print(ppmn)
    if ppmn == 10:
        calcTempo(ppmn)
def trocarPalavra(event):
    if entryWord.get() == palavraSorteada['text']:
        ppm()
        print(palavraSorteada['text'])
        print(entryWord.get())
        entryWord.delete(0, END)
        palavraSorteada['text'] = ' '+sorteio()
    else:
        entryWord.delete(0,END)
        palavraSorteada['text'] = ' '+sorteio()
        print('erro')

tempo_inicial = time.time()
def calcTempo(p):
    global tempo_inicial
    tempo_final = time.time()
    tempo = int(tempo_final) - int(tempo_inicial)
    labelPpm['text'] = 'PPM: ', tempo / p * 60
    global ppmn
    ppmn = 0
    tempo_inicial = time.time()
def iniciar():
    entryWord.delete(0,END)
    palavraSorteada['text'] = sorteio()
    entryWord.bind("<space>", trocarPalavra)




window = Tk()
window.title('Tela inicial')
window.geometry('1000x300')
window.resizable(0,0)
window.config(bg='black')

frameMenu = Frame(window, bg='#778899', width=300, height=290)
frameMenu.place(x=5,y=5)
labelTitulo = Label(frameMenu, text='Typing Test',bg='black', fg='green',width=19, font='Ivy 20')
labelTitulo.bind('<Leave>', lambda e: labelTitulo.configure(font="Ivy 23", width=18))
labelTitulo.bind('<Enter>', lambda e: labelTitulo.configure(font="Ivy 20", width=19))
labelTitulo.place(x=0,y=30)
labelPpm = Label(frameMenu, text='PPM:',bg='#778899', fg='white', font='Ivy 18')
labelPpm.place(x=20,y=90)
btmInit = Button(frameMenu, text='INICIAR',font='Arial 14 bold', command=lambda:iniciar())
btmInit.place(x=100,y=190)

frameGame = Frame(window, bg='#778899', width=690, height=290)
frameGame.place(x=310,y=5)
palavraSorteada = Label(frameGame, text='Typing Test',bg='#c9c9c9', fg='green',width=33, font='Ivy 27')
palavraSorteada.place(x=0,y=30)
entryWord = Entry(frameGame, width=25, font='ivy 24')
entryWord.place(x=120, y=120)

window.mainloop()
    

