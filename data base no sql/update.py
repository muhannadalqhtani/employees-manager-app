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

def update_record():
    user_id = int(input("Enter your ID: "))
    new_name = input("Enter your new name (leave empty to keep the current name): ")
    new_age_str = input("Enter your new age (leave empty to keep the current age): ")

    records = read_records('data.txt')

    for record in records:
        if record.get("id") == user_id:
            if new_name:
                record["name"] = new_name
            if new_age_str:
                record["age"] = int(new_age_str)
            break

    with open('data.txt', 'w') as file:
        for record in records:
            json.dump(record, file)
            file.write('\n')

# Example usage:
update_record()
