import sys
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing from
test_class.from_(nba_player_data)

#Testing select_ command
test_class.select_(["birth_date", "name"])
test_class.where_("name", "Jim Zoet")
test_class.where_("birth_date", "December 20, 1953")



# Desired output -> 1 : {name: "Mammadu"}
