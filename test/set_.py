import sys
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

import time

nba_player_data = "nba_player_data.csv"
nba_players = "nba_players.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing set command
test_class.__update__(nba_player_data)
test_class.__select__(["name", "position"])

data = {"name": "bob"}

test_class.__where__("position", "G")

test_class.__set__(data)

print(test_class.query_dictionary)
# test_class.__repr__()
# test_class.run()

# #Testing select_ command
# test_class.__select__("year_start")