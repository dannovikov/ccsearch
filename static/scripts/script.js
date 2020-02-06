// When the user scrolls down 50px from the top of the document, resize the header
window.onload = function() {
  document.getElementById("topbar").style.paddingBottom = "0px";
}

window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 240 || document.documentElement.scrollTop > 240) {
    //document.getElementById("logotext").style.visibility = "hidden";
    //document.getElementById("logo").style.marginLeft = "1vw";
    //document.getElementById("resultTitle").style.position = "relative";
    document.getElementById("logo").style.maxWidth = "200px";
    document.getElementById("topbar").style.bottom = "50px";

  } else {
    //document.getElementById("resultTitle").style.position = "initial";
    document.getElementById("logo").style.maxWidth = "450px";
    //document.getElementById("logo").style.marginLeft = "auto";
    document.getElementById("topbar").style.height = "100%";
  }
}
