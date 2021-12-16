from os import name
import sys
import pathlib

dirname = str(pathlib.Path(__file__).resolve().parent.parent.joinpath('my-sqlite'))
sys.path.insert(0, dirname)

# sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_players.csv"

#Instance of MySqliteRequest class
test_class = MySqliteRequest()
test_class_B = MySqliteRequest()
#testing from
test_class.FROM(nba_player_data)
test_class.SELECT(["name", "college"])

#Testing join command
# def __join__(self,column_on_db_a, filename_db_b, column_on_db_b):

test_class.JOIN("name", "nba_players.csv", "Player")
test_class.run()
#test_class.__repr__()

# Desired output -> 1 : {name: "Mammadu"}
