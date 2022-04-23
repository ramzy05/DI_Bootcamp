//exercise two

let names= ["john", "sarah", 23, "Rudolf",34];

for(item of names){
  if(!(typeof(item) === 'string')){
    continue;
  }else{
    if(item[0].match(/^[a-z]/)){
      console.log((item).replace(item[0], item[0].toUpperCase()));
    }/*else{
       let tmp = item[0].toUpperCase()
      (item).replace() 
      console.log((item).replace(item[0], item[0].toUpperCase()));
    }*/
  }
}

