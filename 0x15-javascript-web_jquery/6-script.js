const header = $('header');
$('DIV#update_header').on('click', function () {
  if (header.text !== 'New Header!!!') {
    header.text('New Header!!!');
  }
});
