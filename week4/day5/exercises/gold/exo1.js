const divBooks = document.createElement('div');
divBooks.setAttribute('class', 'listBooks');
document.body.appendChild(divBooks);

let allBooks = [
  {
    title : 'Ngum a jemea. La foi inébranlable de Rudolf Dualla Manga Bell',
    author : 'David Mbanga Eyombwan',
    image : 'https://librairiedespeuplesnoirs.odoo.com/web/image/product.product/1104/image_1024/Ngum%20a%20jemea.%20La%20foi%20in%C3%A9branlable%20de%20Rudolf%20Dualla%20Manga%20Bell%20%28Fran%C3%A7ais%29%20-%202017%20de%20David%20Mbanga%20Eyombwan%20%28Auteur%29?unique=478ed44',
    alreadyRead: true
  },
  {
    title : 'Les Bimanes',
    author : 'Séverin Cécile Abéga',
    image : 'https://static.fnac-static.com/multimedia/Images/FR/NR/85/7c/33/3374213/1540-1/tsp20140410183114/Les-Bimanes.jpg',
    alreadyRead: false
  }
];

allBooks.forEach((book)=>{
  if(book.alreadyRead){
    divBooks.innerHTML += `<p style = "color:red;">${book.title} written by ${book.author}.<br><p>`;
  }else{
    divBooks.innerHTML += `<p>${book.title} written by ${book.author}.<br><p>`;
  }
  /* const bookImg = document.createElement('img');
  bookImg.style.width = '100px';
  bookImg.setAttribute('src', book.image);<></>
  bookImg.setAttribute('alt', book.title + ' by ' +book.author)
  divBooks.innerHTML += `<img src= "${book.image}" style= "width = 100px"; alt="${book.title} by ${book.author}">` */
  divBooks.innerHTML += `<img src= "${book.image}" style=" width:100px;" alt="${book.title} by ${book.author}">`
});