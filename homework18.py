import osa
import os

client_1 = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
client_2 = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
client_3 = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
current_dir = os.path.dirname(os.path.abspath(__file__))

def temperature_convert(current_dir):
    with open(os.path.join(current_dir, 'temps.txt')) as f:
        temps = []
        for line in f:
            temps.append(int(line.strip().split(' F')[0]))
    convert_temps = []
    for temp in temps:
        convert_temps.append(client_1.service.ConvertTemp(temp, 'degreeFahrenheit', 'degreeCelsius'))
    return round(sum(convert_temps)/len(convert_temps), 2)

def convert_currencies(current_dir):
    with open(os.path.join(current_dir, 'currencies.txt')) as f:
        currencies = []
        for line in f:
            currencies.append(line.strip().split(' '))
    convert_currencies = []
    i = 0
    while i < len(currencies):
        convert_currencies.append(client_2.service.ConvertToNum('', currencies[i][2], 'RUB', int(currencies[i][1]), True))
        i += 1
    return round(sum(convert_currencies), 0)    

def convert_ways(current_dir):
    with open(os.path.join(current_dir, 'travel.txt')) as f:
        ways = []
        for line in f:
            ways.append(''.join(line.strip().split(' ')[1].split(',')))
    convert_ways = []
    i = 0
    while i < len(ways):
        convert_ways.append(client_3.service.ChangeLengthUnit(float(ways[i]), 'Miles', 'Kilometers'))
        i += 1
    return round(sum(convert_ways), 2)


print('Cредняя за неделю арифметическая температура по Цельсию:',
      temperature_convert(current_dir))
print('Траты на путешествие в рублях: ',
      convert_currencies(current_dir))
print('Cуммарное расстояние пути в километрах с точностью до сотых: ',
      convert_ways(current_dir))