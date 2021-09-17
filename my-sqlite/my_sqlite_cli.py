def print_title():
    program_version = "0.1"
    program_date = "2021-XX-XX"
    title = " ".join(["MySQLite version", program_version, program_date])
    print(title)

def print_prompt():
    prompt = "my_sqlite_cli>"
    user_input = input(prompt)
    return user_input

print_title()
command = print_prompt()
while (command != "quit"):
    command = print_prompt()