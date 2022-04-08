import csv
import mysql.connector

def write_to_blank_csv():
    with open('empty_csv.csv', 'w', newline='', encoding='utf-8') as newcsvfile:
        csv_writer = csv.writer(newcsvfile)
        header_row = ['fund_id', 'fund_name', 'fund_amount']
        csv_writer.writerow(header_row)
        data_rows = [('1', 'S&P500', '1000'), ('2', 'Technology', '2000')]
        csv_writer.writerows(data_rows)


def write_to_csv_data_from_db():
    # retrieve data from DB and write to csv file
    connection = mysql.connector.connect(host='lahman.csw1rmup8ri6.us-east-1.rds.amazonaws.com',
                                         user='python',
                                         passwd='python',
                                         db='lahmansbaseballdb'
                                         )

    query = """
            SELECT year(debut) AS year, avg(weight) AS weight
            FROM people
            WHERE debut is NOT NULL
            GROUP BY year(debut)
            ORDER BY year(debut)
            """

    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    connection.close()

    csv_file = 'weight-over-time.csv'

    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Year', 'Weight'])
        writer.writerows(results)



write_to_blank_csv()
write_to_csv_data_from_db()
