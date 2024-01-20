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

def delete_record():
    user_id = int(input("Enter your ID to delete : "))

    records = read_records('data.txt')

    records = [record for record in records if record.get("id") != user_id]

    with open('data.txt', 'w') as file:
        for record in records:
            json.dump(record, file)
            file.write('\n')

# Example usage:
delete_record()

