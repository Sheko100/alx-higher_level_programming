$(function () {
  $('INPUT#btn_translate').on('click', function () {
    const langCode = $('INPUT#language_code').val();
    $getJSON(url: 'https://hellosalut.stefanbohacek.dev/?lang' + langCode, function (data) {
      console.log(data);
    });
  });
});
