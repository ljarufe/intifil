$(document).ready(function() {
    var window_h;
    var document_h;
    var screen = get_screen();
    
    // $('div.menu').removeClass('no_bg');

    var column_width;
    if(screen == "tiny")
        column_width = 273;
    if(screen == "short")
        column_width = 226;
    if(screen == "medium")
        column_width = 181;
    if(screen == "large")
        column_width = 214;
    if(screen == "huge")
        column_width = 243;

    // Grid layout
    $("#home_content").masonry({
        columnWidth: column_width,
        isAnimated: true,
        isInitLayout: false
    });

    // Cargar thumbnails según la resolución
    var request = $.ajax({
        url: URL_GET_PHOTOS,
        type: "GET",
        data: {category: category, screen: screen},
        dataType: "html"
    });
    request.done(function(msg) {
        var photos = jQuery.parseJSON(msg);
        for(var i = 0; i < photos.length; i++) {
            var item = '<div class="item">' +
                            '<a href="' + photos[i].url + '">' +
                                '<div class="item-container">' +
                                    '<div class="item-content">' + photos[i].name + '</div>' +
                                    '<div class="item-background"></div>' +
                                '</div>' +
                                '<img src="' + photos[i].thumb + '" alt="' + photos[i].name + '" />' +
                            '</a>' +
                        '</div>';
            $("#home_content").append(item);
        }
    });
    request.always(function() {
        $('#home_content').imagesLoaded(function() {
            $("#home_content").masonry('addItems', $(".item"));
            $('#home_content').masonry();
            // Nav controls
            window_h = $(window).height();
            document_h = $(document).height();
            var screens = Math.ceil(document_h/window_h);
            $(".container").css({"height": window_h*screens});
            for(var i=1; i<screens; i++) {
                append_node($("#nav_controls"), "<div class='nav_home up_home'></div>", {"top": window_h*i + 10});
                append_node($("#nav_controls"), "<div class='nav_home down_home'></div>", {"top": window_h*i - 35});
            }
        });
    });

    // Label de las imágenes
    $(".item").live("mouseenter", function() {
        $(this).find(".item-container").fadeIn();
    });
    $(".item").live("mouseleave", function() {
        $(this).find(".item-container").fadeOut();
    });

    // Subir y bajar la pantalla
    $(".up_home").live("click", function() {
        $("body, html").animate({"scrollTop": "-=" + window_h}, 1500, 'easeInOutExpo');
    });
    $(".down_home").live("click", function() {
        $("body, html").animate({"scrollTop": "+=" + window_h}, 1500, 'easeInOutExpo');
    });
    
});
