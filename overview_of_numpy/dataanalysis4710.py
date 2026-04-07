import numpy as np

# create a table to hold the medals table

medal_table = np.array(

[

[1,39,41,33],

[2,38,32,18],

[3,27,14,17],

[4,22,21,22],

[5,20,28,23]

]

)

print(medal_table)

for x in medal_table:
    print(x[1:])

for y in medal_table:
    print
