from program import *
from item import *
from items import *

try:
    #Cria pasta para armazenar log.
    Programa.cria_pasta()

    #Instancia lista de obj's / não pode mudar
    items = [
                Item(name='+5 Dexterity Vest', sell_in=10, quality=20),
                Item(name='Aged Brie', sell_in=2, quality=0),
                Item(name='Elixir of the Mongoose', sell_in=5, quality=7),
                Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80),
                Item(name='Sulfuras, Hand of Ragnaros', sell_in=-1, quality=81),
                Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=20),
                Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=10, quality=49),
                Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=5, quality=55),
                Item(name='Conjured Mana Cake', sell_in=3, quality=6)  # <-- :O
            ]

    items = Items(items)
    programa = Programa(items)
    days = 5
    alertas = []
    for day in range(days+1):
        programa.menu(f'Day {day}')
        for item in items:
            #Verifica o padrão
            padrao_item = items.qualidade_min_e_max(item)
            if padrao_item == 'Itens fora do padrão':
                alertas.append(item) if item not in alertas else ''
                continue
            items.identifica_item(item)

    if len(alertas) > 0:
        Programa.menu(alertas, 'Alertas')
except Exception as erro:
    Programa.print_msg(f'ERRO >> {erro}')

    



