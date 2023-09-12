

# noinspection PyUnusedLocal
# skus = unicode string

SKUS = {
    "A": {"price" : 50, "offer_price" : 130, "offer_qty": 3},
    "B": {"price" : 30, "offer_price" : 45, "offer_qty": 2},
    "C": {"price" : 20},
    "D": {"price" : 15}
}

def checkout(skus):

    total = 0
    counts = {}

    for sku in skus:
        if sku in counts: 
            counts[sku] += 1
        else:
            counts[sku] = 1

    for sku, qty in counts.items():

        if skus in SKUS.keys():
            if SKUS[sku].get('offer_qty') == qty:
                total += SKUS[sku].get('offer_price')
        else:
            total += SKUS[sku].get('price') * qty

    return total






