import os
import datetime
class Programa(list):
        
        def __init__(self, items):
        #Herdando construtores da lista de objetos
            super().__init__(items)

        def cria_pasta():
            try:
                os.mkdir('./logs')
            except Exception as error:
                pass
        
        #printa menu
        def menu(self, msg):
            Programa.print_msg('-='*30)
            Programa.print_msg(f'{msg}'.center(60))
            Programa.print_msg('-='*30)

            Programa.print_msg(f"{'name':<45}{'sellIn':>6}  {'quality':>7}")
            Programa.print_msg('-'*60)
            for item in self:
               Programa.print_msg(f"{item.name:<45}{item.sell_in:>6}  {item.quality:>7}")
            Programa.print_msg("")

        #Salva Log de execução
        def print_msg(msg):
            with open(f'{Programa.path()}', 'a+') as file:
                file.write(f'{msg}\n')
                print(msg)
                
        def path():
            data_hora = str(datetime.datetime.today()).replace(':', '-').split('.')[0].replace(' ', '_')
            log_path = f'{os.path.dirname(os.path.abspath(__file__))}\logs\log_{data_hora}.txt'
            return log_path
        

    
