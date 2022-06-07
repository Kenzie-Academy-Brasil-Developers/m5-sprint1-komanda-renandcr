import os
from pickle import FALSE
from .management import add_item_to_tab
from .menu import AVAILABLE_MENU
from .management import calculate_tab

table_tab = []

def initial_screen():
    while True:
        print("\n1. Adicionar item a comanda")
        print("2. Fechar comanda")

        response = input("Digite o que deseja fazer: ")

        if response == "1":
            os.system("clear")
            add_item_screen()
        elif response == "2":
            os.system("clear")
            check_out_screen()
        elif response != "1" and response != "2":
            os.system("clear")
            print("Digite uma opção válida (1 ou 2)")



def add_item_screen():
    while True:
        id_item = input("\nDigite o id do item: ")
        amount = input("Digite a quantidade desejada: ")

        if str.isdigit(id_item) == False or str.isdigit(amount) == False:
            os.system("clear")
            print("Digite apenas números neste campo")
        elif bool(add_item_to_tab(table_tab, int(id_item), int(amount))):
            name = ""
            for x in AVAILABLE_MENU: 
                if x["id"] == int(id_item):
                    name = x["name"]
                    os.system("clear")
                    print(f'{amount} {name} adicionados(s) a comanda!')
                    initial_screen()                    
        else:
            os.system("clear")
            print(f'{id_item} não é um id de item válido')
        
        
def check_out_screen():
    while True:
        for x in table_tab:
            print(f'Item {table_tab.index(x) + 1}: {x["amount"]} {x["name"]} - R${"{:.2f}".format(x["price"])}')
    
        print("=" *50)
        print(f'Total: R${calculate_tab(table_tab)}')
        print("\nDigite F para finalizar o sistema ")
        response = input()
        
        if response.upper() == "F":
            os.system("clear")
            table_tab.clear()
            break
        else:
            os.system("clear")
            continue

    
