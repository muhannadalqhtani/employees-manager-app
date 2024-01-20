import json

def read_records(filename):
    records = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                records.append(json.loads(line))
    except FileNotFoundError:
        pass
    return records

def read_user_info():
    user_id = int(input("Enter your ID to read: "))

    records = read_records('data.txt')

    for record in records:
        if record.get("id") == user_id:
            print("Your Information:")
            print("ID:", record["id"])
            print("Name:", record["name"])
            print("Age:", record["age"])
            return

    print("User with ID {} not found.".format(user_id))

# Example usage:
read_user_info()
