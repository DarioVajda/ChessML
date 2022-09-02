import math

sigma = 3 # number of classifications

alfa = [ 3, 2, 2, 2 ]

dataSet = [
    { "input": [ 1, 1, 1, 2 ], "classification": 2 },
    { "input": [ 1, 1, 1, 1 ], "classification": 3 },
    { "input": [ 1, 1, 2, 2 ], "classification": 1 },
    { "input": [ 1, 1, 2, 1 ], "classification": 3 },
    { "input": [ 1, 2, 1, 1 ], "classification": 3 },
    { "input": [ 1, 2, 1, 2 ], "classification": 2 },
    { "input": [ 1, 2, 2, 1 ], "classification": 3 },
    { "input": [ 1, 2, 2, 2 ], "classification": 1 },
    { "input": [ 2, 1, 1, 1 ], "classification": 3 },
    { "input": [ 2, 1, 1, 2 ], "classification": 2 },
    { "input": [ 2, 1, 2, 1 ], "classification": 3 },
    { "input": [ 2, 1, 2, 2 ], "classification": 1 },
    { "input": [ 2, 2, 1, 1 ], "classification": 3 },
    { "input": [ 2, 2, 1, 2 ], "classification": 2 },
    { "input": [ 2, 2, 2, 1 ], "classification": 3 },
    { "input": [ 2, 2, 2, 2 ], "classification": 3 },
    { "input": [ 3, 1, 1, 1 ], "classification": 3 },
    { "input": [ 3, 1, 1, 2 ], "classification": 3 },
    { "input": [ 3, 1, 2, 1 ], "classification": 3 },
    { "input": [ 3, 1, 2, 2 ], "classification": 1 },
    { "input": [ 3, 2, 1, 1 ], "classification": 3 },
    { "input": [ 3, 2, 1, 2 ], "classification": 2 },
    { "input": [ 3, 2, 2, 1 ], "classification": 3 },
    { "input": [ 3, 2, 2, 2 ], "classification": 3 }
]


"""

for sigma:
    reset dataSet;
    while there are sigma classification elements in dataSet:
        

"""