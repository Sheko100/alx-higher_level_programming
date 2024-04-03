$(function () {
  const input = $('INPUT#language_code');
  $('INPUT#btn_translate').on('click', greeting);
  input.on('keyup', function (e) {
    if (e.keyCode === 13) {
      greeting();
    }
  });
  function greeting () {
    const langCode = input.val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      data: { lang: langCode }
    })
      .done(function (json) {
        $('DIV#hello').text(json.hello);
      });
  }
});
