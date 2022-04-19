let sentence = "The movie is not that bad, I like it";
let wordNot = sentence.search('not');
let wordBad = sentence.search('bad');


if (wordNot < wordBad){
  sentence = sentence.replace(sentence.substring(wordNot, wordBad + 3), 'good')
  console.log(sentence);
}else{
  console.log(sentence);
}