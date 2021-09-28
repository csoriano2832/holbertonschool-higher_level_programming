$.ajax({
  url: "https://swapi-api.hbtn.io/api/films/?format=json",
  success: function(movie) {
    $.each(movie.results, function(key, value) {
      $("UL#list_movies").append("<li>" + value.title + "</li>");
    });
  }
});
