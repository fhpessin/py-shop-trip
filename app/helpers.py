import math
import datetime


def calculate_distance(loc1: list, loc2: list) -> float:
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in cart.items():
            price = self.products[product]
            cost = price * quantity
            total_cost += cost
            unit = "milks" if product == "milk" else f"{product}s"
            print(f"{quantity} {unit} for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list,
                 money: float, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def get_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist = calculate_distance(self.location, shop.location)
        fuel_cost = (dist * 2 * self.car.fuel_consumption / 100) * fuel_price
        product_cost = sum(
            qty * shop.products[product]
            for product, qty in self.product_cart.items()
        )
        return round(fuel_cost + product_cost, 2)
