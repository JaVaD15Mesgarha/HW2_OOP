import abc

class Food(abc.ABC):
    food_id = 1  

    def __init__(self, name):
        self.name = name
        self.food_id = Food.food_id
        Food.food_id += 1 

    @abc.abstractmethod
    def calculate_price(self):
        pass

    def __add__(self, other):
        return self.calculate_price() + other.calculate_price()

    def __mul__(self, count):
        return self.calculate_price() * count

class Pizza(Food):
    sizes = {"Small": 8, "Medium": 12, "Large": 16}
    extras = {"Cheese": 2, "Extra Sauce": 1.5, "Olives": 1}

    def __init__(self, size, pizza_type, extras=[]):
        super().__init__(f"{size} {pizza_type} Pizza")
        self.size = size
        self.pizza_type = pizza_type
        self.extras = [extra.strip() for extra in extras if extra]

    def calculate_price(self):
        base_price = self.sizes[self.size]
        extra_price = sum(Pizza.extras.get(extra, 0) for extra in self.extras)
        return base_price + extra_price

class Burger(Food):
    layers = {"Single": 6, "Double": 9, "Triple": 12}
    breads = {"Regular": 0, "Sesame": 0.5, "Brioche": 1}
    extras = {"Cheese": 1, "Bacon": 2, "Egg": 1.5}

    def __init__(self, layer, bread, extras=[]):
        super().__init__(f"{layer} Burger with {bread}")
        self.layer = layer
        self.bread = bread
        self.extras = [extra.strip() for extra in extras if extra]

    def calculate_price(self):
        base_price = Burger.layers[self.layer] + Burger.breads[self.bread]
        extra_price = sum(Burger.extras.get(extra, 0) for extra in self.extras)
        return base_price + extra_price

class Drink(Food):
    sizes = {"300ml": 2, "500ml": 3, "1L": 5}

    def __init__(self, size, drink_type):
        super().__init__(f"{size} {drink_type}")
        self.size = size
        self.drink_type = drink_type

    def calculate_price(self):
        return self.sizes[self.size]

class Order:
    def __init__(self):
        self.foods = {}
        self.discounts = {"DISCOUNT10": 0.1}

    def add_item(self, food, quantity):
        if food.food_id in self.foods:
            self.foods[food.food_id]["quantity"] += quantity
        else:
            self.foods[food.food_id] = {"food": food, "quantity": quantity, "food_id" : food.food_id }

    def remove_item(self, food_id):
        if food_id in self.foods:
            del self.foods[food_id]

    def calculate_total(self):
        total = sum(item["food"].calculate_price() * item["quantity"] for item in self.foods.values())
        return total

    def apply_discount(self, code):
        total = self.calculate_total()
        if code in self.discounts:
            total *= (1 - self.discounts[code])
        return total

    def display_order(self, discount_code=None):
        print("Order Summary:")
        for item in self.foods.values():
            print(f"{item['quantity']}x {item['food'].name} (ID: {item['food_id']}) - ${item['food'].calculate_price()} each")

        total_price = self.calculate_total()

        if discount_code:
            total_price = self.apply_discount(discount_code)
            print(f"Discount Code Applied: {discount_code}")

        print(f"Total Price: ${total_price:.2f}")

def main():
    order = Order()
    while True:
        print("** Restourant Menu **")
        print("Order food : 1 \nRemove food: 2 \nShow Order: 3 \nExit: 4")
        x = int(input())
        
        if x == 1:
            food_type = input("Enter food type (Pizza, Burger, Drink): ").strip().lower()
            if food_type == "pizza":
                size = input("Enter size (Small/Medium/Large): ").strip()
                pizza_type = input("Enter pizza type: ").strip()
                extras = input("Enter extras (comma-separated, or leave empty): ").strip().split(',')
                quantity = int(input("Enter number of your Pizza: "))
                order.add_item(Pizza(size, pizza_type, extras), quantity)

            elif food_type == "burger":
                layer = input("Enter layer (Single/Double/Triple): ").strip()
                bread = input("Enter bread type (Regular/Sesame/Brioche): ").strip()
                extras = input("Enter extras (comma-separated, or leave empty): ").strip().split(',')
                quantity = int(input("Enter number of your Burger: "))
                order.add_item(Burger(layer, bread, extras), quantity)

            elif food_type == "drink":
                size = input("Enter size (300ml/500ml/1L): ").strip()
                drink_type = input("Enter type of your Drink: ").strip()
                quantity = int(input("Enter number of your drink: "))
                order.add_item(Drink(size, drink_type), quantity) 
            
        if x == 2 :
            removing = int(input("Please type your Food ID: ")) 
            order.remove_item(removing)

        if x == 3 :
            discount_code = ""
            order.display_order(discount_code)

        if  x == 4:
            discount_code = input("Enter discount code (or press Enter to skip): ").strip()
            order.display_order(discount_code)
            break

if __name__ == '__main__':
    main()
