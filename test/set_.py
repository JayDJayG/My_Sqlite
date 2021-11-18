import sys
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing set command
test_class.__update__(nba_player_data)

data = {"name": "bob", "year_start": "2000"}

test_class.__set__(data)

# #Testing select_ command
# test_class.__select__("year_start")