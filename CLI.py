print("Be Welcome to the CLI (Contact Book)")

contacts = []

# main while that will come back to the menu after the first, second and the third option:
while True:
    answer1 = input(
        "What do you would like to do? \n [1] Add a contact \n [2] Search for a contact \n [3] Exit the program \n"
    )

    while answer1 != "1" and answer1 != "2" and answer1 != "3":
        print("Please could you try it again, Remember you can only choose 1,2 or 3")
        answer1 = input(
            "What do you would like to do? \n [1] Add a contact \n [2] Search for a contact \n [3] Exit the program \n"
        )

    if answer1 == "1":
        add_more = "yes"

        while add_more == "yes":
            print("-----ADD A CONTACT-----")

            name = input("Enter the name of the person: ").strip().capitalize()
            while not name:
                print("Name cannot be empty. Please enter a valid name.")
                name = input("Enter the name of the person: ").strip().capitalize()
            print("Name Added!")

            age = input("Enter the age of the person: ").strip().capitalize()
            while not age:
                print("Age cannot be empty. Please enter a valid age.")
                age = input("Enter the age of the person: ").strip().capitalize()
            print("Age Added!")

            contact_number = (
                input("Enter the contact number of the person: ").strip().capitalize()
            )
            while not contact_number:
                print("Contact Number cannot be empty. Please enter a valid number.")
                contact_number = (
                    input("Enter the contact number of the person: ")
                    .strip()
                    .capitalize()
                )
            print("Contact Number Added!")

            contact = {"name": name, "age": age, "contact_number": contact_number}

            contacts.append(contact)
            add_more = (
                input("Do you would like to add one more contact?").strip().lower()
            )

    elif answer1 == "2":
        print("-----Contact Searching-----")
        print(
            "Before you start, Please remember that you only need to insert the first person´s name or the same with the last´s name as well if it´s necessary!"
        )
        answer_search = (
            input(
                "Could you insert me the name of the person that you would like to see the info from?"
            )
            .strip()
            .capitalize()
        )
        for contact in contacts:
            print(contact["name"])
            if answer_search == contact["name"]:
                print(f"Contact Name: {contact['name']}")
                print(f"Contact Age: {contact['age']}")
                print(f"Contact Number: {contact['contact_number']}")
    elif answer1 == "3":
        print("Okay, We hope to see you again!")
        break
