
//functions<>
let expr = '';

let number = (num)=>{
  expr += num;
  console.log(expr);
}

let operator = (operator)=>{
  expr += operator;
  console.log(expr);
}

let equal = ()=>{
  if(eval()){
    let calcTable = [];
    count = -1;
    for(let i = 0; i < expr.length; i++){
      count++;
      calcTable.push('')
      if((/[\d]+/).test(expr[i])){
        calcTable[count] += expr[i];
      }
      else{
        calcTable[count] = parseInt(calcTable[count])
        calcTable.push(expr[i]);
        count ++;
        continue;
      }
    }
    for(index in calcTable ){
      if(calcTable[index] === '' || isNaN(calcTable[index])){
        calcTable.splice(index,1)
      }
    }

    //concatenate number
    console.log(calcTable);
    let operand = '';
    let tmp = [];
    for(let i = 0;  i < calcTable.length+1 ; i++){
      
      if((/[\d]+/).test(calcTable[i])){
        operand += calcTable[i]
      }else{
        tmp.push(parseInt(operand))
        tmp.push(calcTable[i])
        operand = ''
      }
    }
    tmp.pop();
    calcTable = tmp;

    //end concatenate number
    //calulate now
    let result = calcTable[0]
    for(let i = 0;  i < calcTable.length-1 ; i += 2){
      switch (calcTable[i+1]) {
        case '+':
          result += calcTable[i+2]
          break;
        case '-':
          result -= calcTable[i+2]
          break;
        case '*':
          result *= calcTable[i+2]
          break;
        case '/':
          result /= calcTable[i+2]
          break;
      
        default:
          break;
      }
    }
    let globalResult ='';
    calcTable.forEach(element => {
      globalResult += element
    });
    alert(` = ${result}`);
    expr = ''
    //calulate now
  }
}

let eval = ()=>{
  if(expr.match(/^[\+\-\+\*\\][\d]+$/)){

    alert(`${expr} is invalid operation`);
    return false;
  }
  return true;
}

// End functions