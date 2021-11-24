var ready = (callback) => {
    if (document.readyState != "loading") callback();
    else document.addEventListener("DOMContentLoaded", callback);
}
ready(() => {
    document.querySelector(".header").style.height = window.innerHeight
+ "px";
})

$('.dropdown-toggle').dropdown()



function myFunction() {
  var popup = document.getElementById("myPopup");
  popup.classList.toggle("show");
}


$("#ocultar").click(function() {
  $("#disparador").hide(1500);
  });