people = []

def add_person():
    name = input("Enter name: ")
    age = input("Enter age: ")
    email = input("Enter email: ")

    person = {"name": name, "age": age, "email": email}
    return person

def delete_contact(people):
   for i , person in enumerate(people):
       print(i + 1 , "==>" , person["name"], "||", person["age"], "||", person["email"])
       
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
            print("Contact deleted successfully.")

print(" Hello, welcome to the Content Management System.")
print()

while True:
    command = input("What would you like to do? (ADD/DELETE/SEARCH): ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added successfully.")

    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        pass
    else:
        print("Invalid command. Please try again.")

    print(people)