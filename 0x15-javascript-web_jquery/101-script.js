$(function () {
  const list = $('UL.my_list');
  $('DIV#add_item').on('click', function () {
    list.append('<li>Item</li>');
  });
  $('DIV#remove_item').on('click', function () {
    const item = list.children();
    const lastIndex = item.length - 1;
    if (lastIndex >= 0) {
      item[lastIndex].remove();
    }
  });
  $('DIV#clear_list').on('click', function () {
    list.empty();
  });
});
