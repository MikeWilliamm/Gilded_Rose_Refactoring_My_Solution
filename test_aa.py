#Testes:
#Se a função existe
#Se passa o parametro corretamente
#Se as operações e o retorno é correto.

import pytest
from programa import *
from item import *
import main as ma

#Testa se a função existe e a sua passagem de parametro 
def testa_menu():
    ma.menu(ma.items, 'teste')

def testa_salva_log():
    ma.print_msg('Teste')

#Teste do retorno da função verifica_item
def testa_verifica_item():
    #Verifica item sem erro
    items = [Item(name='+5 Dexterity Vest', sell_in=10, quality=20)]
    alertas = programa(items).verifica_item()
    assert alertas == []
    #Verifica item com erro 
    items = [Item(name='+5 Dexterity Vest', sell_in=10, quality=51)]
    alertas = programa(items).verifica_item()
    assert alertas == items
    #Verifica item lendário sem erro
    items = [Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80)]
    alertas = programa(items).verifica_item()
    assert alertas == []
    #Verifica item lendário com erro
    items = [Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=81)]
    alertas = programa(items).verifica_item()
    assert alertas == items
    
#Testa se a função está identificando corretamente a qualidade de itens
def testa__itens_com_qualidade_min0_e_max50():
    #Verifica se item está dentro do padrão de qualidade
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=20)
    dentro_do_padrao = programa(items).qualidade_min_e_max(items)
    assert dentro_do_padrao == 'Itens dentro do padrão'
    #Verifica se item está fora do padrão de qualidade
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=51)
    fora_do_padrao = programa(items).qualidade_min_e_max(items)
    assert fora_do_padrao == 'Itens fora do padrão'
    #Verifica se item está fora do padrão de qualidade
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=-1)
    fora_do_padrao = programa(items).qualidade_min_e_max(items)
    assert fora_do_padrao == 'Itens fora do padrão'

#Teste se a função está identificando corretamente a qualidade de itens lendários
def testa_itens_lendarios_com_qualidade_min0_e_max50():
    #Verifica se item lendário está dentro do padrão de qualidade
    items = Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80)
    dentro_do_padrao = programa(items).qualidade_min_e_max(items)
    assert dentro_do_padrao == 'Itens dentro do padrão'
    #Verifica se item lendário está fora do padrão de qualidade
    items = Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=81)
    fora_do_padrao = programa(items).qualidade_min_e_max(items)
    assert fora_do_padrao == 'Itens fora do padrão'
    #Verifica se item lendário está fora do padrão de qualidade
    items = Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=50)
    fora_do_padrao = programa(items).qualidade_min_e_max(items)
    assert fora_do_padrao == 'Itens fora do padrão'

def testa_identificacao_dos_itens():
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=20)
    programa(items).identifica_item(items)

def teste_commun_items():
    #teste de condição
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=20)
    programa(items).common_item(items)
    assert items.name == '+5 Dexterity Vest' and items.sell_in == 9 and items.quality == 19
    #teste de coreção de valor
    items = Item(name='+5 Dexterity Vest', sell_in=10, quality=0)
    programa(items).common_item(items)
    assert items.name == '+5 Dexterity Vest'  and items.sell_in == 9 and items.quality == 0

def teste_sufuras_item():
    #teste de qualidade persistente
    items = Item(name='Sulfuras, Hand of Ragnaros', sell_in=0, quality=80)
    programa(items).sufuras_item(items)
    assert items.name == 'Sulfuras, Hand of Ragnaros' and items.quality == 80

def teste_conjured_item():
    #teste de condição
    items = Item(name='Conjured Mana Cake', sell_in=3, quality=6) 
    programa(items).conjured_item(items)
    assert items.name == 'Conjured Mana Cake' and  items.sell_in == 2 and items.quality == 4
    #teste de coreção
    items = Item(name='Conjured Mana Cake', sell_in=3, quality=0) 
    programa(items).conjured_item(items)
    assert items.name == 'Conjured Mana Cake' and  items.sell_in == 2 and items.quality == 0

def teste_aged_brie_item():
    #Teste de condição
    items = Item(name='Aged Brie', sell_in=2, quality=0)
    programa(items).aged_brie_item(items)
    assert items.name == 'Aged Brie' and items.sell_in == 1 and items.quality == 1
    #Teste de coreção de valor
    items = Item(name='Aged Brie', sell_in=2, quality=51)
    programa(items).aged_brie_item(items)
    assert items.name == 'Aged Brie' and items.sell_in == 1 and items.quality == 50

def teste_backstage_item():
    #Testes das 3 condições
    #sell_in <= 5
    items = Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=4, quality=20)
    programa(items).backstage_item(items)
    assert items.name == 'Backstage passes to a TAFKAL80ETC concert' and items.sell_in == 3 and items.quality == 23
    #sell_in <= 10
    items = Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=8, quality=20)
    programa(items).backstage_item(items)
    assert items.name == 'Backstage passes to a TAFKAL80ETC concert' and items.sell_in == 7 and items.quality == 22
    #sell_in > 10
    items = Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=20)
    programa(items).backstage_item(items)
    assert items.name == 'Backstage passes to a TAFKAL80ETC concert' and items.sell_in == 14 and items.quality == 21
    
    #Testes de coreção para qualidade maior que o permitido
    items = Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=15, quality=51)
    programa(items).backstage_item(items)
    assert items.name == 'Backstage passes to a TAFKAL80ETC concert' and items.sell_in == 14 and items.quality == 50

    #Testes de coreção para qualidade menor que o permitido
    items = Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in=-2, quality=-5)
    programa(items).backstage_item(items)
    assert items.name == 'Backstage passes to a TAFKAL80ETC concert' and items.sell_in == -3 and items.quality == 0