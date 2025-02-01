# importing modules
import json
import argparse as arg
import random

with open('data.json', 'r') as file:
    data = json.load(file)

def write_to_json():
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

#functions to be triggered by args
def add(amount, description):
    id = random.randint(1, 100)
    expense = {
        id : {
            "id" : id,
            "amount" : amount,
            "description" : description
        }
    }
    data.update(expense)
    write_to_json()
    print(f"ID {id} : Rs. {amount} added for reason : {description}")

def remove(id):
    for key, value in list(data.items()):
        if key==id:
            del data[key]
            write_to_json()
            print(f"Removed expenses with id ${id}")
            break
    else:
        print("Expense not found")

def update(id, new_amount, new_description):
    for key, value in list(data.items()):
        if key==id:
            value['amount'] = new_amount
            value['description'] = new_description
            write_to_json()
            print(f"Update expense. New amount is ${new_amount} with description : ${new_description}")
            break
    else:
        print("ID not found")

def summary():
    print("Summary of expenses")
    print("ID   Amount  Description")
    print("------------------")
    for key, value in data.items():
        print(f"{value['id']}    {value['amount']}  {value['description']}")

def total():
    sum = 0
    for key, value in data.items():
        sum += value['amount']
    print(f"Total expenses: Rs. {sum}")

# setting up argparse
parser = arg.ArgumentParser(description="A simple expense tracker.")
subparsers = parser.add_subparsers(dest="command")

## parsing arguments - add, remove, update, summary
### add
parser_add = subparsers.add_parser("add", help="Adds expense.")
parser_add.add_argument("amount", type=float, help="Amount to be added as expense")
parser_add.add_argument("description", help="Description of the expense")

### remove
parser_remove = subparsers.add_parser("remove", help="Removes expense")
parser_remove.add_argument("id", help="Removes expense based on ID")

### update
parser_update = subparsers.add_parser("update", help="Modifies an existing expense")
parser_update.add_argument("id", help="Refer ID for updating")
parser_update.add_argument("amount", type=float, help="Update expense amount")
parser_update.add_argument("description", help="Update expense description")

### summary
parser_summary = subparsers.add_parser("summary", help="Gives summary of expenses")

### total expenses
parser_total = subparsers.add_parser("total", help="List the total expenses occurred so far")

args = parser.parse_args()

# calling functions
if args.command == "add":
    add(args.amount, args.description)
elif args.command == "remove":
    remove(args.id)
elif args.command == "update":
    update(args.id, args.amount, args.description)
elif args.command == "summary":
    summary()
elif args.command == "total":
    total()
