import json 

with open("contacts.json", "r") as file:  
    people = json.load(file)["contacts"]

def add_person():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    person = {"name": name, "age": age, "email": email}
    return person


def display_people(people):
     for i , person in enumerate(people):
       print(i + 1 , "==>" , person["name"], "||", person["age"], "||", person["email"])
       

def delete_contact(people):
       display_people(people)
       while True:
           number = input("enter a number to delete: ")
           
           try:
               number = int(number)
               if(number <= 0 or number > len(people)):
                   print("Invalid number. out of range.")
               else:
                   break
           except:
            print("Invalud number. Please try again.")

            people.pop(number - 1)
            print("Person deleted successfully.")

def search_name(people):
    search_name = input("Enter name to search: ")
    results = []
    for person in people:
        name= person["name"]
        if search_name.lower() in name.lower():
            results.append(person)

    display_people(results)

print(" Hello, welcome to the Content Management System.")
print()

while True:
    print("people list size: ", len)
    command = input("What would you like to do? (ADD/DELETE/SEARCH): ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added successfully.")

    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search_name(people)
    else:
        print("Invalid command. Please try again.")

    print(people)


    with open("contacts.json", "w") as file:
        json.dump({"contacts": people},file)