//exercise 1

let x = 23 ,y = 34;

if(x > y){
  console.log('x is the biggest number');
}else{
  console.log('y is the biggest number');
}
//end ex1


//exercise 2

let newDog = 'Chihuahua';
console.log(`There is ${newDog.length} in ${newDog}`);

console.log(newDog.toLocaleUpperCase());
console.log(newDog.toLocaleLowerCase());

if(newDog === "Chihuahua"){
  console.log("I love Chihuahuas, it's my favorite dog breed");
}else{
  console.log("I dont care, I prefer cats");
}

//end ex2

//exercise 3, already finished, I comment just for moving foward exercise 4
/* let userInput = parseInt(prompt('Please enter number'));
if (!(userInput % 2)){
  alert(`${userInput} is an even number`);
}else{
  alert(`${userInput} is an odd number`);
} */


//end3

//exercise 4

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];

if(users.length){//true if users.length is greater than 0
  if(users.length === 1){
    console.log(`${users[0]} is online`);
  } 
  else if(users.length === 2){
    console.log(`${users[0]} and ${users[1]} are online`);
  }else{
    console.log(`${users[0]}, ${users[1]} and ${users.length-2} more are online`);
  }
}else{
  console.log ('no one is online');
}

//end4