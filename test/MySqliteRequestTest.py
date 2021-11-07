import sys
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

#main data srcs
nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#prints generic output of MySqLiteRequest class
print(test_class)
