import sys
import os
import pathlib
dirname = str(pathlib.Path(__file__).resolve().parent.parent.joinpath('my-sqlite'))
# dirname = os.path.dirname(__file__)[:-4] + "my-sqlite"
sys.path.insert(0, dirname)
print(sys.path)

from my_sqlite_request import MySqliteRequest


nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"


def q00(): #Part I - Does it work to SELECT name from nba player data?
    request = MySqliteRequest()
    request = request.FROM('nba_player_data.csv')
    request = request.SELECT("name")
    request.run()

def q01(): #Part I - Does it work to select name from nba player data with a where?
    request = MySqliteRequest()
    request = request.FROM('nba_player_data.csv')
    request = request.SELECT('name')
    request = request.WHERE('college', 'University of California')
    request.run()

def q02(): #Part I - Does it work to SELECT name from nba player data with multiple where?
    request = MySqliteRequest()
    request = request.FROM('nba_player_data.csv')
    request = request.SELECT('name')
    request = request.WHERE('college', 'University of California')
    request = request.WHERE('year_start', '1997')
    request.run()

def q03(): #Part I - Does it work to INSERT a nba player?
    request = MySqliteRequest()
    request = request.INSERT('nba_player_data.csv')
    # request = request.__values__("'name' => 'Alaa Abdelnaby', 'year_start' => '1991', 'year_end' => '1995', 'position' => 'F-C', 'height' => '6-10', 'weight' => '240', 'birth_date' => 'June 24, 1968', 'college' => 'Duke University'")
    request = request.VALUES([{'name': 'Alaa Abdelnaby'}, {'year_start': '1991'}, {'year_end': '1995'}, {'position': 'F-C'}, {'height': '6-10'}, {'weight': '240'}, {'birth_date': 'June 24, 1968'}, {'college': 'Duke University'}])
    request.run()

def q04(): #Part I - Does it work to UPDATE a nba player?
    request = MySqliteRequest()
    request = request.UPDATE('nba_player_data.csv') #should this actually be the SET function?
    request = request.SET([{'name': 'Alaa Renamed'}])
    request = request.WHERE('name', 'Alaa Abdelnaby')
    request.run()

def q05(): #Part I - Does it work to DELETE a nba player?
    request = MySqliteRequest()
    request = request.DELETE()
    request = request.FROM('nba_player_data.csv')
    request = request.WHERE('name', 'Alaa Abdelnaby')
    request.run()

# def q06(): #Part II -  Mysqlite cli simple select
#     SELECT * FROM nba_player_data.csv

# def q07(): #Part II - Mysqlite cli select specific field with where
    # SELECT name,college FROM nba_player_data.csv WHERE college = 'University of California'

# def q08(): #Part II - Mysqlite cli simple insert
#     INSERT INTO nba_player_data.csv VALUES ('Alaa Abdelnaby', '1991', '1995', 'F-C', '6-10', '240', 'June 24, 1968', 'Duke University')

# def q09(): #Part II -  Mysqlite cli simple update
#     UPDATE nba_player_data.csv SET name = 'bob', college = 'South Hampton Institute of Technology' WHERE position = 'C'

# def q10(): #Part II - Mysqlite cli simple delete
#     DELETE FROM nba_player_data.csv WHERE name = 'Matt Zunic'


def main():
    # q00()
    # q01()
    q02()
    # q03()
    # q04()
    # q05()
    # q06()
    # q07()
    # q08()
    # q09()
    # q10()

if __name__ == "__main__":
    main()
