from os import name
import sys

sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_players.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()
test_class_B = MySqliteRequest()
#testing from
test_class.fr0m(nba_player_data)

#Testing join command
# def __join__(self, other, column_on_db_a, filename_db_b, column_on_db_b):

test_class.join(test_class_B, "name", "nba_player.csv", "name")
#test_class.run()
#test_class.__repr__()

# Desired output -> 1 : {name: "Mammadu"}
