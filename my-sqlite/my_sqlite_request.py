from typing import ValuesView
import pandas as pd
from os.path import exists
import random
from pandas.core.base import SelectionMixin


class MySqliteRequest:
    def __init__(self):
        self.columns = []
        self.values_li = []
        self.columns_extracted = []
        self.run_dictionary = {}
        self.query_dictionary = {}
        self.data_location = '../data/'
        self.table = ""
        self.from_usage = False
        self.from_message = "Please use from_ method before any other command"
        self.path_message = "File path does not exist, introduce correct path"
        self.load_dictionary = {
            "__from__": []
            , "__update__": []
            , "__values__": []
            , "__insert__": []
            , "__order__": []
            , "__select__": []
            , "__where__": []
            , "__set__": []
            , "__delete__": []
            , "__join__": []
        }

    def __repr__(self):
        print(f"current state of query is {self.run_dictionary}")
        return

    def __from__(self, table_name):
        """
        from_ implements the sql FROM command, each request must have one.
        from_ will take a string(table_name) this is the name of the csv file to query.
        """
        csv_path = self.data_location + table_name  #create path
        if (exists(csv_path)):  #check file existence
            df = pd.read_csv(csv_path, sep=',')
            df = df.fillna("null")
            df = df.astype(str)
            tuples = [tuple(x) for x in df.values]
            self.columns = list(df.columns)

            for idx, val in enumerate(tuples):
                self.query_dictionary[idx] = {}
                for jdx, value in enumerate(val):
                    self.query_dictionary[idx][self.columns[jdx]] = value

            self.from_usage = True
        else:
            print(self.path_message)
        return self

    def __select__(self, string_s):
        """
        The select_ method implements the sql SELECT command. 
        It takes as the parameter a string OR an array of strings.
        It will continue to build the request. During the run()
        """
        if self.from_usage:

            if not isinstance(string_s, list):  #convert string to list
                s = string_s
                string_s = list()
                string_s.append(s)

            column_bool = True
            for column in string_s:
                if column not in self.columns:
                    column_bool = False
            if self.from_usage == True and column_bool:
                for idx in self.query_dictionary:
                    self.run_dictionary[idx] = {}
                    for column in string_s:
                        self.run_dictionary[idx][column] = self.query_dictionary[idx][column]
        else:
            print(self.from_message)
        return self

    def __where__(self, column_name, criteria):
        """
        The where_ method takes two arguments. column_name targets the column and
        criteria the condition to actuate by filtering the entries within run_dictionary.
        """
        if self.from_usage == True and column_name in self.columns:
            for entry in self.query_dictionary:
                if self.query_dictionary[
                        entry] and criteria != self.query_dictionary[entry][
                            column_name]:
                    self.run_dictionary[
                        entry] = None  #everything that isn't matching the criteria becomes none
        else:
            print(self.from_message)
        return self

    def __join__(self, other, column_on_db_a, filename_db_b, column_on_db_b):
        """
        The join_ method loads another filename_db
        and will join both database on an on column.
        """
        if (not self.run_dictionary):
            self.run_dictionary = self.query_dictionary

        db_B = MySqliteRequest()
        db_B.fr0m(filename_db_b)
        li_B = db_B.column_dict_list_extractor(column_on_db_b)

        if (li_B):
            for idx, val in enumerate(self.run_dictionary):
                if (self.run_dictionary[idx][column_on_db_a] in li_B):
                    jidx = li_B[self.run_dictionary[idx][column_on_db_a]]
                    for val in db_B.query_dictionary[jidx]:
                        self.run_dictionary[idx][val] = db_B.query_dictionary[
                            jidx][val]
                    self.run_dictionary[idx].pop('Unnamed: 0', None)
        else:
            print("Join failed")

        return self

    def __order__(self, order, column_name):
        """
        Order Implement an order method which will received two parameters, 
        order (:asc or :desc) and column_name. 
        It will sort depending on the order base on the column_name.
        """
        temp_d = {}
        tup = []
        oP = ["asc", "desc"]
        if self.from_usage and column_name in self.columns and order in oP:

            for key, val in self.query_dictionary.items():
                tup.append((key, val[column_name]))

            if order in "asc":
                temp = sorted(tup, reverse=False, key=lambda x: x[1])
            else:
                temp = sorted(tup, reverse=True, key=lambda x: x[1])

            for idx, val in enumerate(temp):
                temp_d[idx] = self.run_dictionary[val[0]]

            self.run_dictionary = temp_d
        else:
            print(self.from_message)

        return self

    def __insert__(self, table_name):
        """
        Insert Implement a method to insert which will receive a table name (filename).
        It will continue to build the request.
        """
        self = self.__from__(table_name)
        length = len(self.query_dictionary)
        self.query_dictionary[length] = {}
        for item in self.values_li:
            key = list(item.keys())[0]
            value = list(item.values())[0]
            self.query_dictionary[length][key] = value
        return self
        #each call of insert will be a row. If values for each column aren't provided they be come None

    def __values__(self, data):
        """
        Values Implement a method to values which will receive data.
        (a hash of data on format (key => value)).
        It will continue to build the request. During the run() you do the insert.
        """
        if type(data) == list:
            for kv in data:
                if type(kv) == dict:
                    self.values_li.append(kv)
        else:
            print("Right data format [{'name':'Gaetan'},{'lastname':'Juvin'}]")
        return self

    def __update__(self, table_name):
        """
        Update Implement a method to update which will receive a table name (filename).
        It will continue to build the request.
        An update request might be associated with a where request
        """
        self.table = table_name
        self.__from__(table_name)
        return self
        #update the query dictionary with the proper database

    def __set__(self, data):
        """
        Set Implement a method to update which will receive data
        (a hash of data on format (key => value)). 
        It will perform the update of attributes on all matching row.
        An update request might be associated with a where request.
        """

        #update run dictionary with new values
        for key in data.keys():
            for idx in self.run_dictionary:
                if self.run_dictionary[idx] == None:
                    continue
                else:
                    self.run_dictionary[idx][key] = data[key]
        #update query dictionary from run dictionary
        for idx in self.run_dictionary:
            if self.run_dictionary[idx] == None:
                continue
            else:
                for key in self.run_dictionary[idx]:
                    self.query_dictionary[idx][key] = self.run_dictionary[idx][
                        key]

        #update csv file from new query dictionary
        df = pd.DataFrame(self.query_dictionary[value]
        for value in self.query_dictionary)
        df.to_csv(f"{self.data_location}/{self.table}")

        #for any update block, the logic is as follows:
        # UPDATE
        # WHERE (as necessary)
        # SET
        
        #values and where need one instance of the column when using set

    def __delete__(self):
        """
        Delete Implement a delete method. 
        It set the request to delete on all matching row. 
        It will continue to build the request. 
        An delete request might be associated with a where request.
        """
    
    def __load__(self):
        for key in self.load_dictionary.keys():
            for args in self.load_dictionary[key]:
                try:
                    getattr(self, key)(*args)
                except TypeError:
                    getattr(self, key)(args)



    def __run__(self):
        """
        Prints the product of the query to the console
        """
        #complete self.run
        # self.run_value()
        #UNCOMMENT
        for idx in self.run_dictionary:
            row = ""
            if self.run_dictionary[idx]:
                for column_value in self.run_dictionary[idx]:
                    row += self.run_dictionary[idx][column_value] + " "
                print(row)

    #Helper Functions
    def run_value(self):
        print(self.columns)
        for d in self.values_li:
            for key, value in d.items():
                print(key)
                print(value)

    def column_extractor(self):
        """
        Supports run function in a way columns can be obtained
        befores printing, formatting is not included on function
        """
        choice = random.choice(list(self.run_dictionary.values()))
        li = []
        for key in choice:
            li.append(key)
        return li

    def column_dict_list_extractor(self, column_on_db):
        """
        Supports join function, creates a dictionary 
        where k = column value and v = k where value 
        was allocated
        """

        li = {}
        for idx, val in enumerate(self.query_dictionary):
            li[self.query_dictionary[idx][column_on_db]] = idx
        return li

    #End Helper Function

    def run(self):
        self.__load__()
        return self.__run__()

    def fr0m(self, table_name):
        # return self.__from__(table_name)
        self.load_dictionary["__from__"].append(table_name)
        return self
    
    def where(self, column_name, criteria):
        self.load_dictionary["__where__"].append([column_name, criteria])
        return self

    def order(self, order, column_name):
        # return self.__order__(order, column_name)
        self.load_dictionary["order"].append([order, column_name])

    def join(self, other, column_on_db_a, filename_db_b, column_on_db_b):
        return self.__join__(other, column_on_db_a, filename_db_b,
                             column_on_db_b)

    def select(self, string_s):
        # return self.__select__(string_s)
        self.load_dictionary["__select__"].append(string_s)
        return self

    def values(self, data):
        self.load_dictionary["__values__"].append(data)
        return self

    def insert(self, table_name):
        self.load_dictionary["__insert__"].append(table_name)
        return self
