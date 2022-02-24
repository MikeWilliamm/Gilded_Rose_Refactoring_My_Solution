from item import *
from programa import *
import os
import datetime

path = os.path.dirname(os.path.abspath(__file__)) + '//logs'
data_hora = str(datetime.datetime.today()).replace(':', '-').split('.')[0]
#Salva Log de execução
def print_msg(msg):
    with open(f'{path}//log_{data_hora}.txt', 'a+') as file:
        file.write(f'{msg}\n')
        print(msg)
    
#printa menu
def menu(items, msg, param = 'Vazio'):
    print_msg('-='*30)
    if param == 'Vazio':
        print_msg(f'{msg}'.center(60))
    else:
        print_msg(f'{msg} {param}'.center(60))
    print_msg('-='*30)

    print_msg(f"{'name':<45}{'sellIn':>6}  {'quality':>7}")
    print_msg('-'*60)
    for item in items:
        print_msg(f"{item.name:<45}{item.sell_in:>6}  {item.quality:>7}")
    print_msg("")

#Constroi lista de objetos
items = [
            Item(name='+5 Dexterity Vest', sell_in=10, quality=20),
            Item(name='Aged Brie', sell_in=2, quality=0),
            Item(name='Elixir of the Mongoose', sell_in=5, quality=7),
            Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80),
            Item(name='Sulfuras, Hand of Ragnaros', sell_in=-1, quality=80),
            Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=20),
            Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=10, quality=49),
            Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=5, quality=49),
            Item(name='Conjured Mana Cake', sell_in=3, quality=6)  # <-- :O
        ]
#Envia os items para a classe programa
days = 5
for day in range(days+1):
    menu(items, 'day', day)
    alertas = programa(items).verifica_item()

#Se existir itens fora do padrão de qualidade imprime os alertas
if len(alertas) > 0:
    menu(alertas, 'Alertas')

    

    