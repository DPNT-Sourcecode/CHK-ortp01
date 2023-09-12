

# noinspection PyUnusedLocal
# skus = unicode string

SKUS = {
    "A": {"price" : 50, "offer_price" : 130, "offer_qty": 3},
    "B": {"price" : 30, "offer_price" : 45, "offer_qty": 2},
    "C": {"price" : 20},
    "D": {"price" : 15}
}

def checkout(skus):


    if skus == "": 
        return -1
    if isinstance(skus[0], int):

    else:
        print(f"SKUs in basket: {skus}")

    
    raise NotImplementedError()


