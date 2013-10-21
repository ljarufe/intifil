$(document).ready(function() {
    var window_h = $(window).height();
    $(".team_block").css({height: window_h});

    // Cargar miniaturas según la resolución
    var request_mini = $.ajax({
        url: URL_GET_MINI,
        type: "GET",
        data: {screen: get_screen()},
        dataType: "html"
    });
    request_mini.done(function(msg) {
        var photos = jQuery.parseJSON(msg);
	var miniature = ''
        for(var i = 0; i < photos.length; i++) {
	    var active = (photos[i].slug == ITEM_SLUG)? 'class="active"':'';
            miniature += '<span>' + photos[i].name + '</span>' +
                            '<a href="' + photos[i].url + '">' +
                                '<img src="' + photos[i].thumb + '" alt="' + photos[i].name + '" '+ active +' />' +
                            '</a>';
        }
	$(".team_preview_container").append(miniature);	
    });
    request_mini.always(function() {
        if($(document).scrollTop() == 0) {
            $("body, html").animate({"scrollTop": "+=" + $("header").height()}, 2000, 'easeInOutExpo');
        }
    });

    // cargar imagen del equipo
    $.ajax({
        url: URL_GET_PHOTO,
        type: "GET",
        data: {screen: get_screen()},
        dataType: "html"
    }).done(function(msg){
	var photo = jQuery.parseJSON(msg);
	$('.team_big_image_container img')
	    .attr('src', photo.thumb)
	    .attr('alt', photo.name);
    });

    // cargar imagenes de los miembros del equipo
    $.ajax({
        url: URL_GET_TEAMMEMBERS_PHOTO,
        type: "GET",
        data: {screen: get_screen()},
        dataType: "html"
    }).done(function(msg){
	var photos = jQuery.parseJSON(msg);
	for (var i=0; i<photos.length; i++){
	    $('img#tm_' + i.toString()).attr('src', photos[i].thumb);
	}
    });


    $(".next_page").click(function() {
        $("body, html").animate({"scrollTop": "+=" + window_h}, 2000, 'easeInOutExpo');
    });

    // Mostrar títulos de las imágenes en miniatura
    // $(".team_preview_container a").live("mouseenter", function() {
    //     $(this).prev("span").fadeIn();
    // }).live("mouseleave", function() {
    //     $(this).prev("span").fadeOut();
    // });
    $(document).on('mouseenter', '.team_preview_container img', function(){
	var pos = $(this).position();
	console.log(pos);
	var top = pos.top - 22;
	var left = pos.left + 34;
	console.log(top)
	var upper_text = $(this).parent().prev("span");
	$(upper_text)
	    .attr('style', 'top: ' + top + 'px; left: ' + left + 'px;');
	$(upper_text).fadeIn();

    });
    $(document).on('mouseleave', '.team_preview_container img', function(){
    	$(this).parent().prev("span").hide();
    });


    var msg_hide = setTimeout(function() {
        if($(document).scrollTop() == $("header").height()) {
            $("body, html").animate({"scrollTop": "+=" + window_h}, 2000, 'easeInOutExpo');
        }
    }, 6000);


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
    });


});
