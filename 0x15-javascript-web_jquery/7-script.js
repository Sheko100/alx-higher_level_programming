$.ajax('https://swapi-api.alx-tools.com/api/people/5/?format=json')
  .done(function (chara) {
    $('DIV#character').text(chara.name);
  });
