$.ajax('https://swapi-api.alx-tools.com/api/films/?format=json')
  .done(function (json) {
    const films = json.results;
    const title = [];
    films.forEach(function (film) {
      title.push($('<li></li>').text(film.title));
    });
    $('UL#list_movies').append(title);
  });
