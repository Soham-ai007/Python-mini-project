def friends_list():
    num_users = int(input("Enter number of all users: "))
    friends_dict = {}

    for i in range(num_users):
        user = input(f"Enter name of user {i + 1}: ")
        friends = input(f"Enter {user}'s list of friends (comma-separated): ").split(",")
        friends_dict[user] = set(friend.strip() for friend in friends)

    return friends_dict

def seek_out_mutual_friends(friends_dict):
    mutual_friends = set.intersection(*friends_dict.values())
    return mutual_friends

def find_mutual_friends(friends_dict, user1, user2):
    if user1 in friends_dict and user2 in friends_dict:
        return friends_dict[user1].intersection(friends_dict[user2])
    else:
        return None

if __name__ == "__main__":
    friends_dict = friends_list()

    print("\nLists of Friends:")
    for user, friends in friends_dict.items():
        print(f"{user}: {friends}")

    common_friends = seek_out_mutual_friends(friends_dict)
    print("\nAmong all users, these are mutual friends:", common_friends if common_friends else "None")

    print("\nFind mutual friends between two users:")
    user1 = input("Enter first user: ")
    user2 = input("Enter second user: ")
    mutual_friends = find_mutual_friends(friends_dict, user1, user2)

    if mutual_friends is not None:
        print(f"Mutual friends between {user1} and {user2}: {mutual_friends if mutual_friends else 'None'}")
    else:
        print("One or both users not found.")
