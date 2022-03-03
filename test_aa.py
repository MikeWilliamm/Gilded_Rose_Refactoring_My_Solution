#Testes:
#Se a função existe
#Se passa o parametro corretamente
#Se as operações e o retorno é correto.

import pytest
from program import *
from item import *
import main as ma
from items import *
import os

#Teste se path log está retornando corretamente
def teste_program_path_log():
    
    path_log_func = Programa.path()

    data_hora = str(datetime.datetime.today()).replace(':', '-').split('.')[0].replace(' ', '_')
    path = os.path.dirname(os.path.abspath(__file__))
    path_log_teste = f'{path}\logs\log_{data_hora}.txt'
    assert path_log_func == path_log_teste

def teste_program_cria_pasta():
    Programa.cria_pasta()
    path = os.path.dirname(os.path.abspath(__file__))
    list_path = os.listdir(path)
    assert 'logs' in list_path

#Teste para saber se o printa menu funciona, enviando uma lista de itens e uma mensagem para aparecer no cabeçalho
def teste_program_print_menu():
    items = [Item(name='+5 Dexterity Vest', sell_in=10, quality=50), Item(name='+5 Dexterity Vest', sell_in=10, quality=50)]
    items = Programa(items)
    items.menu('teste')
    #with pytest.raises()

#Teste verifica se a função que salva mesagem de execução no log está realmente salvando a mensagem
def teste_cria_log():
    path_log = Programa.path()
    Programa.print_msg('Teste_pyTeste')
    with open(f'{path_log}', 'r') as file: #r = leitura do arquivo
        read = file.read()
    assert 'Teste_pyTeste' in read
    
#Testa se a função está identificando corretamente a qualidade de itens
def testa__itens_com_qualidade_min0_e_max50():
    #Verifica se item está dentro do padrão de qualidade
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=50)
    padrao_item = Items.qualidade_min_e_max(items, items)
    assert padrao_item == 'Itens dentro do padrão'
    #Verifica se item está fora do padrão de qualidade
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=51)
    padrao_item = Items.qualidade_min_e_max(items, items)
    assert padrao_item == 'Itens fora do padrão'
    #Verifica se item está fora do padrão de qualidade
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=-1)
    padrao_item = Items.qualidade_min_e_max(items, items)
    assert padrao_item == 'Itens fora do padrão'

#Teste se a função está identificando corretamente a qualidade de itens lendários
def testa_itens_lendarios_com_qualidade_min0_e_max50():
    #Verifica se item lendário está dentro do padrão de qualidade
    items = Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80)
    padrao_item = Items.qualidade_min_e_max(items, items)
    assert padrao_item == 'Itens dentro do padrão'
    #Verifica se item lendário está fora do padrão de qualidade
    items = Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=81)
    padrao_item = Items.qualidade_min_e_max(items, items)
    assert padrao_item == 'Itens fora do padrão'
    #Verifica se item lendário está fora do padrão de qualidade
    items = Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=50)
    padrao_item = Items.qualidade_min_e_max(items, items)
    assert padrao_item == 'Itens fora do padrão'

#Verifica se a função identificacao existe e funciona
def testa_identificacao_dos_itens():
    items = [Item(name='+5 Dexterity Vest', sell_in=10, quality=20)]
    items = Items(items)
    items.identifica_item(items[0])

def teste_commun_items():
    items = [Item(name='+5 Dexterity Vest', sell_in=10, quality=20), 
            Item(name='+5 Dexterity Vest', sell_in=10, quality=0),
            Item(name='+5 Dexterity Vest', sell_in=10, quality=55)]
    items = Items(items)
    #teste de identificação de commun_item.
    #teste de condição de sell_in e quality receber -1.
    items.identifica_item(items[0])
    assert items[0].name == '+5 Dexterity Vest' and items[0].sell_in == 9 and items[0].quality == 19
    #teste de coreção de valor de quality nunca ser menor que 0
    items.identifica_item(items[1])
    assert items[1].name == '+5 Dexterity Vest'  and items[1].sell_in == 9 and items[1].quality == 0
    #teste de coreção de valor de quality nunca ser maior que 50
    items.identifica_item(items[2])
    assert items[2].name == '+5 Dexterity Vest'  and items[2].sell_in == 9 and items[2].quality == 50

def teste_sufuras_item():
    #teste de identificação de item lendario e de qualidade persistente
    items = [Item(name='Sulfuras, Hand of Ragnaros', sell_in=2, quality=80)]
    items = Items(items)
    items.identifica_item(items[0])
    assert items[0].name == 'Sulfuras, Hand of Ragnaros' and items[0].sell_in == 1 and items[0].quality == 80

def teste_conjured_item():
    #instanciando obj teste
    items = [Item(name='Conjured Mana Cake', sell_in=3, quality=6), 
            Item(name='Conjured Mana Cake', sell_in=3, quality=0),
            Item(name='Conjured Mana Cake', sell_in=3, quality=55)]
    items = Items(items)
    #Teste de identificação de conjured_item.
    #Teste de condição sell_in -1 e quality -2.
    items.identifica_item(items[0])
    assert items[0].name == 'Conjured Mana Cake' and  items[0].sell_in == 2 and items[0].quality == 4
    #teste de coreção de valor de quality nunca ser menor que 0
    items.identifica_item(items[1])
    assert items[1].name == 'Conjured Mana Cake' and  items[1].sell_in == 2 and items[1].quality == 0
    #teste de coreção de valor de quality nunca ser maior que 50
    items.identifica_item(items[2])
    assert items[2].name == 'Conjured Mana Cake' and  items[2].sell_in == 2 and items[2].quality == 50

def teste_aged_brie_item():
    #Instanciação de obj
    items = [Item(name='Aged Brie', sell_in=2, quality=0), 
            Item(name='Aged Brie', sell_in=2, quality=51),
            Item(name='Aged Brie', sell_in=2, quality=-2)]
    items = Items(items)
    #Teste de condição sell_in -1, quality +1
    items.identifica_item(items[0])
    assert items[0].name == 'Aged Brie' and items[0].sell_in == 1 and items[0].quality == 1
    #teste de coreção de valor de quality nunca ser maior que 50
    items.identifica_item(items[1])
    assert items[1].name == 'Aged Brie' and items[1].sell_in == 1 and items[1].quality == 50
    #teste de coreção de valor de quality nunca ser menor que 0
    items.identifica_item(items[2])
    assert items[2].name == 'Aged Brie' and items[2].sell_in == 1 and items[2].quality == 0

def teste_backstage_item():
    items = [Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=4, quality=20),
            Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=8, quality=20),
            Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=20),
            Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=51),
            Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=-2, quality=-5)]

    items = Items(items)
    #Testes das 3 condições
    #Se sell_in for <= 5, entrão quality recebe +3.
    items.identifica_item(items[0])
    assert items[0].name == 'Backstage passes to a TAFKAL80ETC concert' and items[0].sell_in == 3 and items[0].quality == 23
    #Se sell_in <= 10, então quality recebe +2
    items.identifica_item(items[1])
    assert items[1].name == 'Backstage passes to a TAFKAL80ETC concert' and items[1].sell_in == 7 and items[1].quality == 22
    #Se sell_in > 10, então quality recebe +1
    items.identifica_item(items[2])
    assert items[2].name == 'Backstage passes to a TAFKAL80ETC concert' and items[2].sell_in == 14 and items[2].quality == 21
    #Testes de coreção para qualidade maior que o permitido 50
    items.identifica_item(items[3])
    assert items[3].name == 'Backstage passes to a TAFKAL80ETC concert' and items[3].sell_in == 14 and items[3].quality == 50
    #Testes de coreção para qualidade menor que o permitido 0
    items.identifica_item(items[4])
    assert items[4].name == 'Backstage passes to a TAFKAL80ETC concert' and items[4].sell_in == -3 and items[4].quality == 0