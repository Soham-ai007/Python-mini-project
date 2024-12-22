def input_friend_list():
        return input("Enter friends' names (comma-separated): ").strip().split(',')

def find_common_friends(person_data, person1, person2):
    
    if person1 in person_data and person2 in person_data:
        return list(set(person_data[person1]) & set(person_data[person2]))
    else:
        return None

def find_all_friends(person_data):
    
    all_friends_set = set()
    for friends in person_data.values():
        all_friends_set.update(friends)
    return list(all_friends_set)

def main():
    person_data = {}

    while True:
        print("\nMenu:")
        print("1. Add a person and their friends")
        print("2. Find common friends between two persons")
        print("3. Display all unique friends")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            person = input("Enter the person's name: ").strip()
            if person in person_data:
                print(f"{person} already exists. Updating their friend list.")
            else:
                print(f"Adding a new person: {person}")
            person_data[person] = input_friend_list()

        elif choice == "2":
            person1 = input("Enter the first person's name: ").strip()
            person2 = input("Enter the second person's name: ").strip()
            common_friends = find_common_friends(person_data, person1, person2)

            if common_friends is not None:
                if common_friends:
                    print(f"Common friends between {person1} and {person2}: {', '.join(common_friends)}")
                else:
                    print(f"No common friends between {person1} and {person2}.")
            else:
                print("One or both person names are not in the system.")

        elif choice == "3":
            all_friends = find_all_friends(person_data)
            print(f"All unique friends: {', '.join(all_friends)}")

        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()