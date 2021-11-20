from os import name
import sys

sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing from
test_class.fr0m(nba_player_data)

#Testing select_ command
test_class.__select__(["name", "year_start", "position"])

li = test_class.column_list_extractor("name")
print(li)

#test_class.run()
#test_class.__repr__()

# Desired output -> 1 : {name: "Mammadu"}
