from .menu import AVAILABLE_MENU

table_tab = []
def get_item(item_id: int):
    res = [x for x in AVAILABLE_MENU if x["id"] == item_id] 

    if bool(res) == False:
        return None
    else:
        return res


def add_item_to_tab(table_tab, item_id: int, amount: float):
    item = get_item(item_id)

    if(bool(item) == False):
        return False
    else:
        newItems = dict(id=item[0]["id"], name=item[0]["name"], price=item[0]["price"], amount=amount)
        table_tab.append(newItems)
        return True


def calculate_tab(table_tab):
    res = 0

    for x in table_tab:
        if bool(x["price"]):
            res += x["price"] * x["amount"]
    
    return "{:.2f}".format(res)





