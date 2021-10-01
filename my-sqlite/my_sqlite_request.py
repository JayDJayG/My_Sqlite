import pandas as pd
from os.path import exists

class MySqliteRequest:

    def __init__(self):
        self.columns = []
        self.run_dictionary = {}
        self.query_dictionary = {}
        self.data_location = '../data/'
        self.from_usage = False
        self.from_message = "Please use from_ method before any other command"
        self.path_message = "File path does not exist, introduce correct path"

    def __repr__(self):
        print(f"current state of query is {self.query_dictionary}")
        return

    def from_(self, table_name):
        """
        from_ implements the sql FROM command, each request must have one.
        from_ will take a string(table_name) this is the name of the csv file to query.
        """
        csv_path = self.data_location + table_name
        if (exists(csv_path)):
            df = pd.read_csv(csv_path, sep = ',')
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

    def select_(self, string_s):
        """
        The select_ method implements the sql SELECT command. 
        It takes as the parameter a string OR an array of strings.
        It will continue to build the request. During the run()
        """
        if self.from_usage:
            if not isinstance(string_s, list):
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
            print (self.from_message)

    def where_(self, column_name, criteria):
        """
        The where_ method takes two arguments. column_name targets the column and
        criteria the condition to actuate by filtering the entries within run_dictionary.
        """
        if self.from_usage == True and column_name in self.columns:
            for entry in self.run_dictionary:
                if self.run_dictionary[entry] and criteria not in self.run_dictionary[entry][column_name]:
                    self.run_dictionary[entry] = None
        else:
            print (self.from_message)

    def join_(self, column_on_db_a, filename_db_b, column_on_db_b):
        """
        The join_ method loads another filename_db
        and will join both database on an on column.
        """

    def order_(self, order, column_name):
        """
        Order Implement an order method which will received two parameters, 
        order (:asc or :desc) and column_name. 
        It will sort depending on the order base on the column_name.
        """

    def insert_(self, table_name):
        """
        Insert Implement a method to insert which will receive a table name (filename).
        It will continue to build the request.
        """
    def values_(self, data):
        """
        Values Implement a method to values which will receive data.
        (a hash of data on format (key => value)).
        It will continue to build the request. During the run() you do the insert.
        """
    def update_(self, table_name):
        """
        Update Implement a method to update which will receive a table name (filename).
        It will continue to build the request.
        An update request might be associated with a where request
        """
    def set_(self, data):
        """
        Set Implement a method to update which will receive data
        (a hash of data on format (key => value)). 
        It will perform the update of attributes on all matching row.
        An update request might be associated with a where request.
        """

    def delete_(self):
        """
        Delete Implement a delete method. 
        It set the request to delete on all matching row. 
        It will continue to build the request. 
        An delete request might be associated with a where request.
        """
    def run_(self):
        print("HELLO")
