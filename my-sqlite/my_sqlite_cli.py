from os import name
from my_sqlite_request import MySqliteRequest

class CLI:
    def print_title(self):
        program_version = "0.1"
        program_date = "2021-XX-XX"
        title = " ".join(["MySQLite version", program_version, program_date])
        print(title)

    def print_prompt(self):
        prompt = "my_sqlite_cli>"
        user_input = input(prompt)
        return user_input

    def parse_prompt(self, user_input, request_object):
        tokens = user_input.split()
        command_list = []
        command_count = 0
        for i in range(0, len(tokens)):
            if hasattr(request_object, tokens[i]): #check if token is a command in MySqliteREquest class
                command_list.append([])
                command_list[command_count].append(tokens[i])
                command_count = command_count + 1
            elif command_count > 0: #otherwise attach to current command list
                command_list[command_count - 1].append(tokens[i])
            else:
                print("Error: unknown command or invalid arguments: " + user_input)
        return command_list

    def run_commands(self, command_list, request_object):
        for idx, query in enumerate(command_list):
            # print(query) #debug
            try:
                getattr(request_object, query[0])(*query[1:])
            except TypeError:
                getattr(request_object, query[0])(query[1:])
        request_object.run()

def main():
    cli = CLI()
    request_object = MySqliteRequest()
    cli.print_title()
    user_input = cli.print_prompt()
    while (user_input != "quit"):
        command_list = cli.parse_prompt(user_input, request_object)
        cli.run_commands(command_list, request_object)
        request_object = MySqliteRequest()
        user_input = cli.print_prompt()


if __name__ == "__main__":
    main()