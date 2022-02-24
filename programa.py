class programa(object):

    def __init__(self, items):
        self.items = items

    def verifica_item(self):
        alertas = []
        for item in self.items:
            #Verifica o padrão
            padrao_item = self.qualidade_min_e_max(item)
            if padrao_item == 'Itens fora do padrão':
                alertas.append(item)
                continue
            self.identifica_item(item)
        return alertas

    #Verifica padrão de valores minimus e maximos de qualidade
    def qualidade_min_e_max(self, item):
        item_lendario = 'Sulfuras, Hand of Ragnaros'
        if item.name != item_lendario:
            if item.quality <= 50 and item.quality >= 0:
                return 'Itens dentro do padrão'
            else:
                return 'Itens fora do padrão'
        else:
            if item.quality == 80:
                return 'Itens dentro do padrão'
            else:
                return 'Itens fora do padrão'
    
    #Identifica qual o tipo do Item
    def identifica_item(self, item):
        if item.name == 'Backstage passes to a TAFKAL80ETC concert':
            return self.backstage_item(item)
        elif item.name == "Aged Brie":
            return self.aged_brie_item(item)
        elif item.name == 'Conjured Mana Cake':
            return self.conjured_item(item)
        elif item.name == 'Sulfuras, Hand of Ragnaros':
            return 'Item lendários'
        else:
            return self.common_item(item)

    
    def common_item(self, item):
        item.sell_in -= 1
        item.quality -= 1
        if item.quality < 0:
            item.quality = 0
    
    def sufuras_item(self, item):
        pass

    def conjured_item(self, item):
        item.sell_in -= 1
        item.quality -= 2

        if item.quality < 0:
            item.quality = 0

    def aged_brie_item(self, item):
        item.sell_in -= 1
        item.quality += 1

        if item.quality > 50:
            item.quality = 50

    def backstage_item(self,item): 
        item.sell_in -= 1
        
        if item.sell_in <= 5:
            item.quality += 3
        elif item.sell_in <= 10:
            item.quality += 2
        else:
            item.quality += 1

        if item.quality > 50:
            item.quality = 50
        if item.sell_in < 0:
            item.quality = 0

