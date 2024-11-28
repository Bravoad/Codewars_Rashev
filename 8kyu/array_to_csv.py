"""
Create a function that returns the CSV representation of
 a two-dimensional numeric array.

Example:

input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]]

output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'"""


def to_csv_text(array: list) -> str:
    csv_list = []
    for arr in array:
        csv_list.append(','.join(map(str, arr)))
    return '\n'.join(csv_list)


print(to_csv_text([[1, 2, 3], [4, 5, 6]]))
