from datetime import date
from operator import itemgetter


def sort_by_fname_with_lambda(ww2_leaders):
    ww2_leaders.sort(key=lambda leader: leader['fname'])
    print(ww2_leaders, sep="\n")


def sort_by_name_with_itemgetter(ww2_leaders):
    ww2_leaders.sort(key=itemgetter('fname', 'lname'), reverse=True)
    print(ww2_leaders, sep="\n")


if __name__ == "__main__":
    ww2_leaders = [{'fname': 'Winston', 'lname': 'Churchill', 'dob': date(1889, 4, 20)},
                   {'fname': 'Charles', 'lname': 'de Gaulle', 'dob': date(1883, 7, 29)},
                   {'fname': 'Adolph', 'lname': 'Hitler', 'dob': date(1890, 11, 22)},
                   {'fname': 'Benito', 'lname': 'Mussolini', 'dob': date(1882, 1, 30)},
                   {'fname': 'Franklin', 'lname': 'Roosevelt', 'dob': date(1884, 12, 30)},
                   {'fname': 'Joseph', 'lname': 'Stalin', 'dob': date(1878, 12, 18)},
                   {'fname': 'Hideki', 'lname': 'Tojo', 'dob': date(1874, 11, 30)}]
    sort_by_fname_with_lambda(ww2_leaders)
    print("*" * 70)
    sort_by_name_with_itemgetter(ww2_leaders)
    print("*" * 70)

