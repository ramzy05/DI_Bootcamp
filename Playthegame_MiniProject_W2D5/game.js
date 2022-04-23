let computerNumber = Math.floor(Math.random()*10);

//<head>
let playTheGame = ()=>{
  //alert(computerNumber);
  if(confirm('Do you want to play game?')){
    let userInput, count = 1;
    /* count will increase only if the input is a number */
    do{
       userInput = parseInt(prompt('Please enter a number'));
      if (isNaN(userInput)){
        alert('Sorry Not a number');
        //if the input is not a number, then we going to reask user to input a number without increment count varibale
      }else{
        if(!(0 <= userInput && userInput <=10)){
          alert('Sorry it\’s not a good number');
          //count ++; we don't increment count because the number is not in the good range(0-10)
        }else{
          
          if(test(userInput, computerNumber)){
            //user win the game
            break;
          }else{
            //try again
            count ++;
          }
        }
      }
      if(count === 4){
        alert('out of chances')
        return;
      }
    }while(count < 4 );
    return;
  }

  alert('No problem, Goodbye');
  return;
}

let test = (userNumber,computerNumber)=>{
  
  if(userNumber < computerNumber){
    alert ('Your number is smaller then the computer\’s, guess again')
    return false;
  }else if(userNumber > computerNumber){
    alert("Your number is bigger then the computer’s, guess again")
    return false;
  }

  alert('WINNER')
  return true;
 
}