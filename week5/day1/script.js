let tabBody = document.body.querySelector('tbody');

function insertRow(){
  tabBody.innerHTML += '<tr><td>Row2 cell1</td> <td>Row2 cell2</td></tr>'
}

//ex2
document.getElementById('jsstyle').addEventListener('click', function(){
  alert(this.innerHTML);
});

document.getElementById('jsstyle2').addEventListener('click', function(){
  alert('click sur bouton');
});

document.querySelector('div').addEventListener('click', function(){
  alert('click div');
});
document.querySelector('div').addEventListener('mouseover', function(e){
  this.style.color = 'red';
  alert('survol div');
  //e.stopPropagation()
});
document.querySelector('div p').addEventListener('mouseover', function(e){
  this.style.color = 'red'
  alert('survol p');
 // e.stopPropagation()
}, true);