let sect = document.body.querySelector('section');
let planets = [
  'Mercury', 'Venus', 'Earth',
  'Mars', 'Jupiter', 'Saturn',
  'Uranus', 'Neptune'
]

let planetColors = [
  'slategray',
  '#eae0c8',
  '#0022EE',
  '#DD2146',
  '#DD21B4',
  '#AF9501',
  '#70A892',
  '#E0B3CF'
];

let planetsContainer = [];
var i = 0;
planets.forEach((planet)=>{
  let newDiv = document.createElement('div');
  newDiv.classList.add('planet');
  newDiv.textContent = planet;
  newDiv.style.background = planetColors[i];
  newDiv.style.margin = "0 auto";
  sect.append(newDiv);
  i++;
});