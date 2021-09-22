class MySqliteRequest:
    #Constructor It will be prototyped:
    query_dictionary = {}

    def __repr__(self):
        print(f"current state of query is {self.query_dictionary}")
        return "end of query"

    def from_(self, table_name):
        """
        From Implement a from method which must be present on each request.
        From will take a parameter and it will be the name of the table.
        (technically a table_name is also a filename (.csv))
        """

    def select(self, column_name_a, column_name_b):
        """
        Select Implement a where method which will take one argument a string OR an array of string.
        It will continue to build the request. During the run()
        you will collect on the result only the columns sent as parameters to select :-).
        """

    def where(self, column_name, criteria):
        """
        Where Implement a where method which will take 2 arguments: column_name and value.
         It will continue to build the request.
         During the run() you will filter the result which match the value.
        """

    def join(self, column_on_db_a, filename_db_b, column_on_db_b):
        """
        Join Implement a join method which will load another filename_db 
        and will join both database on a on column.
        """

    def order(self, order, column_name):
        """
        Order Implement an order method which will received two parameters, 
        order (:asc or :desc) and column_name. 
        It will sort depending on the order base on the column_name.
        """

    def insert(self, table_name):
        """
        Insert Implement a method to insert which will receive a table name (filename).
        It will continue to build the request.
        """
    def values(self, data):
        """
        Values Implement a method to values which will receive data.
        (a hash of data on format (key => value)).
        It will continue to build the request. During the run() you do the insert.
        """
    def update(self, table_name):
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

    def delete(self):
        """
        Delete Implement a delete method. 
        It set the request to delete on all matching row. 
        It will continue to build the request. 
        An delete request might be associated with a where request.
        """
    def run(self):
        print("HELLO")
