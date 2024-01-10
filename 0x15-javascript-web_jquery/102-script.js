$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const langCode = $('INPUT#language_code').val();
    $.ajax({
      url: 'https://hellosalut.stefanbohacek.dev/',
      data: { lang: langCode }
    })
      .done(function (json) {
        $('DIV#hello').text(json.hello);
      });
  });
});
