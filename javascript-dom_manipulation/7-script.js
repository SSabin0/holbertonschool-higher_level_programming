fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const movieList = document.getElementById('list_movies');
    data.results.forEach(movie => {
      const newItem = document.createElement('li');
      newItem.innerText = movie.title;
      movieList.appendChild(newItem);
    });
  })
  .catch(error => console.error('Error:', error));
