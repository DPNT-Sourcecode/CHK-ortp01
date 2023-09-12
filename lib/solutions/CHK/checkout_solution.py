

# noinspection PyUnusedLocal
# skus = unicode string

SKUS = {
    "A": {"price" : 50, "offer_price" : 130, "offer_qty": 3},
    "B": {"price" : 30, "offer_price" : 45, "offer_qty": 2},
    "C": {"price" : 20},
    "D": {"price" : 15}
}

def checkout(skus):

    total = 0:

    for sku in skus:

        if skus == "": 
            total = -1
        elif isinstance(skus[0], int):
            if skus[0] == SKUS[sku].get('offer_qty'):
                total += SKUS[sku].get('offer_price', -1)
        else:
            total += SKUS[sku].get('price', -1)

    return total





