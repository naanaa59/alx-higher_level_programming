$(function () {
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (films) {
      films.results.forEach(function (film) {
        $('#list_movies').append('<li>' + film.title + '</li>');
      });
    }
  });
});
