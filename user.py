from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"Name",
        "message":"New Expense - Name: ",
    },
]

def add_user(*args):
    infos = prompt(user_questions)
    if infos['Name'] == "" or infos['Name'] == " ":
        return False
    with open('users.csv', 'a', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([infos['Name']])
    print("User Add")
    return True