$(document).ready(function() {
  $.ajax({
    url: "https://fourtonfish.com/hellosalut/?lang=fr",
    success: function(greeting) {
      $("DIV#hello").text(greeting.hello);
    }
  });
});

