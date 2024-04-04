$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    success: function (response) {
      $('DIV#hello').append(response.hello);
    }
  });
});
