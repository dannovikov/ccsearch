// When the user scrolls down 50px from the top of the document, resize the header
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 250 || document.documentElement.scrollTop > 250) {
    //document.getElementById("logotext").style.visibility = "hidden";
    document.getElementById("logo").style.maxWidth = "130px";
    document.getElementById("topbar").style.height = "50px";
  } /*else {
    document.getElementById("logo").style.maxWidth = "400px";
    document.getElementById("topbar").style.height = "100%";
  //  document.getElementById("logotext").style.visibility = "visible";
}*/
}
