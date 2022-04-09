import csv


def write_to_csv_with_dict_writer():
    funds_dict = [{'fund_id': 1, 'fund_type': 'stock', 'fund_return': '30%', 'fund_term': '30 years'},
                  {'fund_id': 2, 'fund_type': 'bond', 'fund_return': '5%', 'fund_term': '55 years'}
                  ]

    with open('funds_info_dict.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = funds_dict[0].keys()
        dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        dict_writer.writeheader()
        dict_writer.writerows(funds_dict)


def append_to_csv_with_dict_writer():
    new_funds_dict = [{'fund_id': 10, 'fund_type': 'income', 'fund_return': '15%', 'fund_term': '10 years'},
                      {'fund_id': 20, 'fund_type': 'cryptocurrency', 'fund_return': '99%', 'fund_term': '100 years'}
                      ]

    with open('funds_info_dict.csv', 'a', newline='', encoding='utf-8') as csvfile:
        fieldnames = new_funds_dict[0].keys()
        dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        dict_writer.writerows(new_funds_dict)


write_to_csv_with_dict_writer()
append_to_csv_with_dict_writer()
