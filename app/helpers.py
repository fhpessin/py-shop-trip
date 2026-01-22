import math
import datetime
from typing import List, Dict, Any


def calculate_distance(loc1: List[int], loc2: List[int]) -> float:
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


class Shop:
    def __init__(self, name: str, location: List[int], products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, cart: Dict[str, int]) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        
        total_products_cost = 0.0
        for product, quantity in cart.items():
            price = self.products[product]
            cost = price * quantity
            total_products_cost += cost
            unit = "milks" if product == "milk" else f"{product}s"
            print(f"{quantity} {unit} for {cost} dollars")
            
        print(f"Total cost is {total_products_cost} dollars")
        print("See you again!")


class Customer:
    def __init__(
        self, 
        name: str, 
        product_cart: Dict[str, int], 
        location: List[int], 
        money: float, 
        car: Dict[str, Any]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def get_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = calculate_distance(self.location, shop.location)
        # Ida e volta: distância * 2
        fuel_needed = (distance * 2 * self.car.fuel_consumption) / 100
        fuel_cost = fuel_needed * fuel_price
        
        product_cost = sum(
            qty * shop.products[prod] 
            for prod, qty in self.product_cart.items()
        )
        return round(fuel_cost + product_cost, 2)
