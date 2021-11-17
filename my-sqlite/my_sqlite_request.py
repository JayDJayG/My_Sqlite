import pandas as pd
import math
from os.path import exists
import random
from pandas.core.base import SelectionMixin


class MySqliteRequest:
    def __init__(self):
        self.columns = []
        self.columns_extracted = []
        self.run_dictionary = {}
        self.query_dictionary = {}
        self.data_location = '../data/'
        self.from_usage = False
        self.from_message = "Please use from_ method before any other command"
        self.path_message = "File path does not exist, introduce correct path"

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
            return self.query_dictionary
        else:
            print(self.path_message)

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
                        self.run_dictionary[idx][
                            column] = self.query_dictionary[idx][column]
        else:
            print(self.from_message)

    def __where__(self, column_name, criteria):
        """
        The where_ method takes two arguments. column_name targets the column and
        criteria the condition to actuate by filtering the entries within run_dictionary.
        """
        if self.from_usage == True and column_name in self.columns:
            for entry in self.run_dictionary:
                # print(entry) #debug
                # print(self.run_dictionary[entry]) #debug
                if self.run_dictionary[
                        entry] and criteria != self.run_dictionary[entry][
                            column_name]:
                    self.run_dictionary[entry] = None
        else:
            print(self.from_message)

    def __join__(self, other, column_on_db_a, filename_db_b, column_on_db_b):
        """
        The join_ method loads another filename_db
        and will join both database on an on column.
        """

    def __order__(self, order, column_name):
        """
        Order Implement an order method which will received two parameters, 
        order (:asc or :desc) and column_name. 
        It will sort depending on the order base on the column_name.
        """
        oP = ["asc", "desc"]
        if self.from_usage and column_name in self.columns and order in oP:
            index = self.columns.index(column_name)

            if order in "asc":
                print("ASCENDANT for sure")
                d = dict(
                    sorted(self.query_dictionary.items(),
                           key=lambda item: item[index]))
            else:
                d = dict(
                    sorted(self.query_dictionary.items(),
                           key=lambda item: item[index]))

            #print(sorted_df)
            print(self.column_extractor())
        #next step to is self.column_extractor() to finish query

        else:
            print(self.from_message)

    def order(self, order, column_name):
        return self.__order__(order, column_name)

    def __insert__(self, table_name):
        """
        Insert Implement a method to insert which will receive a table name (filename).
        It will continue to build the request.
        """

    def __values__(self, data):
        """
        Values Implement a method to values which will receive data.
        (a hash of data on format (key => value)).
        It will continue to build the request. During the run() you do the insert.
        """

    def __update__(self, table_name):
        """
        Update Implement a method to update which will receive a table name (filename).
        It will continue to build the request.
        An update request might be associated with a where request
        """

    def __set__(self, data):
        """
        Set Implement a method to update which will receive data
        (a hash of data on format (key => value)). 
        It will perform the update of attributes on all matching row.
        An update request might be associated with a where request.
        """

    def __delete__(self):
        """
        Delete Implement a delete method. 
        It set the request to delete on all matching row. 
        It will continue to build the request. 
        An delete request might be associated with a where request.
        """

    def __run__(self):

        for idx in self.run_dictionary:
            row = ""
            if self.run_dictionary[idx]:
                for column_value in self.run_dictionary[idx]:
                    row += self.run_dictionary[idx][column_value] + " "
                print(row)

    def column_extractor(self):

        choice = random.choice(list(self.run_dictionary.values()))
        li = []
        for key in choice:
            li.append(key)
        return li

    def run(self):
        return self.__run__()

    def fr0m(self, table_name):
        return self.__from__(table_name)
