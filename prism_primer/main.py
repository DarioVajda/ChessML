
# TDD prezentacija na ytu


import math

#region alfa, sigma

# number of possible answers for the questions
alfa = [ 3, 2, 2, 2 ] 

# number of classifications
sigma = 3

#endregion

dataSet = [
    { "input": [ 1, 1, 1, 1 ], "classification": 3 },
    { "input": [ 1, 1, 1, 2 ], "classification": 2 },
    { "input": [ 1, 1, 2, 1 ], "classification": 3 },
    { "input": [ 1, 1, 2, 2 ], "classification": 1 },
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

#region p sigma

pSigma = [0, 0, 0]
for element in dataSet:
    pSigma[element['classification'] - 1] += 1
for i in range(0, 3):
    pSigma[i] = pSigma[i] / len(dataSet)
print(pSigma)

# endregion

def pSigmaAlfa(sigma, alfa, alfaValue):
    _filtered = filter(lambda x: (x["input"][alfa-1] == alfaValue), dataSet)
    filtered = []
    
    for element in _filtered:
        filtered.append(element)

    res = 1 / len(filtered)

    countSigma = 0
    for element in filtered:
        # print(element, 'sigma', sigma, 'alfaValue', alfaValue)
        if element["classification"] == sigma:
            countSigma += 1

    res *= countSigma

    return res

def iSigma(sigma):
    return math.log(1/pSigma[sigma], 2)

def iSigmaAlfa(sigma, alfa, alfaValue):
    psa = pSigmaAlfa(sigma, alfa, alfaValue)
    if(psa == 0):
        return -10000
    else:
        return math.log(psa / pSigma[sigma], 2)


#region ALGORITHM

rules = []
for i in range(0, 3):
    pSigma = [0, 0, 0]
    
    sigmaInfo = iSigma(i)
    
    # _list = filter(lambda x: x["classification"] == i+1, dataSet)

    list = []

    for j in range(0, len(alfa)):
        for k in range(0, alfa[j]):
            list.append({ "alfa": j, "alfaValue": k, "info": pSigmaAlfa(i+1, j+1, k+1) })
    
    list.sort(key=lambda x: x['info'], reverse=True)

    totalInfo = 0
    index = 0
    ruleList = []
    print(sigmaInfo)
    while totalInfo < sigmaInfo:
        for element in dataSet:
            pSigma[element['classification'] - 1] += 1
        for i in range(0, 3):
            pSigma[i] = pSigma[i] / len(dataSet)

        print(list[index], list[index]["info"], index, totalInfo)
        ruleList.append({ "alfa": list[index]["alfa"], "value": list[index]["alfaValue"]})
        totalInfo += list[index]["info"] # TREBA DA SE GLEDA P, A NE I OVDE I TO DA SE SABIRA
        index += 1

        dataSet = dataSet.filter(lambda x: x["input"][list[index]["alfa"]-1] != list[index]["alfaValue"])
    
    rules.append({ "rules": ruleList, "classification": i+1 })


for rule, i in zip(rules, range(1, 4)):
    print(i)
    for element in rule["rules"]:
        print(element)
    # print(rule["classification"])
    print()



#endregion

