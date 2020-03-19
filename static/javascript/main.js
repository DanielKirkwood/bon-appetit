$(".jumbotron-custom").css({ height: $(window).height() + "px" });

$(window).on("resize", function() {
  $(".jumbotron-custom").css({ height: $(window).height() + "px" });
});
