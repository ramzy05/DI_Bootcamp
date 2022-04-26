/* document.body.getElementsByTagName('div')[0]
let divUser =document.body.querySelector('div')

let firstLis = document.body.querySelectorAll('ul li:nth-of-type(1)');

firstLis.forEach((item) => {
  console.log(item);
});

let aTag = document.body.querySelector('a');
console.log(aTag.attributes.length)

for(let item of aTag.attributes){
  console.log(`${item.name} = ${item.value}`)
} */

let par = document.body.getElementsByTagName('p')[0];
par.style.cssText = "\
    font-family:Arial, sans-serif;\
   font-size:2.5rem; \
   display: inline-block;\
   position: relative; top:200px;left:100px;\
   color: white; text-transform: capitalize;\
   background-image: linear-gradient(120deg,  rgba(0,244,0,.8) 10%, rgba(255,23,0,.8));\
   box-shadow: 0px 0px 15px rgba(255,23,0,.8);border:none;\
   border-radius:20px;\
   padding: 20px 30px;\
";