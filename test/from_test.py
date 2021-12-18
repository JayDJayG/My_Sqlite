import sys

sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing from
test_class = test_class.FROM(nba_player_data)

test_class = test_class.SELECT("name")

test_class.run()
