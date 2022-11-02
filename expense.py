from PyInquirer import prompt
import csv

def get_spender():
    users = []
    with open('users.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            users.append(row[0])
    return users

def get_consomer(spender):
    consomers = []
    with open('users.csv', 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            if spender == row[0]:
                consomers.append({"name": row[0], "checked": True})
            else:
                consomers.append({"name": row[0]})
    consomer_option = {
        "type":"checkbox",
        "name":"consomer",
        "message":"New Expense - Consomer",
        "choices": consomers,
    },
    return prompt(consomer_option)

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender:",
        "choices": get_spender(),
    },
    

]

def new_expense(*args):
    infos = prompt(expense_questions)
    consomer = get_consomer(infos['spender'])
    consomers=""
    for row in consomer['consomer']:
        consomers += row + " "

    with open('expense_report.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos['amount'], infos['label'], infos['spender'], consomers])
    print("Expense Added !")
    return True


