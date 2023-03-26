from tkinter import *


def mostrarTestes():
    janelaTestes = Tk()
    janelaTestes.geometry('300x400')
    teste01 = Button(janelaTestes, text='TESTE DE INVESTIMENTO INTEL', command=lambda: mostrarTeste1())
    teste01.pack(pady=15, side=TOP)
    teste02 = Button(janelaTestes, text='TESTE DE INVESTIMENTO AMAZON', command=lambda: mostrarTeste2())
    teste02.pack(pady=15, side=TOP)
    teste03 = Button(janelaTestes, text='TESTE DE INVESTIMENTO SONY', command=lambda: mostrarTeste3())
    teste03.pack(pady=15, side=TOP)
    teste04 = Button(janelaTestes, text='TESTE DE INVESTIMENTO NVIDIA', command=lambda: mostrarTeste4())
    teste04.pack(pady=15, side=TOP)


# Metodo para printar um relatorio sobre a estrategia de investimento na empresa Intel
def mostrarTeste1():
    janelaTesteIntel = Tk()
    janelaTesteIntel.geometry('300x400')
    textoTeste0 = Label(janelaTesteIntel, text='TESTE DE INVESTIMENTO INTEL')
    textoTeste0.pack(pady=15, side=TOP)
    textoTeste1 = Label(janelaTesteIntel, text='Comprado por 58.07 e vendido por 58.05, Saldo = -0.02')
    textoTeste1.pack(pady=15, side=TOP)
    textoTeste2 = Label(janelaTesteIntel, text='Comprado por 58.05 e vendido por 58.08, Saldo = 0')
    textoTeste2.pack(pady=15, side=TOP)
    textoTeste3 = Label(janelaTesteIntel, text='Comprado por 58.09 e vendido por 57.98, Saldo = -0.11')
    textoTeste3.pack(pady=15, side=TOP)
    textoTeste4 = Label(janelaTesteIntel, text='Comprado por 52.00 e vendido por 52.02, Saldo = 0.02')
    textoTeste4.pack(pady=15, side=TOP)
    textoTeste5 = Label(janelaTesteIntel, text='SALDO TOTAL = -0.11')
    textoTeste5.pack(pady=15, side=TOP)
    janelaTesteIntel.mainloop()


# Metodo para printar um relatorio sobre a estrategia de investimento na empresa Amazon
def mostrarTeste2():
    janelaTesteAmazon = Tk()
    janelaTesteAmazon.geometry('300x400')
    textoTeste0 = Label(janelaTesteAmazon, text='TESTE DE INVESTIMENTO AMAZON')
    textoTeste0.pack(pady=15, side=TOP)
    textoTeste1 = Label(janelaTesteAmazon, text='Comprado por 1746.56 e vendido por 1790.26, Saldo = 43.70 ')
    textoTeste1.pack(pady=15, side=TOP)
    textoTeste2 = Label(janelaTesteAmazon, text='Comprado por  1770.40 e vendido por 1770.62, Saldo = 0.22')
    textoTeste2.pack(pady=15, side=TOP)
    textoTeste3 = Label(janelaTesteAmazon, text='Comprado por 1770.76 e vendido por 1773.01, Saldo = 2.25')
    textoTeste3.pack(pady=15, side=TOP)
    textoTeste4 = Label(janelaTesteAmazon, text='Comprado por 1773.03 e vendido por 1767.73, Saldo = -5.30')
    textoTeste4.pack(pady=15, side=TOP)
    textoTeste5 = Label(janelaTesteAmazon, text='SALDO TOTAL = 40.87')
    textoTeste5.pack(pady=15, side=TOP)
    janelaTesteAmazon.mainloop()


# Metodo para printar um relatorio sobre a estrategia de investimento na empresa Sony
def mostrarTeste3():
    janelaTesteSony = Tk()
    janelaTesteSony.geometry('300x400')
    textoTeste0 = Label(janelaTesteSony, text='TESTE DE INVESTIMENTO AMAZON')
    textoTeste0.pack(pady=15, side=TOP)
    textoTeste1 = Label(janelaTesteSony, text='Comprado por 61.77 e vendido por 62.03, Saldo = 0.26')
    textoTeste1.pack(pady=15, side=TOP)
    textoTeste2 = Label(janelaTesteSony, text='Comprado por 61.04 e vendido por 60.87, Saldo = -0.17')
    textoTeste2.pack(pady=15, side=TOP)
    textoTeste3 = Label(janelaTesteSony, text='Comprado por 58.91 e vendido por 58.96, Saldo = 0.05')
    textoTeste3.pack(pady=15, side=TOP)
    textoTeste5 = Label(janelaTesteSony, text='SALDO TOTAL = 0.14')
    textoTeste5.pack(pady=15, side=TOP)
    janelaTesteSony.mainloop()


# Metodo para printar um relatorio sobre a estrategia de investimento na empresa Nvidia
def mostrarTeste4():
    janelaTesteNvidia = Tk()
    janelaTesteNvidia.geometry('300x400')
    textoTeste0 = Label(janelaTesteNvidia, text='Comprado por 208.85 e vendido por 208.67, Saldo = -0.15')
    textoTeste0.pack(pady=15, side=TOP)
    textoTeste1 = Label(janelaTesteNvidia, text='Comprado por 208.35 e vendido por 208.45, Saldo = 0.10')
    textoTeste1.pack(pady=15, side=TOP)
    textoTeste2 = Label(janelaTesteNvidia, text='Comprado por 202.43 e vendido por 201.34, Saldo = -1.09')
    textoTeste2.pack(pady=15, side=TOP)
    textoTeste3 = Label(janelaTesteNvidia, text='SALDO TOTAL = -1.14')
    textoTeste3.pack(pady=15, side=TOP)
    janelaTesteNvidia.mainloop()
