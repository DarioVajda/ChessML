
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


const pSigma = (s) => {
    return 0.5;
}

const iSigma = (ps) => {
    return Math.log2(1/ps);
}



for(let currSigma = 1; currSigma <= sigma; i++) {

    let dataSet = getDataSet();

    // repeating this action until the dataset does not contain any more instances of sigma classification
    while(dataSet.filter(element => element.classification === currSigma).length > 0) {
        let ps = pSigma(currSigma);
        let is = iSigma(ps);
        let totalInfo = 0;
        let max = { p: 0, count: 0 };

        for(let i = 0; i < alfa.length; i++) {
            for(let j = 0; j < alfa[i]; j++) {

            }
        }
    }

}

