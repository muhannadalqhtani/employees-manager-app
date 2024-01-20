import json

def get_highest_id(filename):
    records = read_records(filename)
    if records:
        return max(record["id"] for record in records)
    else:
        return 0

def create_record(filename):
    data = {}
    data["id"] = get_highest_id(filename) + 1
    data["name"] = input("Enter Name: ")
    data["age"] = int(input("Enter Age: "))
    
    records = read_records(filename)
    records.append(data)

    with open(filename, 'w') as file:
        json.dump(records, file, indent=2)

def read_records(filename):
    records = []
    try:
        with open(filename, 'r') as file:
            records = json.load(file)
    except FileNotFoundError:
        pass
    return records

# Example usage:
create_record('users.json')
