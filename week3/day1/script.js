//1
let adressNumber = "Je vis à Mendong", adressStreet = "Rue 300", country = "Cameroun";

//2

let globalAdress = adressNumber.concat(' ', adressStreet, ', au', country);

//3

console.log(globalAdress);

//exercise 2
let yearOfBirth = 1970, futureYear = 2035;
console.log("I will be "+ (futureYear - yearOfBirth) +" in " + yearOfBirth + "." );


// exo 3

let pets = ['cat','dog','fish','rabbit','cow'];
console.log(pets[1]);


pets.push(' horse');
pets.splice(pets.length-3, 1);

console.log(pets.length)
console.log(pets)