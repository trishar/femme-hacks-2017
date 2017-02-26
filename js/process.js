var txt = '';

  function getValue() {
    var val = document.getElementById("link").value;
    window.location.href = 'page2.html';
    txt = val;
    console.log(val)
  }

//   $(function() {
//     $('button').click(function() {
//         var url = $('#submittedUrl').val();
//         $.ajax({
//             url: '/submitUrl',
//             data: $('form').serialize(),
//             type: 'POST',
//             success: function(response) {
//                 console.log(response);
//             },
//             error: function(error) {
//                 console.log(error);
//             }
//         });
//     });
// });

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

    url = Object.keys(data).map(function(k) {
	    return encodeURIComponent(k) + '=' + encodeURIComponent(data[k])
	}).join('&')

  });
