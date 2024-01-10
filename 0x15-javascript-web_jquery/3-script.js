const header = $('header');
$('DIV#red_header').on('click', function () {
  if (!header.hasClass('red')) {
    header.addClass('red');
  }
});
