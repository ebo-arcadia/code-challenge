import csv

csv_file_path = 'state_population_2021.csv'

# with open(csv_file_path, newline='', encoding = "ISO-8859-1") as csvfile:
#     populations = csv.reader(csvfile)
#     for row in populations:
#         print(', '.join(row))

with open(csv_file_path, newline='', encoding="ISO-8859-1") as csvfile:
    populations = csv.DictReader(csvfile)
    print('headers:', populations.fieldnames)
    for row in populations:
        pop_2020 = int(row['POPESTIMATE2020'].replace(',', ''))
        pop_2021 = int(row['POPESTIMATE2021'].replace(',', ''))

        pop_change = pop_2021 - pop_2020

        print(f"{row['CTYNAME']}: {pop_2021:,} - {pop_2020:,} = {pop_change:,}")