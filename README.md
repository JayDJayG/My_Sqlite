# My-sqlite
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Prerequisites](#prerequisites)

## General info

My-sqlite program works as a functional SQL engine and CLI, implementing the following SQL commands:

UPDATE, VALUES, INSERT, ORDER, SELECT, WHERE, DELETE, SET, and JOIN.

All the Commands above are implemented in my_sqlite_request.py within the MySqliteRequest class.
The My-sqlite CLI is implemented in my_sqlite_cli.py within the CLI class.

Altogether serves the purpose to query, update, delete, and in general manipulate csv files that function as databases.
## Technologies

Built with LOVE and the use of:
Python 3.9.9
pandas >= 1.2.4
pytest >= 6.2.5

## Setup

To run this project use make:

$>make

## Prerequisites

Please make sure you have installed Python3 and pip installed on your computer.