$(document).ready(function() {
    var window_w = $(window).width();
    var window_h = $(window).height();
    var header_h = $("header").height();

    // Ajustar cada slide según la pantalla (para resoluciones grandes)
    if(window_w < 1199)
        window_h = 947;
    else
        $(".slide").css({height: window_h});

    // Cargar miniaturas según la resolución
    var request_mini = $.ajax({
        url: URL_GET_MINI,
        type: "GET",
        data: {category: category, screen: get_screen()},
        dataType: "html"
    });
    request_mini.done(function(msg) {
        var photos = jQuery.parseJSON(msg);
        var miniature = '';
            for(var i = 0; i < photos.length; i++) {
                var active_class = (photos[i].slug == item)? 'class="active"':'';
                miniature += '<span>' + photos[i].name + '</span>' +
                             '<a href="' + photos[i].url + '">' +
                               '<img src="' + photos[i].thumb + '" alt="' + photos[i].name + '" position="' + i + '" '+ active_class  +'/>' +
                             '</a>';
            }
        $(".growimages").append(miniature);
    });
    request_mini.always(function() {
        if($(document).scrollTop() == 0) {
            $("body, html").animate({"scrollTop": "+=" + header_h}, 2000, 'easeInOutExpo');
        }
    })

    // Cargar sliders
    var request_slider = $.ajax({
        url: URL_GET_SLIDER,
        type: "GET",
        data: {item: item, screen: get_screen()},
        dataType: "html"
    });
    request_slider.done(function(msg) {
        var subitems = jQuery.parseJSON(msg);
        for(var i = 0; i < subitems.length; i++) {
            var subitem = $("#id_slider_" + subitems[i].slug);
            for(var j = 0; j < subitems[i].slider.length; j++)
                subitem.append('<img src="' + subitems[i].slider[j].thumb + '" pos="' + j + '" />');
            if(subitems[i].videos.length) {
                for(var k = 0; k < subitems[i].videos.length; k++, j++) {
                    subitem.append('<div pos="' + j + '">' + subitems[i].videos[k].video + '</div>');
                    subitem.children("div").each(function() {
                        $(this).css({height: $(this).find("iframe").height()});
                    });
                }
                subitem.OverSlider({
                    controls_container: subitem.parent().find(".nav_slider"),
                    controls_type: NUMBERS,
                    easing: 'easeInOutExpo',
                    speed: 1200
                });
            }
            else {
                subitem.kenBurning({
                    controls_container: subitem.parent().find(".nav_slider"),
                    zoom : 1.25,
                    time : 10000
                });
            }
        }
    });

    $(".next_page").click(function() {
        var actual = $(document).scrollTop();
        var scroll = (Math.ceil(actual/window_h))*window_h - actual + header_h;
        $("body, html").animate({"scrollTop": "+=" + scroll}, 1500, 'easeInOutExpo');
        document.title = "Intifil | " + $(this).attr("title");
    });

    // Cambio antiguo entre secciones por las miniaturas
//    $(".growimages img").live("click", function() {
//        var scroll = $(this).attr("position")*window_h - $(document).scrollTop() + $("header").height();
//        $("body, html").animate({"scrollTop": "+=" + scroll}, 1500, 'easeInOutExpo');
//    });

    // $(".growimages a").live("mouseenter", function() {
    //     $(this).prev("span").fadeIn();
    // }).live("mouseleave", function() {
    //     $(this).prev("span").fadeOut();
    // });
    $(document).on('mouseenter', '.growimages img', function(){
        var pos = $(this).position();
        var top = pos.top - 22;
        var left = pos.left + 22;
        var upper_text = $(this).parent().prev("span");
        $(upper_text)
            .attr('style', 'top: ' + top + 'px; left: ' + left + 'px;');
        $(upper_text).fadeIn();
    });
    $(document).on('mouseleave', '.growimages img', function(){
    	$(this).parent().prev("span").hide();
    });

    // Setting slider container to the same height of the gray text container
    // for "large" and "medium" screens
    var screen_name = get_screen();
    if ( screen_name == "large" || screen_name == "medium") {
    	$('div.image_slider').height($('div.description').height()+20);
    }

    // Frequently in Chrome the following error is raised: 
    // "Protocols, domains, and ports must match."
    // as a result the slides that contains videos are set with height of 0px;
    // A workaround for this issue is to set again the slides height 
    // the very first time the scroll event is raised.
    var sliders_visible_verified = false;

    // Showing logo on slides when the header logo is not visible
    function isScrolledIntoView(elem)
    {
        var docViewTop = $(window).scrollTop();
        var docViewBottom = docViewTop + $(window).height();
        var elemTop = elem.offset().top;
        var elemBottom = elemTop + elem.height();
        //return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
        return ((elemBottom <= docViewBottom) && (elemBottom > docViewTop));
    }

    var header_logo = $('header img');
    var slide_logo = $('div.slide_logo');
    var header_logo_visible = true;
    $(window).scroll(function(){
        if ( isScrolledIntoView(header_logo) && header_logo_visible) {
            slide_logo.fadeOut();
            header_logo_visible = false;
        }
        else if (!isScrolledIntoView(header_logo) && !header_logo_visible) {
            slide_logo.fadeIn();
            header_logo_visible = true;
        }

	if (!sliders_visible_verified){
	    $('div.image_slider').height($('div.description').height()+20);
	    sliders_visible_verified = true;
	}

    });

});
