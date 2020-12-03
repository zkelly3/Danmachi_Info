familias = {}


$(function() {
  $.getJSON('familia.json', function(data) {
      data.forEach(function(e) {
         console.log(e)
      });
  });
});