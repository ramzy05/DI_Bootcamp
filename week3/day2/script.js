//Exercise1

let myFavFood = "Pop Corn", myFavMeal = "dinner";

console.log(`I eat ${myFavFood} at every ${myFavMeal}`);

//endExo1

//exercise 2

//part1
let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];
let myWatchedSeriesLength = myWatchedSeries.length;
let myWatchedSeriesSentence = 'black mirror, money heist, and the big bang theory';
console.log(`I watched ${myWatchedSeriesLength} series : ${myWatchedSeriesSentence}`);
//end1

//part2
myWatchedSeries.splice(2, 1, "Hint");
myWatchedSeries.push('Prison Break');
myWatchedSeries.unshift("Blacklist");
myWatchedSeries.splice(1,1);
console.log(myWatchedSeries[1].charAt(2));
console.log(myWatchedSeries);
//end2
//endExo2

//exo3

let tmpCel = 20.56, tmpFar = (tmpCel / 5)* 9 + 32;
console.log(`${tmpCel}°C = ${tmpFar.toFixed(2)}°F`);

//end3

//exo4

let c;
let a = 34;
let b = 21;

console.log(a+b) //first expression
    // Prediction: It will output 55, because a = 34 and b = 21
    // Actual: 55
a = 2;

console.log(a+b) //second expression
    // Prediction: It will output 23, because a = 2 and b = 21
    // Actual: 23

// c is equal to undefined

console.log(3 + 4 + '5');// output = 75

//endExo 4

//Exo 5
typeof(15)
// Prediction: number
// Actual: number

typeof(5.5)
// Prediction: number
// Actual: number

typeof(NaN)
// Prediction: number
// Actual: number

typeof("hello")
// Prediction: String
// Actual: String

typeof(true)
// Prediction: Boolean
// Actual: Boolean


typeof(1 != 2)
// Prediction:
// Actual:

"hamburger" + "s"
// Prediction: "hamburgers", here we are concatenating two stings
// Actual: "hamburgers"

"hamburgers" - "s"
// Prediction: NaN, substraction is only use with numbers
// Actual: NaN

"1" + "3"
// Prediction: "13", the to operand string so the output is the concatenation of to string
// Actual: "13"

"1" - "3"
// Prediction: NaN, substraction is only use with numbers
// Actual: NaN

"johnny" + 5
// Prediction: "johnny5", when the we are adding to a string with a number, the ouput is always a string 
// Actual: "johnny5"

"johnny" - 5,
// Prediction: NaN, substraction is only use with numbers
// Actual: NaN

99 * "hello"
// Prediction: NaN, multiplication is only use with numbers
// Actual: NaN

1 != 1
// Prediction: false, the assertion is equivalent to 1 is different than one
// Actual: false

1 == "1"
// Prediction: true, this comparator just evaluate the difference between the value of operands, here the both values are equal
// Actual: true

1 === "1"
// Prediction: false, === comparator evaluate type and value of the operands, here the both value are equal but the type is not the same (number and String)
// Actual: false

//endExo 5


//exo 6


5 + "34"
// Prediction: 534, addition of a string and a number always give a string
// Actual: 534

5 - "4"
// Prediction: NaN, substraction is only use with numbers
// Actual: NaN

10 % 5
// Prediction: 0, % operator is used to get the rest  of division of the first operand by the second
// Actual: 0

5 % 10
// Prediction: 0,
// Actual: 5

"Java" + "Script"
// Prediction: "JavaScript"
// Actual:

" " + " "
// Prediction: "  "
// Actual: "  "

" " + 0
// Prediction: "0"
// Actual: "0"

true + true
// Prediction: 2, true is converted in 1 
// Actual: 2

true + false
// Prediction: 1, false = 0
// Actual: 1

false + true
// Prediction: 1
// Actual: 1

false - true
// Prediction: -1
// Actual: -1

!true
// Prediction: false
// Actual: false

3 - 4
// Prediction: -1
// Actual: -1

"Bob" - "bill"
// Prediction: NaN
// Actual: NaN

//endExo6