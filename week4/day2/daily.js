

//<head>
function getInput(){
  let input;
  do{
    input = prompt('Enter words separate by comma');
    if(input instanceof String || !input/* to make sur the string is empty */){alert("Please enter a sequence of words");}
  }while(!input);
  input = input.replace(/ /gm, '');//remove whitespace
  return input.split(',');
}

function theWidthAndHeight(liste){
  let maxLengthItem = liste[0].length
  for(let i = 1; i<liste.length; i++){
    if(maxLengthItem < liste[i].length){
      maxLengthItem = liste[i].length
    }
  }//width = maxLenfthItem + 2, height = liste.lenght + 2
  return [maxLengthItem + 4, liste.length + 2];
}

function draw(){
  let liste = getInput()
  console.log(liste)
  let width_height = theWidthAndHeight(liste);
  //print the first line of star
  for(let i = 0; i < width_height[0]; i++){
    document.write(`*`);
  }
  document.write(`<br>`);
  for(let i = 0; i <= width_height[1] - 3; i++){
    document.write(`*&nbsp;&nbsp;${liste[i]}`);
    /* for(let j=0; j < Math.round(((width_height[0]-(liste[i-1]).length))/2); j++){
      console.log(Math.round(((width_height[0]-(liste[i-1]).length))/2));
      document.write(``);
    } */
    /* document.write(`&nbsp;${liste[i-1]}`); */
    if(liste[i].length == width_height[0]-4){
      for(let j=1; j <= ((width_height[0]-liste[i].length-1)); j++){
        document.write(`&nbsp;`);/*  */
      }
    }else{

      for(let j=1; j <= ((width_height[0] -liste[i].length)+2); j++){
        document.write(`&nbsp;`);/*  */
      }
    }
    console.log(width_height[0]-liste[i].length);
    document.write(`*<br>`);
  }
   //print the last line of star
  for(let i = 0; i < width_height[0]; i++){
    document.write(`*`);
  }
}