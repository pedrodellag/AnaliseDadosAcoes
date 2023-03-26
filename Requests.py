import requests


# Metodo que retorna um objeto json com os dados sobre a timeseries da Intel
def intelDailyRequest():
    intelResponse = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=INTC&apikey'
                                 '=TXH1J76KFHUZPOET')
    intelDaily = intelResponse.json()
    arq = open('arquivos\IntelDaily.json', 'w')
    intelDailyStr = str(intelDaily)
    arq.write(intelDailyStr)
    arq.close()
    return intelDaily


# Metodo que retorna um objeto json com as medias moveis da Intel
def intelMMRequest():
    intelMMResponse = requests.get('https://www.alphavantage.co/query?function=SMA&symbol=INTC&interval=daily'
                                   '&time_period=7&series_type=close&apikey=TXH1J76KFHUZPOET')
    intelMM = intelMMResponse.json()
    arq = open('arquivos\IntelMM.json', 'w')
    intelMMStr = str(intelMM)
    arq.write(intelMMStr)
    arq.close()
    return intelMM


# Metodo que retorna um objeto json com os dados sobre a timeseries da Amazon
def amazonDailyRequest():
    amazonResponse = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AMZN&apikey'
                                  '=TXH1J76KFHUZPOET')
    amazonDaily = amazonResponse.json()
    arq = open('arquivos\AmazonDaily.json', 'w')
    amazonDailyStr = str(amazonDaily)
    arq.write(amazonDailyStr)
    arq.close()
    return amazonDaily


# Metodo que retorna um objeto json com as medias moveis da Amazon
def amazonMMRequest():
    amazonMMResponse = requests.get('https://www.alphavantage.co/query?function=SMA&symbol=AMZN&interval=daily'
                                    '&time_period=7&series_type=close&apikey=TXH1J76KFHUZPOET')
    amazonMM = amazonMMResponse.json()
    arq = open('arquivos\AmazonMM.json', 'w')
    amazonMMStr = str(amazonMM)
    arq.write(amazonMMStr)
    arq.close()
    return amazonMM


# Metodo que retorna um objeto json com os dados sobre a timeseries da Sony
def sonyDailyRequest():
    sonyResponse = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=SNE&apikey'
                                '=TXH1J76KFHUZPOET')
    sonyDaily = sonyResponse.json()
    arq = open('arquivos\SonyDaily.json', 'w')
    sonyDailyStr = str(sonyDaily)
    arq.write(sonyDailyStr)
    arq.close()
    return sonyDaily


# Metodo que retorna um objeto json com as medias moveis da Sony
def sonyMMRequest():
    sonyMMResponse = requests.get('https://www.alphavantage.co/query?function=SMA&symbol=SNE&interval=daily'
                                  '&time_period=7&series_type=close&apikey=TXH1J76KFHUZPOET')
    sonyMM = sonyMMResponse.json()
    arq = open('arquivos\SonyMM.json', 'w')
    sonyMMStr = str(sonyMM)
    arq.write(sonyMMStr)
    arq.close()
    return sonyMM


# Metodo que retorna um objeto json com os dados sobre a timeseries da Nvidia
def nvidiaDailyRequest():
    nvidiaResponse = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDA&apikey'
                                  '=TXH1J76KFHUZPOET')
    nvidiaDaily = nvidiaResponse.json()
    arq = open('arquivos\MvidiaDaily.json', 'w')
    nvidiaDailyStr = str(nvidiaDaily)
    arq.write(nvidiaDailyStr)
    arq.close()
    return nvidiaDaily


# Metodo que retorna um objeto json com as medias moveis da Nvidia
def nvidiaMMRequest():
    nvidiaMMResponse = requests.get('https://www.alphavantage.co/query?function=SMA&symbol=NVDA&interval=daily'
                                    '&time_period=7&series_type=close&apikey=TXH1J76KFHUZPOET')
    nvidiaMM = nvidiaMMResponse.json()
    arq = open('arquivos\MvidiaMM.json', 'w')
    nvidiaMMStr = str(nvidiaMM)
    arq.write(nvidiaMMStr)
    arq.close()
    return nvidiaMM
