/* loads Product page selection box options */
$('#sort-selector').change(function() {
    var selector = $(this);
    var currentUrl = new URL(window.location);

    var selectedVal = selector.val();
    if(selectedVal != "reset"){
        var sort = selectedVal.split("_")[0];
        var direction = selectedVal.split("_")[1];

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);

        window.location.replace(currentUrl);
    } else {
        currentUrl.searchParams.delete("sort");
        currentUrl.searchParams.delete("direction");

        window.location.replace(currentUrl);
    }
})
/* loads Product page selection box options */

/* Srcoller Appear */
window.onscroll = function() {ScrollFunction()};

function ScrollFunction() {
  if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
    document.getElementById("Scroller").className = "TopScroller TaketoTop";
  } else {
    document.getElementById("Scroller").className = "TopScroller";
  }
}
/* Srcoller Appear */

/* Srcoller Position Change */
function TakeToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
/* Srcoller Position Change */