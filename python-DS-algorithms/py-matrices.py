# what is matrix data type?
# what is the use of it?
# it is special case of the 2-D dimentional array data type where each element in the array is of strictly the same size
# it is often used for mathematical and scientific calculation

# example: create a 7x5 matrix of recording temperature for 1 week
from numpy import *

temp_in_a_week = array([['Mon', 18, 20, 22, 17], ['Tue', 11, 18, 21, 18],
                        ['Wed', 15, 21, 20, 19], ['Thu', 11, 20, 22, 21],
                        ['Fri', 18, 17, 23, 22], ['Sat', 12, 22, 20, 18],
                        ['Sun', 13, 15, 19, 16]])

reshape_temp_matrix = reshape(temp_in_a_week, (7, 5))

# how to add a row to a matrix?
temp_matrix = reshape_temp_matrix.copy()
avg_temp_matrix = append(temp_matrix, [['Avg', 12, 15, 13, 11]], 0)

# how to add a column to a matrix?
new_matrix = reshape_temp_matrix.copy()
extra_col_matrix = insert(new_matrix, 5, ["sunny", "rainy", "mostly sunny", "snow", "ice", "fog", "drizzle"], axis=1)

# how to delete a row or a column in a matrix?
alpha_matrix = reshape_temp_matrix.copy()
sunday_removed_matrix = delete(alpha_matrix, [6], axis=0)
days_removed_matrix = delete(alpha_matrix, [0], axis=1)

# how to update values in a row or a column?
# re-assign the values at the index of the row in the matrix
beta_matrix = reshape_temp_matrix.copy()
beta_matrix[6] = ['Sun', -1, -1, -1, -1]

if __name__ == "__main__":
    print(reshape_temp_matrix)
    print("-----------------")
    print("print data from Tue morning (expected 11): ", reshape_temp_matrix[1][1])  # access values in a matrix
    print("-----------------")
    print("print data from entire Sun: ", reshape_temp_matrix[6])  # access values in a matrix
    print("-----------------")
    print("new matrix after adding a row: ", avg_temp_matrix)
    print("-----------------")
    print("new matrix after adding a column: ", extra_col_matrix)
    print("-----------------")
    print("new matrix after removing sun row : ", sunday_removed_matrix)
    print("-----------------")
    print("new matrix after removing days column : ", days_removed_matrix)
    print("-----------------")
    print("new matrix after updating Sun values : ", beta_matrix)
