

# noinspection PyUnusedLocal
# skus = unicode string

SKUS = {
    "A": {"price" : 50, "offer_price" : 130, "offer_qty": 3},
    "B": {"price" : 30, "offer_price" : 45, "offer_qty": 2},
    "C": {"price" : 20},
    "D": {"price" : 15}
}

def checkout(skus):
    print(skus)
    total = 0
    counts = {}

    for sku in skus:
        if sku in counts: 
            counts[sku] += 1
        else:
            counts[sku] = 1

    for sku, qty in counts.items():
        print(f'sku: {sku}, qty: {qty}')
        if sku in SKUS.keys():
            if SKUS[sku].get('offer_qty'):
                if qty >= SKUS[sku].get('offer_qty',0) :
                    offers = int(qty / SKUS[sku].get('offer_qty',0))
                    print(f'offers: {offers}')
                    total += SKUS[sku].get('offer_price', 0) * offers
                    print(f'offer: {qty}{sku} : {total}')
                    remainder = qty - (SKUS[sku].get('offer_qty',0) * offers)
                    print(f"remainder: {remainder}")
                    total += remainder * SKUS[sku].get('price')
                else: 
                    total += SKUS[sku].get('price') * qty
            else:
                print('normal')
                total += SKUS[sku].get('price') * qty
        else:
            total = -1
        print(total)

    return total


