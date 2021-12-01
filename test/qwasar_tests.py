import sys
sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"


def q00():
    request = MySqliteRequest()
    request = request.__from__('nba_player_data.csv')
    request = request.__select__("name")
    request.run()

def q01():
    request = MySqliteRequest()
    request = request.__from__('nba_player_data.csv')
    request = request.__select__('name')
    request = request.__where__('college', 'University of California')
    request.run()

def q02():
    print("placeholder")

def main():
    # q00()
    q01()

if __name__ == "__main__":
    main()
