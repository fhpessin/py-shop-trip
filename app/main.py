import json
import os
from app.helpers import Customer, Shop


def shop_trip() -> None:
    # Localiza o arquivo config.json no mesmo diretório
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    
    with open(config_path, "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    shops = [Shop(**s) for s in data["shops"]]
    customers = [Customer(**c) for c in data["customers"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        
        best_shop = None
        cheapest_cost = float("inf")

        for shop in shops:
            cost = customer.get_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {cost}")
            if cost < cheapest_cost:
                cheapest_cost = cost
                best_shop = shop

        if best_shop and cheapest_cost <= customer.money:
            print(f"{customer.name} rides to {best_shop.name}\n")
            best_shop.print_receipt(customer.name, customer.product_cart)
            customer.money -= cheapest_cost
            customer.location = best_shop.location
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a "
                  "purchase in any shop\n")
