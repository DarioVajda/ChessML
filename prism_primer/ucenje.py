import math



sigma = 3 # number of classifications

alfa = [ 3, 2, 2, 4 ]

def getDataSet():
    return [
        { "input": [ 1, 1, 1, 1 ], "classification": 3 },
        { "input": [ 1, 1, 1, 2 ], "classification": 2 },
        { "input": [ 1, 1, 1, 3 ], "classification": 2 }, ###################
        { "input": [ 1, 1, 1, 4 ], "classification": 3 }, #__________________
        { "input": [ 1, 1, 2, 1 ], "classification": 3 },
        { "input": [ 1, 1, 2, 2 ], "classification": 1 },
        { "input": [ 1, 1, 2, 3 ], "classification": 2 }, ###################
        { "input": [ 1, 1, 2, 4 ], "classification": 3 }, #__________________
        { "input": [ 1, 2, 1, 1 ], "classification": 3 },
        { "input": [ 1, 2, 1, 2 ], "classification": 2 },
        { "input": [ 1, 2, 1, 3 ], "classification": 2 }, ###################
        { "input": [ 1, 2, 1, 4 ], "classification": 3 }, #__________________
        { "input": [ 1, 2, 2, 1 ], "classification": 3 },
        { "input": [ 1, 2, 2, 2 ], "classification": 1 },
        { "input": [ 1, 2, 2, 3 ], "classification": 3 }, ###################
        { "input": [ 1, 2, 2, 4 ], "classification": 3 }, #__________________
        { "input": [ 2, 1, 1, 1 ], "classification": 3 },
        { "input": [ 2, 1, 1, 2 ], "classification": 2 },
        { "input": [ 2, 1, 1, 3 ], "classification": 1 }, ###################
        { "input": [ 2, 1, 1, 4 ], "classification": 3 }, #__________________
        { "input": [ 2, 1, 2, 1 ], "classification": 3 },
        { "input": [ 2, 1, 2, 2 ], "classification": 1 },
        { "input": [ 2, 1, 2, 3 ], "classification": 2 }, ###################
        { "input": [ 2, 1, 2, 4 ], "classification": 2 }, #__________________
        { "input": [ 2, 2, 1, 1 ], "classification": 3 },
        { "input": [ 2, 2, 1, 2 ], "classification": 2 },
        { "input": [ 2, 2, 1, 3 ], "classification": 1 }, ###################
        { "input": [ 2, 2, 1, 4 ], "classification": 1 }, #__________________
        { "input": [ 2, 2, 2, 1 ], "classification": 3 },
        { "input": [ 2, 2, 2, 2 ], "classification": 3 },
        { "input": [ 2, 2, 2, 3 ], "classification": 1 }, ###################
        { "input": [ 2, 2, 2, 4 ], "classification": 1 }, #__________________
        { "input": [ 3, 1, 1, 1 ], "classification": 3 },
        { "input": [ 3, 1, 1, 2 ], "classification": 3 },
        { "input": [ 3, 1, 1, 3 ], "classification": 1 }, ###################
        { "input": [ 3, 1, 1, 4 ], "classification": 1 }, #__________________
        { "input": [ 3, 1, 2, 1 ], "classification": 3 },
        { "input": [ 3, 1, 2, 2 ], "classification": 1 },
        { "input": [ 3, 1, 2, 3 ], "classification": 3 }, ###################
        { "input": [ 3, 1, 2, 4 ], "classification": 3 }, #__________________
        { "input": [ 3, 2, 1, 1 ], "classification": 3 },
        { "input": [ 3, 2, 1, 2 ], "classification": 2 },
        { "input": [ 3, 2, 1, 3 ], "classification": 2 }, ###################
        { "input": [ 3, 2, 1, 4 ], "classification": 2 }, #__________________
        { "input": [ 3, 2, 2, 1 ], "classification": 3 },
        { "input": [ 3, 2, 2, 2 ], "classification": 3 },
        { "input": [ 3, 2, 2, 3 ], "classification": 2 }, ###################
        { "input": [ 3, 2, 2, 4 ], "classification": 2 }, #__________________
    ]

dataSet = getDataSet()

"""

while dataSet:
    pick any sigma and calculate info

    while totalInfo < sigmaInfo:
        { alfa, alfaValue, info, count } = finding alfa with the highest information gain (filtering out all instances from temporary dataSet that do not satisfy the current rules)
        totalInfo += info
        rules.push({ alfa, alfaValue })

    filtering out all the instances from dataSet that satisfy the rules


"""

def checkIfSatisfies(rules, element):
    for rule in rules:
        if rule["alfaValue"] != element["input"][rule["alfa"]-1]:
            return False
    return True

def filterDataSet(rules):
    res = list(filter(lambda x: checkIfSatisfies(rules, x), dataSet))
    return res


def pSigma(s, rules):
    tempDataSet = filterDataSet(rules)
    tempList = list(filter(lambda x: x["classification"] == s, tempDataSet))

    return len(tempList) / len(tempDataSet)

def pSigmaAlfa(s, a, aValue, rules):
    tempDataSet = filterDataSet(rules)
    aList = list(filter(lambda x: x["input"][a] == aValue + 1, tempDataSet))
    aLen = len(aList)
    sLen = len(list(filter(lambda x: x["classification"] == s, aList)))

    value = 0
    if aLen != 0: value = sLen / aLen
    return { "value": value, "count": aLen }


def iSigma(s, rules):
    return math.log(1 / pSigma(s, rules), 2)

def iSigmaAlfa(s, a, aValue, rules):
    psa = pSigmaAlfa(s, a, aValue, rules)
    ps = pSigma(s, rules)


    if psa["value"] == 0:
        return { "info": 0, "count": 0 }
    return { "info": math.log(psa["value"] / ps, 2), "count": psa["count"] }


ruleList = []
for currSigma in range(1, sigma + 1):
    dataSet = getDataSet()


    iteration = 0
    while len(list(filter(lambda x: x["classification"] == currSigma, dataSet))) > 0:

        iteration += 1

        totalInfo = 0
        sigmaInfo = iSigma(currSigma, [])

        conditions = []

        while abs(totalInfo - sigmaInfo) > 1e-4 :
        # while len(list(filter(lambda x: x["classification"] == currSigma, dataSet))) < len(dataSet) :

            tempRule = { "alfa" : -1, "alfaValue": -1, "info": 0, "count": 0}
            for i in range(0, len(alfa)):
                if i+1 in map(lambda x: x["alfa"], conditions):
                    continue

                for j in range(0, alfa[i]):
                    temp = iSigmaAlfa(currSigma, i, j, conditions)
                    if temp["info"] > tempRule["info"] or (temp["info"] == tempRule["info"] and temp["count"] > tempRule["count"]):
                        tempRule = { "alfa": i+1, "alfaValue": j+1, "info": temp["info"], "count": temp["count"] }

            totalInfo += tempRule["info"]

            conditions.append({ "alfa": tempRule["alfa"], "alfaValue": tempRule["alfaValue"] })

        ruleList.append({ "rules": conditions, "classification": currSigma })

        for i in range(0, len(dataSet)):
            if checkIfSatisfies(conditions, dataSet[i]):
                dataSet[i] = False
        
        dataSet = list(filter(lambda x: x != False, dataSet))


def formatRule(rule):
    alfaChars = ['a', 'b', 'c', 'd' ]
    res = '  ' + str(rule["classification"]) + ' - '
    for condition in rule["rules"]:
        res = res + alfaChars[condition['alfa'] - 1] + str(condition['alfaValue']) + ' + '
    return res[:-3]

print()
print("Rules:")
for rule in ruleList:
    print(formatRule(rule))