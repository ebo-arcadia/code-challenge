# what is the function or purpose of partial?
# as a developer, I want to do less work in the future
# partial allows reusing of a function with modification
# in other words, it makes a function re-usuable and can be customized
# a good use case is to analyze retail data

import pandas as pandas
from functools import partial

transaction_ids = [1000, 1001, 1002, 1003]
item_ids = ['python 101', 'angular 101', 'javascript 101', 'tensor flow 101']
sales_amount = [None, 90, 122, 312]
quantity_sold = [1, 2, None, 4]
item_cost = [None, 13, 41, None]

dataframe = pandas.DataFrame({
    'trans_id': transaction_ids,
    'item_id': item_ids,
    'sales_amount': sales_amount,
    'quantity_dols': quantity_sold,
    'item_cost': item_cost
})

def drop_null_values(data, target_column, item_column):
    null_items = set(data[data[target_column].isnull()[item_column]])
    print(f"Null values present in {null_items}")
    return data.dropna(subset=target_column)


drop_nulls_custom = partial(drop_null_values, data=dataframe, item_column='item_id')

drop_nulls_custom(target_column='item_cost')
