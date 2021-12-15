import sys

sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"

request = MySqliteRequest()
request = request.DELETE()
request = request.__from__('nba_player_data.csv')
request = request.WHERE('name', 'Alaa Abdelnaby')
request.run()

print(list(request.run_dictionary.keys())[-1] + 1)
