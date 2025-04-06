import pickle

class Product:
    def __init__(self, name, price, category, worker, stock):
        self.name = name
        self.price = price
        self.category = category
        self.worker = worker
        self.stock = stock
        self.ratings = []

    def rating(self, point):
        if 1 <= point <= 5:
            self.ratings.append(point)

    def average_rating(self):
        return round(sum(self.ratings) / len(self.ratings), 2) if self.ratings else 0


class User:
    def __init__(self, username, password, role="user"):
        self.username = username
        self.password = password
        self.role = "admin" if username == "ADMIN" and password == "ADMIN" else role
        self.balance = 0
        self.cart = {}
        self.product_point = []
        self.purchased_products = []

    def add_to_cart(self, product, quantity):
        if product.stock >= quantity:
            self.cart[product] = self.cart.get(product, 0) + quantity
        else:
            print("Not enough stock available!")

    def remove_from_cart(self, product):
        if product in self.cart:
            del self.cart[product]
            print(f"{product.name} removed from cart.")
        else:
            print("Product not in cart.")

    def finalize_order(self):
        total = sum(product.price * quantity for product, quantity in self.cart.items())
        if self.balance >= total:
            self.balance -= total
            for product, quantity in self.cart.items():
                product.stock -= quantity
                self.purchased_products.append(product)
            self.cart.clear()
            print("Your Order Has Been Finalized.")
        else:
            print("Not Enough Cash")

    def show_cart(self):
        if not self.cart:
            print("Cart is empty.")
        for product, quantity in self.cart.items():
            print(f"{product.name} x{quantity} = {product.price * quantity}$")

    def rate_product(self, product, point):
        if product in self.purchased_products and product not in self.product_point:
            product.rating(point)
            self.product_point.append(product)
            print("Thanks for your feedback!")
        else:
            print("You cannot rate this product.")


class Store:
    def __init__(self):
        self.users = []
        self.products = []

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print("Login successful!")
                return user
        print("Invalid Username Or Password")
        return None

    def signup(self, username, password, role="user"):
        for user in self.users:
            if user.username == username:
                print("This Username Is Taken Already!")
                return None
        if len(password) < 8:
            print("Password Is Too Short!")
            return None
        user = User(username, password, role)
        self.users.append(user)
        print("Account created successfully!")
        return user

    def add_product(self, name, price, category, worker, stock):
        self.products.append(Product(name, price, category, worker, stock))

    def search(self, key, value):
        results = []
        if key == "name":
            results = [p for p in self.products if value.lower() in p.name.lower()]
        elif key == "category":
            results = [p for p in self.products if value.lower() in p.category.lower()]
        elif key == "price":
            min_p, max_p = value
            results = [p for p in self.products if min_p <= p.price <= max_p]
        return results

    def save_data(self, filename="store.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_data(filename="store.pkl"):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("New Shop")
            return Store()


def user_menu(store, current_user):
    while True:
        print(f"\nBalance: {current_user.balance}$")
        print("1. Search Products\n2. Add to Cart\n3. View Cart\n4. Remove from Cart\n5. Finalize Order")
        print("6. Rate Product\n7. Increase Balance\n0. Logout")
        choice = input("Choice: ")

        if choice == "1":
            key = input("Search by (name/category/price): ")
            if key.lower() == "price":
                min_p = int(input("Min Price: "))
                max_p = int(input("Max Price: "))
                results = store.search("price", (min_p, max_p))
            else:
                value = input("Value: ")
                results = store.search(key.lower(), value)
            for i, p in enumerate(results, 1):
                print(f"{i}. {p.name} | {p.category} | {p.price}$ | Rating: {p.average_rating()}")

        elif choice == "2":
            name = input("Product name: ")
            matches = [p for p in store.products if name.lower() in p.name.lower()]
            if matches:
                product = matches[0]
                quantity = int(input("Quantity: "))
                current_user.add_to_cart(product, quantity)
            else:
                print("Product not found.")

        elif choice == "3":
            current_user.show_cart()

        elif choice == "4":
            name = input("Product to remove: ")
            matches = [p for p in current_user.cart if name.lower() in p.name.lower()]
            if matches:
                current_user.remove_from_cart(matches[0])
            else:
                print("Product not in cart.")

        elif choice == "5":
            current_user.finalize_order()
            store.save_data()

        elif choice == "6":
            name = input("Product name: ")
            matches = [p for p in store.products if name.lower() in p.name.lower()]
            if matches:
                score = int(input("Rating (1-5): "))
                current_user.rate_product(matches[0], score)
                store.save_data()
            else:
                print("Product not found.")

        elif choice == "7":
            amount = int(input("Amount to add: "))
            current_user.balance += amount
            print("Balance updated.")

        elif choice == "0":
            print("Logged out.")
            store.save_data()
            break

        else:
            print("Invalid choice.")


def admin_menu(store, current_user):
    while True:
        print("\nAdmin Panel")
        print("1. Add Product\n0. Logout")
        choice = input("Choice: ")
        if choice == "1":
            name = input("Name: ")
            category = input("Category: ")
            price = int(input("Price: "))
            stock = int(input("Stock: "))
            store.add_product(name, price, category, current_user.username, stock)
            print("Product added.")
            store.save_data()
        elif choice == "0":
            print("Logged out.")
            store.save_data()
            break
        else:
            print("Invalid choice.")


def main():
    store = Store.load_data()
    while True:
        print("\n--- Welcome to the Console Store ---")
        choice = input("1. Login\n2. Signup\n3. Exit\nChoice: ")
        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            user = store.login(username, password)
            if user:
                if user.role == "admin":
                    admin_menu(store, user)
                else:
                    user_menu(store, user)

        elif choice == "2":
            username = input("Username: ")
            password = input("Password (min 8 characters): ")
            user = store.signup(username, password)
            if user:
                user_menu(store, user)

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
