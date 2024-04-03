$('#add_item').click(function () {
  "$('.my_list').add($('<li>').text('Item')).appendTo('.my_list');";
  $('.my_list').append($('<li>').text('Item'));
});
