from my_sqlite_request import MySqliteRequest



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
    print("Error: unknown command or invalid arguments:" + user_input)

print_title()
user_input = print_prompt()
while (user_input != "quit"):
    parse_prompt(user_input)
    user_input = print_prompt()