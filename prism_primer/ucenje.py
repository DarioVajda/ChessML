from asyncio.windows_events import NULL
import math




def formatRule(rule):
    alfaChars = ['a', 'b', 'c', 'd' ]
    res = '  ' + str(rule["classification"]) + ' - '
    for condition in rule["rules"]:
        res = res + alfaChars[condition['alfa'] - 1] + str(condition['alfaValue']) + ' + '
    return res[:-3]



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

def pSigmaAlfa(s, rules):
    tempDataSet = filterDataSet(rules)
    R = {}
    for i in range(0, len(alfa)):
        R[i] = {}
        for j in range(0, alfa[i]):
            R[i][j] = { "aLen": 0, "sLen": 0 }

    for e in tempDataSet:
        for i in range(0, len(alfa)):
            for j in range(0, alfa[i]):
                if e["input"][i] == j+1:
                    R[i][j]["aLen"] += 1
                    if e["classification"] == s:
                        R[i][j]["sLen"] += 1
    
    tempValue = NULL
    for i in range(0, len(alfa)):
        for j in range(0, alfa[i]):
            e = R[i][j]
            value = 0
            if e["aLen"] != 0: value = e["sLen"] / e["aLen"]
            temp = { "value": value, "count": e["aLen"] }
            R[i][j] = temp
    
    # print()
    # print()
    # for i in R.keys():
    #     print(f'{i}:' + ' {')
    #     for j in R[i].keys():
    #         print(' ', f'{j}:', R[i][j])
    #     print('}')
    return R


def iSigma(ps):
    return math.log(1 / ps, 2)

def iSigmaAlfa(s, rules, ps):
    psa = pSigmaAlfa(s, rules) # { alfa: { value: { alfa, alfaValue, info, count },... },... }

    list = []
    for i in range(0, len(alfa)):
        if i+1 in map(lambda x: x["alfa"], conditions):
            continue

        for j in range(0, alfa[i]):
            currPsa = psa[i][j]
            # print(currPsa)
            if currPsa["value"] == 0:
                temp = {  "alfa" : i+1, "alfaValue": j+1, "info": 0, "count": 0 }
            else:
                temp = {  "alfa" : i+1, "alfaValue": j+1, "info": math.log(currPsa["value"] / ps, 2), "count": currPsa["count"] }
            list.append(temp)
    
    return list


def findBestCondition(conditions, currSigma, sigmaProb):
    # print(len(conditions))

    condition = { "alfa" : -1, "alfaValue": -1, "info": 0, "count": 0}
    choices = iSigmaAlfa(currSigma, conditions, sigmaProb)
    for c in choices:
        if c["info"] > condition["info"] or (c["info"] == condition["info"] and c["count"] > condition["count"]):
            condition = c
    
    # print(condition)
    return condition



ruleList = []
for currSigma in range(1, sigma + 1):
    dataSet = getDataSet()


    iteration = 0
    while len(list(filter(lambda x: x["classification"] == currSigma, dataSet))) > 0:

        iteration += 1

        totalInfo = 0
        sigmaProb = pSigma(currSigma, [])
        sigmaInfo = iSigma(sigmaProb)

        conditions = []
        
        # for e in ruleList:
        #     print(formatRule(e))

        while abs(totalInfo - sigmaInfo) > 1e-4 :
            
            sigmaProb = pSigma(currSigma, conditions)
            tempRule = findBestCondition(conditions, currSigma, sigmaProb)
            totalInfo += tempRule["info"]
            conditions.append({ "alfa": tempRule["alfa"], "alfaValue": tempRule["alfaValue"] })

        ruleList.append({ "rules": conditions, "classification": currSigma })

        for i in range(0, len(dataSet)):
            if checkIfSatisfies(conditions, dataSet[i]):
                dataSet[i] = False
        
        dataSet = list(filter(lambda x: x != False, dataSet))

print()
print("Rules:")
for rule in ruleList:
    print(formatRule(rule))