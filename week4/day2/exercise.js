//exo 1

//partI
  (function infoAboutMe(){
    console.log('My name is Ramses, my hobbies are football and coding');
  }());
//endI

//partII
  function infoAboutPerson(personName, personAge, personFavoriteColor){
    console.log(`Your name is ${personName}, you are ${personAge} years old, your favorite color is ${personFavoriteColor}`);
  }
  infoAboutPerson("David", 45, "blue");
  infoAboutPerson("Josh", 12, "yellow");

//endII

//end exo1
//exo 2

function calculateTip(){
  let billAmount = parseFloat(prompt('Enter the amount of the bill'));
  let tipAmount ;
  if(billAmount < 50){//<head>
    tipAmount = parseFloat(((billAmount * 20)/100).toFixed(2))
  }else if(billAmount >= 50 && billAmount <= 200){
    tipAmount = parseFloat(((billAmount * 15)/100).toFixed(2)) 
  }else{
    tipAmount = parseFloat(2((billAmount * 10)/100).toFixed(2)) 
  }
  //final bill
  console.log(`Your final bill is \$${billAmount + tipAmount}`);
}

/* calculateTip(); */

//end exo2

//exo 3
  function isDivisible(divisor){
    let sumOfDivisibleNumber = 0;
    console.log('Outcome : ');
    for(let i = 0; i < 501; i++){
      if(i % divisor === 0){
        sumOfDivisibleNumber += i;
        console.log(`${i} `)
      }
    }
    console.log(`Sum : ${sumOfDivisibleNumber}`);
  }

/* isDivisible(23); */
//end exo3


//exo 4

  let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
  };

  let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
  }; 

  let shoppingList = ['banana', 'orange', 'apple'];

  function myBill(){
    let totalPrice = 0;
    for(let name of shoppingList){
      if(stock[name] > 0){
        //decrease the stock by 1
        --stock[name];
        //add the price of item to totalPrice
        totalPrice += prices[name];

      }
   }
   return totalPrice;
  }

  myBill();
//end exo4


//exo 5//<head>

function changeEnough(itemPrice, amountOfChange){
  return(
    itemPrice <= amountOfChange[0]*0.25 + 
                amountOfChange[1]*0.10 +
                amountOfChange[2]*0.05 +
                amountOfChange[3]*0.01
  );
 
}

changeEnough(4.25, [25, 20, 5, 0])
//end exo5


//exo 6//<head>

function hotelCost(day){
  //here we are sure that day is a positive number
  return day * 140;
}

function planeRideCost(destination){
  //the destination is not and empy string
  if(destination === 'London' || destination.toLowerCase() === 'london'){
    return 183;
  }else if (destination === 'Paris' || destination.toLowerCase() === 'paris'){
    return 220;
  }else{
    return 300;
  }
}


function rentalCarCost(day){
  if(day > 10){
    return (day * 40) - (day*40)*5/100
  }
  return day*40
}


function totalVacationCost(){
  let dayHotelCost, destination ,dayCarCost;
  do{
    dayHotelCost = parseInt(prompt('Enter the number of day you are going to stay in the hotel'));
    if(typeof(dayHotelCost) == undefined || isNaN(dayHotelCost) || dayHotelCost < 0){alert("Please enter a correct positive number!");}
  }while(isNaN(dayHotelCost) || dayHotelCost < 0);


  do{
    dayCarCost = parseInt(prompt('Enter the number of days you would like to rent the car'));
    if(typeof(dayCarCost) == undefined || isNaN(dayCarCost) || dayCarCost < 0){alert("Please enter a correct positive number!");}
  }while(isNaN(dayCarCost) || dayCarCost < 0);

  do{
    destination = prompt('Enter your destination');
    if(destination instanceof String || !destination /* to make sur the string is empty */){alert("Please enter a correct destination");}
  }while(!destination) ;

  console.log(`The car cost: \$${rentalCarCost(dayCarCost)}, \
the hotel cost: \$${hotelCost(dayHotelCost)}, \
the plane tickets cost: ${planeRideCost(destination)}.`);
}


//end exo6//<head>