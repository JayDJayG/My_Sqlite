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
                new_row.append(row.pop())
                formatted_command_list.append(new_row)
            elif row[0] == 'INSERT': #INSERT [INSERT, [table_name]]
                command = row.pop(0)
                new_row = [command]
                for i in range(1, len(row)):
                    if row[i].lower() == 'into':
                        row.pop(i)
                new_row.append(row.pop())
                formatted_command_list.append(new_row)
            elif row[0] == 'VALUES': #VALUES [VALUES, dict{data}]
                command = row.pop(0)
                new_row = [command]
                row_str = ' '.join(row)
                found_item = False
                item = ""
                list_of_values = []
                for index, char in enumerate(row_str):
                    if char == "'":
                        found_item = not found_item
                        if len(item) > 0:
                            list_of_values.append(item)
                            item = ""
                    elif found_item == True:
                        item = ''.join([item, char])
                new_row.append(list_of_values)
                formatted_command_list.append(new_row)
            elif row[0] == 'UPDATE': #UPDATE [UPDATE, table_name]
                formatted_command_list.append([row[0], row[1]])
            elif row[0] == 'SET': #SET [SET, dict{data}]
                command = row.pop(0)
                new_row = [command]
                row_item_type = []
                for index, item in enumerate(row):
                    if item == '=':
                        row_item_type[index - 1] = 'key'
                        row_item_type.append('=')
                    else:
                        row_item_type.append('value')
                print(f"row_item_type = {row_item_type}")
                key_list = []
                value_list = []
                value = ""
                index = 0
                while index < len(row_item_type):
                    if row_item_type[index] == 'key':
                        key_list.append(row[index])
                        index = index + 1
                    elif row_item_type[index] == 'value':
                        while ((index < len(row_item_type)) and (row_item_type[index] == 'value')):
                            value = ' '.join([value, row[index]])
                            index = index + 1
                        value_list.append(value)
                        value = ""
                    else:
                        index = index + 1
                for index, item in enumerate(value_list):
                    try:
                        value_list[index] = value_list[index].replace(" '","")
                    except ValueError as ex:
                        pass
                    try:
                        value_list[index] = value_list[index].replace("'","")
                    except ValueError as ex:
                        pass                
                set_dict = {}
                for index in range(0, len(key_list)):
                    set_dict[key_list[index]] = value_list[index]
                new_row.append(set_dict)
                formatted_command_list.append(new_row)
            elif row[0] == 'DELETE': #DELETE [DELETE]
                formatted_command_list.append([row[0]])




            #functions that need formmatting for the input
                #join [join, [other, column_on_db_a, filename_db_b, column_on_db_b]]
                
        # return list of commands in format [COMMAND, load_dictionary_arguments]
        return formatted_command_list


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
        print(f"command_list = {command_list}") #debug
        formatted_command_list = cli.transform_command_list(command_list)
        print(f"formatted_command_list = {formatted_command_list}") #debug
        cli.run_commands(formatted_command_list, request_object)
        request_object = MySqliteRequest()
        user_input = cli.print_prompt()


if __name__ == "__main__":
    main()