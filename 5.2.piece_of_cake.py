def get_recipe_price(prices, optionals=None, **amounts):
    if optionals is None:
        optionals = []

    total_price = 0

    for ingredient, price_per_100g in prices.items():
        if ingredient not in optionals:
            amount = amounts.get(ingredient, 0)

            total_price += (amount / 100) * price_per_100g

    if total_price == int(total_price):
        return int(total_price)

    return total_price


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

print(get_recipe_price({}))
