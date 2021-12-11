import sys
sys.path.insert(0, '../my-sqlite')
# print(sys.path)
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"


def q00(): #Part I - Does it work to select name from nba player data?
    request = MySqliteRequest()
    request = request.fr0m('nba_player_data.csv')
    request = request.select("name")
    request.run()

def q01(): #Part I - Does it work to select name from nba player data with a where?
    request = MySqliteRequest()
    request = request.fr0m('nba_player_data.csv')
    request = request.select('name')
    request = request.where('college', 'University of California')
    request.run()

def q02(): #Part I - Does it work to select name from nba player data with multiple where?
    request = MySqliteRequest()
    request = request.fr0m('nba_player_data.csv')
    request = request.select('name')
    request = request.where('college', 'University of California')
    request = request.where('year_start', '1997')
    request.run()

def q03(): #Part I - Does it work to insert a nba player?
    request = MySqliteRequest()
    request = request.insert('nba_player_data.csv')
    # request = request.__values__("'name' => 'Alaa Abdelnaby', 'year_start' => '1991', 'year_end' => '1995', 'position' => 'F-C', 'height' => '6-10', 'weight' => '240', 'birth_date' => 'June 24, 1968', 'college' => 'Duke University'")
    request = request.values([{'name': 'Alaa Abdelnaby'}, {'year_start': '1991'}, {'year_end': '1995'}, {'position': 'F-C'}, {'height': '6-10'}, {'weight': '240'}, {'birth_date': 'June 24, 1968'}, {'college': 'Duke University'}])
    request.run()

def q04(): #Part I - Does it work to update a nba player?
    request = MySqliteRequest()
    request = request.update('nba_player_data.csv') #should this actually be the set function?
    request = request.set([{'name': 'Alaa Renamed'}])
    request = request.where('name', 'Alaa Abdelnaby')
    request.run()

def q05(): #Part I - Does it work to delete a nba player?
    request = MySqliteRequest.new
    request = request.__delete__()
    request = request.fr0m('nba_player_data.csv')
    request = request.__where__('name', 'Alaa Abdelnaby')


    request.run()

# def q06(): #Part II - Can you run this request in the CLI?

# def q07(): #Part II - Can you run this request in the CLI?

# def q08(): #Part II - Can you run this request in the CLI?

# def q09(): #Part II - Can you run this request in the CLI?

# def q10(): #Part II - Can you run this request in the CLI?


def main():
    # q00()
    # q01()
    # q02()
    # q03()
    q04()
    # q05()
    # q06()
    # q07()
    # q08()
    # q09()
    # q10()

if __name__ == "__main__":
    main()
