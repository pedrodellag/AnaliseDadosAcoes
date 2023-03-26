import threading
import matplotlib.pyplot as plt
from Requests import *
from Testes import *


# Metodo que plota o grafico das ações da Intel
def mostrarGraficos1():
    graficox = []
    graficoxres = []
    graficox2 = []
    graficox2res = []
    graficox3 = []
    graficox3res = []
    graficoy = []

    # Repetiçaõ para gerar os dias
    for i in range(30):
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)

    # Recebendo os dados do request ja no formato json
    intelDaily = intelDailyRequest()
    intelMM = intelMMRequest()

    # Pegando os dados do objeto json e armazanenando em listas
    timeSeries = intelDaily['Time Series (Daily)']
    for key, value in timeSeries.items():
        for inner_key, inner_value in value.items():
            graficox.append(float(value['4. close']))
            graficox3.append(float(value['5. volume']))

    timeSeriesMM = intelMM['Technical Analysis: SMA']
    for key, value in timeSeriesMM.items():
        for inner_key, inner_value in value.items():
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))

    # Resumindo os dados
    for i in range(150):
        graficoxres.append(graficox[i])
        graficox2res.append(graficox2[i])
        graficox3res.append(graficox3[i])

    # Invertendo as listas para que fiquem na ordem correta
    graficox.reverse()
    graficox2.reverse()
    graficox3.reverse()

    # Definindo os pontos de compra e venda
    comprasy = [5.61, 7.52, 10.55, 27.46]
    comprasx = [58.07, 58.05, 58.09, 52.00]
    vendasy = [2.54, 6.70, 8.38, 13.27, 29.03]
    vendasx = [58.32, 58.05, 58.08, 57.98, 52.02]

    # Plotando os gráficos
    plt.figure()
    plt.subplot(211)
    plt.scatter(comprasy, comprasx, c='green', label='COMPRA', zorder=3, marker="^", s=69)
    plt.scatter(vendasy, vendasx, c='red', label='VENDA', zorder=3, marker="v", s=69)
    plt.plot(graficoy, graficoxres, label='Fechamento', zorder=1)
    plt.plot(graficoy, graficox2res, label='Média Móvel', zorder=2)
    plt.title('Preço das ações da INTEL')
    plt.xlabel('Dias')
    plt.ylabel('Preço ($)', labelpad=1)
    plt.legend()
    plt.subplot(212)
    plt.bar(graficoy, graficox3res, label='Volume')
    plt.xlabel('Dias')
    plt.ylabel('Volume')
    plt.legend()
    plt.show()


# Metodo que plota o grafico das ações da Amazon
def mostrarGraficos2():
    graficox = []
    graficoxres = []
    graficox2 = []
    graficox2res = []
    graficox3 = []
    graficox3res = []
    graficoy = []

    # Repetiçaõ para gerar os dias
    for i in range(30):
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)

    # Recebendo os dados do request ja no formato json
    amazonDaily = amazonDailyRequest()
    amazonMM = amazonMMRequest()

    # Pegando os dados do objeto json e armazanenando em listas
    timeSeries = amazonDaily['Time Series (Daily)']
    for key, value in timeSeries.items():
        for inner_key, inner_value in value.items():
            graficox.append(float(value['4. close']))
            graficox3.append(float(value['5. volume']))

    timeSeriesMM = amazonMM['Technical Analysis: SMA']
    for key, value in timeSeriesMM.items():
        for inner_key, inner_value in value.items():
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))

    # Resumindo os dados
    for i in range(150):
        graficoxres.append(graficox[i])
        graficox2res.append(graficox2[i])
        graficox3res.append(graficox3[i])

    # Invertendo as listas para que fiquem na ordem correta
    graficox.reverse()
    graficox2.reverse()
    graficox3.reverse()

    # Definindo os pontos de compra e venda
    comprasy = [5.96, 23.55, 25.40, 27.41]
    comprasx = [1746.56, 1770.40, 1770.76, 1773.03]
    vendasy = [17.26, 24.53, 26.58, 29.09]
    vendasx = [1790.26, 1770.62, 1773.01, 1767.73]

    # Plotando os graficos
    plt.figure()
    plt.subplot(211)
    plt.scatter(comprasy, comprasx, c='green', label='COMPRA', zorder=3, marker="^", s=69)
    plt.scatter(vendasy, vendasx, c='red', label='VENDA', zorder=3, marker="v", s=69)
    plt.plot(graficoy, graficoxres, label='Fechamento', zorder=1)
    plt.plot(graficoy, graficox2res, label='Média Móvel', zorder=2)
    plt.title('Preço das ações da AMAZON')
    plt.xlabel('Dias')
    plt.ylabel('Preço ($)', labelpad=1)
    plt.legend()

    plt.subplot(212)
    plt.bar(graficoy, graficox3res, label='Volume')
    plt.xlabel('Dias')
    plt.ylabel('Volume')
    plt.legend()
    plt.show()


# Metodo que plota o grafico das ações da Sony
def mostrarGraficos3():
    graficox = []
    graficoxres = []
    graficox2 = []
    graficox2res = []
    graficox3 = []
    graficox3res = []
    graficoy = []

    # Repetiçaõ para gerar os dias
    for i in range(30):
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)

    # Recebendo os dados do request ja no formato json
    sonyDaily = sonyDailyRequest()
    sonyMM = sonyMMRequest()

    # Pegando os dados do objeto json e armazanenando em listas
    timeSeries = sonyDaily['Time Series (Daily)']
    for key, value in timeSeries.items():
        for inner_key, inner_value in value.items():
            graficox.append(float(value['4. close']))
            graficox3.append(float(value['5. volume']))

    timeSeriesMM = sonyMM['Technical Analysis: SMA']
    for key, value in timeSeriesMM.items():
        for inner_key, inner_value in value.items():
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))

    # Resumindo os dados
    for i in range(150):
        graficoxres.append(graficox[i])
        graficox2res.append(graficox2[i])
        graficox3res.append(graficox3[i])

    # Invertendo as listas para que fiquem na ordem correta
    graficox.reverse()
    graficox2.reverse()
    graficox3.reverse()

    # Definindo os pontos de compra e venda
    comprasy = [5.04, 15.51, 25.26]
    comprasx = [61.77, 61.04, 58.91]
    vendasy = [9.19, 18.16, 28.96]
    vendasx = [62.03, 60.87, 58.96]

    # Plotando os graficos
    plt.figure()
    plt.subplot(211)
    plt.scatter(comprasy, comprasx, c='green', label='COMPRA', zorder=3, marker="^", s=69)
    plt.scatter(vendasy, vendasx, c='red', label='VENDA', zorder=3, marker="v", s=69)
    plt.plot(graficoy, graficoxres, label='Fechamento', zorder=1)
    plt.plot(graficoy, graficox2res, label='Média Móvel', zorder=2)
    plt.title('Preço das ações da SONY')
    plt.xlabel('Dias')
    plt.ylabel('Preço ($)', labelpad=1)
    plt.legend()

    plt.subplot(212)
    plt.bar(graficoy, graficox3res, label='Volume')
    plt.xlabel('Dias')
    plt.ylabel('Volume')
    plt.legend()
    plt.show()


# Metodo que plota o grafico das ações da Nvidia
def mostrarGraficos4():
    graficox = []
    graficoxres = []
    graficox2 = []
    graficox2res = []
    graficox3 = []
    graficox3res = []
    graficoy = []

    # Repetiçaõ para gerar os dias
    for i in range(30):
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)
        graficoy.append(i + 1)

    # Recebendo os dados do request ja no formato json
    nvidiaDaily = nvidiaDailyRequest()
    nvidiaMM = nvidiaMMRequest()

    # Pegando os dados do objeto json e armazanenando em listas
    timeSeries = nvidiaDaily['Time Series (Daily)']
    for key, value in timeSeries.items():
        for inner_key, inner_value in value.items():
            graficox.append(float(value['4. close']))
            graficox3.append(float(value['5. volume']))

    timeSeriesMM = nvidiaMM['Technical Analysis: SMA']
    for key, value in timeSeriesMM.items():
        for inner_key, inner_value in value.items():
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))
            graficox2.append(float(value['SMA']))

    # Resumindo os dados
    for i in range(150):
        graficoxres.append(graficox[i])
        graficox2res.append(graficox2[i])
        graficox3res.append(graficox3[i])

    # Invertendo as listas para que fiquem na ordem correta
    graficox.reverse()
    graficox2.reverse()
    graficox3.reverse()

    # Definindo os pontos de compra e venda
    comprasy = [8.74, 10.48, 21.11]
    comprasx = [208.85, 208.35, 202.43]
    vendasy = [1.76, 9.15, 11.75, 22.15]
    vendasx = [215.02, 208.67, 208.45, 201.34]

    # Plotando os graficos
    plt.figure()
    plt.subplot(211)
    plt.scatter(comprasy, comprasx, c='green', label='COMPRA', zorder=3, marker="^", s=69)
    plt.scatter(vendasy, vendasx, c='red', label='VENDA', zorder=3, marker="v", s=69)
    plt.plot(graficoy, graficoxres, label='Fechamento', zorder=1)
    plt.plot(graficoy, graficox2res, label='Média Móvel', zorder=2)
    plt.title('Preço das ações da NVIDIA')
    plt.xlabel('Dias')
    plt.ylabel('Preço ($)', labelpad=1)
    plt.legend()

    plt.subplot(212)
    plt.bar(graficoy, graficox3res, label='Volume')
    plt.xlabel('Dias')
    plt.ylabel('Volume')
    plt.legend()
    plt.show()


# Metodos para ganhar tempo e conseguir fazer as requests
def mostrarGraficos11():
    t1 = threading.Timer(30.0, mostrarGraficos1)
    t1.start()


def mostrarGraficos12():
    t2 = threading.Timer(30.0, mostrarGraficos2)
    t2.start()


def mostrarGraficos13():
    t3 = threading.Timer(30.0, mostrarGraficos3)
    t3.start()


def mostrarGraficos14():
    t4 = threading.Timer(30.0, mostrarGraficos4)
    t4.start()


# Inicia o programa e o menu principal
janelaPrincipal = Tk()
janelaPrincipal.geometry('300x400')
textoMenu = Label(janelaPrincipal, text='MENU PRINCIPAL')
textoMenu.pack(pady=15, side=TOP)
grafico01 = Button(janelaPrincipal, text='AÇÕES INTEL', command=lambda: mostrarGraficos11())
grafico01.pack(pady=15, side=TOP)
grafico02 = Button(janelaPrincipal, text='AÇÕES AMAZON', command=lambda: mostrarGraficos12())
grafico02.pack(pady=15, side=TOP)
grafico03 = Button(janelaPrincipal, text='AÇÕES SONY', command=lambda: mostrarGraficos13())
grafico03.pack(pady=15, side=TOP)
grafico04 = Button(janelaPrincipal, text='AÇÕES NVIDIA', command=lambda: mostrarGraficos14())
grafico04.pack(pady=15, side=TOP)
botaoTestes = Button(janelaPrincipal, text='RELATÓRIOS', command=lambda: mostrarTestes())
botaoTestes.pack(pady=15, side=TOP)
janelaPrincipal.mainloop()
