const header = $('header');
$('DIV#red_header').on('click', function () {
  if (header.css('color') !== '#FF0000') {
    header.css('color', '#FF0000');
  }
});
