$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const langCode = $('INPUT#language_code').val();
    console.log(langCode);
    $.ajax('https://hellosalut.stefanbohacek.dev/?lang=' + langCode).done(function (json) {
      $('DIV#hello').text(json.hello);
    });
  });
});
