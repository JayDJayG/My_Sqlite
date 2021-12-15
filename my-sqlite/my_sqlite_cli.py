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
        # command_list is a 2D list of functions and function arguments
        # command_list[index of function][function name, argument0, argument1, etc]


    def transform_command_list(self, command_list):
        formatted_command_list = []
        for row in command_list:
            if row[0] == 'FROM': ##from [from, table_name]
                formatted_command_list.append([row[0], row[1]])
            elif row[0] == 'WHERE': #WHERE [WHERE, column_name, criteria]
                new_row = [row[0], row[1]]
                row.remove('=')
                end_of_row = ' '.join(row[2:])
                try:
                    end_of_row = end_of_row.replace("'","")
                except ValueError as ex:
                    pass
                new_row.append(end_of_row)
                formatted_command_list.append(new_row)
            elif row[0] == 'SELECT': #select [select, [string_s]]
                formatted_command_list.append([row[0], row[1:]])
            elif row[0] == 'ORDER': #ORDER [ORDER, order, column_name]
                command = row.pop(0)
                new_row = [command]
                for i in range(1, len(row)):
                    if row[i].lower() == 'asc' or row[i].lower() == 'desc':
                        order = row.pop(i)
                        new_row.append(order)
                        print(f"row = {row}")
                new_row.append(row[0])
                formatted_command_list.append(new_row)



            #functions that need formmatting for the input
                #ORDER [ORDER, [order, column_name]]
                #join [join, [other, column_on_db_a, filename_db_b, column_on_db_b]]
                #select [select, [string_s]]
                #VALUES [VALUES, dict{data}]
                #INSERT [INSERT, [table_name]]
                #set [SET, dictionary values]
                #DELETE [DELETE]
        # return list of commands in format [COMMAND, load_dictionary_arguments]
        return formatted_command_list
        #transform command_list to go into my_sqlite_Request.load_dictionary


    def run_commands(self, formatted_command_list, request_object):
        for idx, query in enumerate(formatted_command_list):
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
        print(command_list)
        formatted_command_list = cli.transform_command_list(command_list)
        print(formatted_command_list)
        cli.run_commands(formatted_command_list, request_object)
        request_object = MySqliteRequest()
        user_input = cli.print_prompt()


if __name__ == "__main__":
    main()