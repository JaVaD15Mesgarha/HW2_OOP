import random 
Soldiers = {
    "Infantry": {"cost" : 10 , "power" : 1 , "chance" : 0.8 , "health" : 3},
    "Cavalry": {"cost" : 25 , "power" : 2 , "chance" : 0.6 , "health" : 5},
    "Archer": {"cost" : 20 , "power" : 1.5 , "chance" : 0.75 , "health" : 2},
    "Heavy_cavalry": {"cost" : 50 , "power" : 4 , "chance" : 0.4 , "health" : 10}
    }
class User: 
    def __init__(self, name , money=100):
        self.name = name
        self.squad = []
        self.money = money

    def buy_soldier(self , soldier , number) :
        if soldier in Soldiers and self.money >= Soldiers[soldier]['cost'] * number:
            for i in range(number):
                self.squad.append(Soldier(soldier)) 
            self.money -= Soldiers[soldier]['cost'] * number
            print(f"{self.name} bought {number} {soldier}")
        else : 
            print(f"{self.name} does not have money for buying this soldier")
    
    def is_eliminated(self):
        return len(self.squad) == 0 

    def fight(self, other):
        print(f"{self.name} and {other.name} started a battle")
        while self.squad and other.squad : 
            attacker_soldier = random.choice(self.squad)
            defender_soldier = random.choice(other.squad)
            attacker_soldier.attack(defender_soldier)
            if defender_soldier.health <= 0 :
                other.squad.remove(defender_soldier)
        if other.is_eliminated():
            print(f"{other.name} Lost the battle")
            stolen_money = other.money // 2
            self.money += stolen_money
            other.money -= stolen_money
            print(f"{self.name} has taken {other.money} coin from {other.name}")
            if other.money == 0:
                print(f"{other.name} is  Eliminated")  
            
    
    def end_day(self):
        self.money += 50

class Soldier:
    def __init__(self, soldier):
        self.soldier = soldier
        self.health = Soldiers[soldier]['health']
        self.power = Soldiers[soldier]['power']
        self.chance = Soldiers[soldier]['chance']

    def attack(self , other):
        if random.random() < self.chance:
            other.health -= self.power
        else :
            self.health -= other.power

commands= []

def process_commands():
    users = {}
    while True :    
        command = input().strip()
        if command == "" :
            break
        commands.append(command)
    for command in commands : 
        parts = command.split()
        if parts[0] == "CREATE_USER":
            users[parts[1]] = User(parts[1])
            print(f"Registered {parts[1]} with initial money of 100")
        elif parts[0] == "BUY":
            if parts[1] in users:
                users[parts[1]].buy_soldier(parts[2], int(parts[3]))
        elif parts[0] == "ATTACK":
            if parts[1] in users and parts[2] in users:
                users[parts[1]].fight(users[parts[2]])
        elif parts[0] == "DAY":
            for player in users.values():
                player.end_day()
            print("End of the day, players budgets:", ", ".join(f"{p.name} = {p.money}" for p in users.values()))

def main():
    process_commands()

if __name__ == '__main__' :
    main() 