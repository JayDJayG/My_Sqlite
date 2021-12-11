import sys
import pytest

sys.path.insert(0, '../my-sqlite')
from my_sqlite_request import MySqliteRequest

nba_player_data = "nba_player_data.csv"
nba_player = "nba_player.csv"


def test_prep():
    test_classy = MySqliteRequest()
    test_classy = test_classy.__from__("nba_player_data.csv")
    test_classy = test_classy.__select__("year_start")
    stry = str(test_classy.run_dictionary)
    return stry


#Instance of MySqliteRequest class
test_class = MySqliteRequest()

#testing from
test_class = test_class.__from__(nba_player_data)

#Testing select_ command
test_class = test_class.__select__("year_start")

str1 = str(test_class.run_dictionary)


def test_y():

    assert str1 == test_prep(), "HOLA"


#test_class.__repr__()

# Desired output -> 1 : {name: "Mammadu"}
