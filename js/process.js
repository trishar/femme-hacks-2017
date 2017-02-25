function getValue() {
  var val = document.getElementById("link").value;
  window.location.href = 'page2.html';
  console.log(window.location.pathname);
  return val;
}
