
let sigma = 3;
let alfa = [ 3, 2, 2, 2 ]

let getDataSet = () => [
    { input: [ 1, 1, 1, 2 ], classification: 2 },
    { input: [ 1, 1, 1, 1 ], classification: 3 },
    { input: [ 1, 1, 2, 2 ], classification: 1 },
    { input: [ 1, 1, 2, 1 ], classification: 3 },
    { input: [ 1, 2, 1, 1 ], classification: 3 },
    { input: [ 1, 2, 1, 2 ], classification: 2 },
    { input: [ 1, 2, 2, 1 ], classification: 3 },
    { input: [ 1, 2, 2, 2 ], classification: 1 },
    { input: [ 2, 1, 1, 1 ], classification: 3 },
    { input: [ 2, 1, 1, 2 ], classification: 2 },
    { input: [ 2, 1, 2, 1 ], classification: 3 },
    { input: [ 2, 1, 2, 2 ], classification: 1 },
    { input: [ 2, 2, 1, 1 ], classification: 3 },
    { input: [ 2, 2, 1, 2 ], classification: 2 },
    { input: [ 2, 2, 2, 1 ], classification: 3 },
    { input: [ 2, 2, 2, 2 ], classification: 3 },
    { input: [ 3, 1, 1, 1 ], classification: 3 },
    { input: [ 3, 1, 1, 2 ], classification: 3 },
    { input: [ 3, 1, 2, 1 ], classification: 3 },
    { input: [ 3, 1, 2, 2 ], classification: 1 },
    { input: [ 3, 2, 1, 1 ], classification: 3 },
    { input: [ 3, 2, 1, 2 ], classification: 2 },
    { input: [ 3, 2, 2, 1 ], classification: 3 },
    { input: [ 3, 2, 2, 2 ], classification: 3 }
]


/*

for i < sigma {
    reset dataset
    while(dataset.filter(classification === i).length > 0) {
        calculate sigma probability and sigma info
        while(total info < sigma info) {
            find max psa (take count into consideration after the probability value)
            increase total info by max psa
            filter temporary dataset to satisfy this condition
            rule.push(condition)
        }
        filter dataset to satisfy this rule
        rules.push(rule)
    }
}

*/

function generateRule(dataSet) {
    
}

function removeCoveredInstances(dataSet, rule) {

}


let ruleList = [];
for(let currClass = 1; currClass <= sigma; i++) {

    let dataSet = getDataSet();

    // repeating this action until the dataset does not contain any more instances of sigma classification
    while(dataSet.filter(element => element.classification === currClass).length > 0) {
        let { rule, covered } = generateRule(dataSet); // [ { a: Number, value: Number } ]
        ruleList.push({ class: currClass, rule: rule});
        dataSet = removeCoveredInstances(dataSet, rule);
    }

}

