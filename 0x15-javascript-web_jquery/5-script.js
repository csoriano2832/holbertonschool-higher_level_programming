$("DIV#add_item").on("click", function() {
  let item = "<li>Item</li>";
  
  $("UL.my_list").append(item);
});
