class Vehicle:
    def __init__(self, vehicle_id, type, max_weight, fixed_cost, cost_per_km, fuel_consumption_per_km):
        self.vehicle_id = vehicle_id
        self.type = type
        self.fuel_consumption_per_km = fuel_consumption_per_km
        self.fixed_cost = fixed_cost
        self.cost_per_km = cost_per_km
        self.max_weight = max_weight
        self.total_distance = 0
        self.total_fuel_cost = 0
        self.total_variable_cost = 0

    def calculate_trip_cost(self, distance, fuel_price, weight):
        if weight > self.max_weight:
            print(f"Error: Cargo weight {weight}kg exceeds max limit {self.max_weight}kg for {self.type}.")
            return False , False
        variable_cost = distance * self.cost_per_km
        fuel_cost = distance * self.fuel_consumption_per_km * fuel_price
        self.total_distance += distance
        self.total_fuel_cost += fuel_cost
        self.total_variable_cost += variable_cost
        return variable_cost, fuel_cost


class LogisticsSystem:
    fuel_prices = {}
    vehicle_types = {
        "PLANE": (5000000, 2000, 10, 10000),
        "TRUCK": (1000000, 500, 3, 5000),
        "PICKUP": (800000, 300, 2, 1500),
        "CAR": (500000, 200, 1.5, 500),
    }

    def __init__(self):
        self.vehicles = {}
        self.next_vehicle_id = 1
        self.distances = {
            "A": {"B": 100, "C": 200, "D": 150, "E": 300},
            "B": {"A": 100, "C": 250, "D": 180, "E": 400},
            "C": {"A": 200, "B": 250, "D": 120, "E": 350},
            "D": {"A": 150, "B": 180, "C": 120, "E": 280},
            "E": {"A": 300, "B": 400, "C": 350, "D": 280},
        }

    def add_vehicle(self, type):
        if type not in self.vehicle_types:
            print("Invalid vehicle type.")
            return
        fixed_cost, cost_per_km, fuel_consumption_per_km, max_weight = self.vehicle_types[type]
        vehicle = Vehicle(self.next_vehicle_id, type, max_weight, fixed_cost, cost_per_km, fuel_consumption_per_km)
        self.vehicles[self.next_vehicle_id] = vehicle
        print(f"Vehicle {type} added with fixed cost: {vehicle.fixed_cost} , variable cost per km: {vehicle.cost_per_km}")
        self.next_vehicle_id += 1

    def set_fuel_price(self, fuel_type, price):
        self.fuel_prices[fuel_type] = price
        print(f"Fuel price for {fuel_type} set to {price} per liter.")

    def add_trip(self, vehicle_name, origin, destination, weight):
        vehicle = self.vehicles[vehicle_name]
        distance = self.distances[origin][destination]
        if vehicle.type == "PLANE" :
            fuel_type = "JET_FUEL"
        elif vehicle.type == "TRUCK" :
            fuel_type = "DIESEL"
        else :
            fuel_type = "GASOLINE"
        
        if fuel_type not in self.fuel_prices:
            print(f"Fuel price for {fuel_type} is not set.")
            return

        variable_cost, fuel_cost = vehicle.calculate_trip_cost(distance, self.fuel_prices[fuel_type], weight)
        if variable_cost is not None:
            print(f"Trip registered: {vehicle.type} from {origin} to {destination} carrying {weight} kg.")

    def end_month(self):
        total_fixed = 0
        total_variable = 0
        total_fuel_cost = 0
        for vehicle in self.vehicles.values() :
            total_fixed += vehicle.fixed_cost 
        for vehicle in self.vehicles.values() :
            total_fuel_cost += vehicle.total_fuel_cost
        for vehicle in self.vehicles.values() :
            total_variable += vehicle.total_variable_cost 
        total_cost = total_fixed + total_variable + total_fuel_cost
        print("End of month report:")
        print(f"Total Fixed Maintenance Cost: {total_fixed}")
        print(f"Total Variable Maintenance Cost: {total_variable}")
        print(f"Total Fuel Cost: {total_fuel_cost}")
        print(f"Total Operational Cost: {total_cost}")
        for vehicle in self.vehicles.values():
            print(f"{vehicle.type} (ID: {vehicle.vehicle_id}):")
            print(f"   Fixed maintenance: {vehicle.fixed_cost}")
            print(f"   Variable maintenance: {vehicle.total_variable_cost}")
            print(f"   Fuel cost: {vehicle.total_fuel_cost}")


def main():
    logistics = LogisticsSystem()
    commands = []
    while True:
        command = input().strip()
        commands.append(command)
        if command == "END_MONTH":
            break
    
    for i in range(len(commands)):
        if commands[i] == "END_MONTH":
            logistics.end_month()
            break
        parts = commands[i].split()
        if parts[0] == "ADD_VEHICLE":
            type = parts[1]
            logistics.add_vehicle(type)

        elif parts[0] == "SET_FUEL_PRICE":
            fuel_type, price = parts[1] , parts[2]
            logistics.set_fuel_price(fuel_type, int(price))

        elif parts[0] == "ADD_TRIP":
            vehicle_id, origin, destination, weight = parts[1:]
            logistics.add_trip(int(vehicle_id), origin, destination, int(weight))

if __name__ == '__main__' : 
    main()