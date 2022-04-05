# mySQl vs sqlite
# sqlite is server-less DB, stored as files, light-weight, can be transferred among computers
# sqlite is good for not too large set of data

import sqlite3

def fetch_with_sqlite3():
    connection = sqlite3.connect('baseballDB.sqlite')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    query = f"""SELECT p.nameFirst, p.nameLast, b.HR, t.name AS team, b.yearID
            FROM batting b
            JOIN people p ON p.playerID = b.playerID JOIN teams t ON t.ID = b.team_ID
            WHERE b.yearID = ? 
            ORDER BY b.HR DESC
            LIMIT 4;"""

    checking = True
    while checking:
        year_id = int(input('Enter a year (0 to quit): '))
        if year_id == 0:
            break

        cursor.execute(query, [year_id])

        results = cursor.fetchall()

        for i, result in enumerate(results, 1):
            name = f"{result['nameFirst']} {result['nameLast']}"
            print(f"{i}. {name}: {result['HR']}")

    cursor.close()
    connection.close()

fetch_with_sqlite3()