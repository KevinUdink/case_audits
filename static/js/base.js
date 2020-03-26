// Adding functionality to make things more dynamic on the pages based on screen size
//  AND we can toggle the navigation manually to allow for more screen real estate for content
(function($) {
  "use strict";

  // Toggle the side navigation
  $("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
  });

})(jQuery);
