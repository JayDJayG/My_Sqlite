from my_sqlite_request import MySqliteRequest

valid_commands = [
    'from',
    'select',
    'where',
    'join',
    'order',
    'insert',
    'values',
    'update',
    'set',
    'delete'
    ]

command_list = []
command_dictionary = {}

def print_title():
    program_version = "0.1"
    program_date = "2021-XX-XX"
    title = " ".join(["MySQLite version", program_version, program_date])
    print(title)


def print_prompt():
    prompt = "my_sqlite_cli>"
    user_input = input(prompt)
    return user_input

def parse_prompt(user_input):
    tokens = user_input.split()
    print(tokens)
    for i in range(0, len(tokens)):
        if tokens[i] in valid_commands:
            command_list.append(tokens[i])
        elif (len(command_list) > 0):
            command_list[-1].append(token[i])
        else:
            print("Error: unknown command or invalid arguments: " + user_input)
        print(command_list)

print_title()
user_input = print_prompt()
while (user_input != "quit"):
    parse_prompt(user_input)
    user_input = print_prompt()