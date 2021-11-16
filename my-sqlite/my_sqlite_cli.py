from my_sqlite_request import MySqliteRequest

# valid_commands = [
#     'from',
#     'select',
#     'where',
#     'join',
#     'order',
#     'insert',
#     'values',
#     'update',
#     'set',
#     'delete'
#     ]

def print_title():
    program_version = "0.1"
    program_date = "2021-XX-XX"
    title = " ".join(["MySQLite version", program_version, program_date])
    print(title)


def print_prompt():
    prompt = "my_sqlite_cli>"
    user_input = input(prompt)
    return user_input

def parse_prompt(user_input, request_object):
    tokens = user_input.split()
    # print(tokens) #debug
    command_list = []
    command_count = 0
    for i in range(0, len(tokens)):
        # print(f"i = {i}") #debug
        # print(f"command = {tokens[i]}") #debug        
        if hasattr(request_object, tokens[i]): #check if token is a command in MySqliteREquest class
            command_list.append([])
            command_list[command_count].append(tokens[i])
            command_count = command_count + 1
        elif command_count > 0: #otherwise attach to current command list
            command_list[command_count - 1].append(tokens[i])
        else:
            print("Error: unknown command or invalid arguments: " + user_input)
    print(command_list) #debug
    return command_list

def run_commands(command_list, request_object):
    for idx, query in enumerate(command_list):
        try:
            getattr(request_object, query[0])(*query[1:])
        except TypeError:
            getattr(request_object, query[0])(query[1:])


request_object = MySqliteRequest()
print_title()
user_input = print_prompt()
while (user_input != "quit"):
    command_list = parse_prompt(user_input, request_object)
    run_commands(command_list, request_object)
    user_input = print_prompt()