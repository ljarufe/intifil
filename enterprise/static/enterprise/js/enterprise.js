$(document).ready(function() {
    var screen = get_screen();
    var column_width;
    if(screen == "tiny")
        column_width = 158;
    else if(screen == "short")
        column_width = 202;
    else
        column_width = 230;

    $(".sitemap_container").columnize({width: column_width, height: 300});
    $("h3, hr").addClass("dontend");
});