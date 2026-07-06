# quand on veut add un Animal
# on choisi l' enclos
# et ensuite on y ajoute l'animal
# donc a enclos.animallist.append

from asyncio.windows_events import NULL


class enclosure:
    def __init__(self, name, quantity, animal_list = []):
        self.name = name
        self.quantity = quantity
        self.animal_list = animal_list
    def display_enclosure_informations(self):
        print("------------------------------------")
        print("Name : ",self.name)
        print("Quantity : ",self.quantity)
    def add_animal_to_enclosure(self, animal):
        self.animal_list.append(animal)
        self.quantity -= 1
    
nature = enclosure("Fields", 99999)
class Animal:
    def __init__(self, name, age, weight, enclosure=nature):
        self.name = name
        self.age = age
        self.weight = weight
        self.enclosure = enclosure.name
    def eat(self):
        print(self.name,"is eating")
        return 0
    def sleep(self):
        print(self.name,"is sleeping")
        return 0
    def display(self):
        print("------------------------------------")
        print("Name : ",self.name)
        print("Age : ",self.age)
        print("Weight : ",self.weight)
    def make_noise(self):
        return 0

class Lion(Animal):
    def make_noise(self):
        print(self.name, "Roars")
        return 0
    def display(self):
        super().display()
        print("Type: Lion")
class Elephant(Animal):
    def make_noise(self):
        print(self.name,"Trumpets")
        return 0
    def display(self):
        super().display()
        print("Type: Elephant")
class Monkey(Animal):
    def make_noise(self):
        print(self.name, "Screams")
        return 0
    def display(self):
        super().display()
        print("Type: Monkey")
class Bird(Animal):
    def make_noise(self):
        print(self.name, "Shouting")
        return 0
    def display(self):
        super().display()
        print("Type: Bird")

def add_animal(enclosure):
    print("Which type of animal do you want to add?")
    choix = input("1.Lion \n2.Elephant \n3.Monkey \n4.Bird\n")
    Name = input("Enter the Animal Name : ")
    Age = int(input("Enter the Animal Age : "))
    Weight = int(input("Enter the Animal Weight(kg) : "))
    if choix == "1":
        NameN = Lion(Name, Age, Weight,enclosure)
        Animals_list.append(NameN)
    elif choix == "2":
        NameN = Elephant(Name, Age, Weight,enclosure)
        Animals_list.append(NameN)
    elif choix == "3":
        NameN = Monkey(NameN)
        Animals_list.append(NameN)
    elif choix == "4":
        NameN = Bird(Name, Age, Weight,enclosure)
        Animals_list.append(NameN)
    else :
        print("choice not correct")
        add_animal(enclosure)
    enclosure.add_animal_to_enclosure(NameN)

class Zoo():

    id = 0
    def add(self):
        if Enclosure_list != []:
            print("Type the number of the enclosure of destination")
            number = 1
            for i in Enclosure_list:
                print(number,":", i.name)
                number += 1
            enclosure_number = int(input(">"))
            if enclosure_number > number:
                print("Number not correct")
            elif Enclosure_list[enclosure_number-1].quantity <= 0 :
                print("This enclosure is full")
            else :
                enclosure = Enclosure_list[enclosure_number-1]
                add_animal(enclosure)
        else:
            print("You don't have any enclosure")
        

    def create_enclosure(self):
        print("Enter your enclosure information")
        name = input("Enter the Name of the enclosure :")
        quantity = int(input("Enter the Quantity of the enclosure :"))
        Enclosure_list.append(enclosure(name,quantity))
    
    def display_all_enclosure_information(self):
        for i in Enclosure_list:
            print("------------------------------------")
            print("Name : ",i.name)
            print("Quantity : ",i.quantity)
            print("Animals : ",i.animal_list)
    def supprimer(self):
        Name_delete = input("Enter the name of the animal you want to delete : ")
        find = False
        for i in Animals_list:
            if i.name == Name_delete:
                Animals_list.remove(i)
                find = True
        if find is False:
            print("This animal Does not exist")

    def rechercher(self):
        Name_search = input("Enter the name of the animal you are looking for : ")
        find = False
        for i in Animals_list:
            if i.name == Name_search:
                i.display()
                find = True
        if find is False:
            print("This animal Does not exist")

    def afficher(self):
        for i in Animals_list:
                i.display()
        if Animals_list == []:
            print("The list is empty")

    def nourrir_animaux(Animal):
        for i in Animals_list:
                i.eat()
        if Animals_list == []:
            print("The list is empty")

    def faire_parler(Animal):
        for i in Animals_list:
                i.make_noise()
        if Animals_list == []:
            print("The list is empty")
class Employee:
    def __init__(self, name, salaire):
        self.name = name
        self.salaire = salaire
    def work(self):
        return 0

class Animal_Caretaker(Employee):
    def work(self):
        print("Giving Food an animals")

class Veterinarian(Employee):
    def work(self):
        print("Heals an animal")

class Keeper(Employee):
    def work(self):
        print("Check for animals")

        
Lion1 = Lion("Marco", 4, 241)
Monkey1 = Monkey("Monkey", 8, 35)
Enclosure_list = []
Animals_list = []
Animals_list.append(Monkey1)
Animals_list.append(Lion1)
zoo = Zoo()
def main():
    print("Welcome to the Zoo management system")
    choice = NULL;
    while choice != "0":
        print("Chose an action")
        print("0.Quit")
        print("1.Display all the animals")
        print("2.Add an Animal")
        print("3.Delete an animal")
        print("4.Search an animal")
        print("5.Give Food to all animals")
        print("6.Make all animals sound")
        print("7.Add an enclosure")
        print("8.Print all enclosure information")
        choice = input(">")
        if choice == "1":
            zoo.afficher()
        elif choice == "2":
            zoo.add()
        elif choice == "3":
            zoo.supprimer()
        elif choice == "4":
            zoo.rechercher()
        elif choice == "5":
            zoo.nourrir_animaux()
        elif choice == "6":
            zoo.faire_parler()
        elif choice == "7":
            zoo.create_enclosure()
        elif choice == "8":
            zoo.display_all_enclosure_information()
        elif choice == "0":
            print("Aurevoir!")
        else :
            print("choix incorrect")
main()

print(Animals_list)