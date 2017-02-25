var txt = '';

  function getValue() {
    var val = document.getElementById("link").value;
    window.location.href = 'page2.html';
    console.log(window.location.pathname);
    txt = val;
  }

  $( document ).ready(function() {
      console.log( "ready!" );
      $.ajax({
      url: "../parsing/parser.py",
      type: 'POST',
      data: {val: txt},
      success: function(data, status){
        //check status
        //do something with data
      }
    });
  });
