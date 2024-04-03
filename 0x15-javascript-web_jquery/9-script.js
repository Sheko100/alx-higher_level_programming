$.ajax('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .done(function (json) {
    $('DIV#hello').text(json.hello);
  });
