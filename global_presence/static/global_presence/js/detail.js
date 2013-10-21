$(document).ready(function(){

    // loads flags thumbnails based on the screen resolution
    var request_mini = $.ajax({
        url: URL_GET_MINI,
        type: "GET",
        data: {screen: get_screen()},
        dataType: "html"
    });
    request_mini.done(function(msg) {
        var photos = jQuery.parseJSON(msg);
	var miniature = '';
        for(var i = 0; i < photos.length; i++) {
	    var active = (photos[i].id == COUNTRY & i != 0)? 'active':'';
            miniature += '<span>' + photos[i].name + '</span>' +
		'<a href="' + photos[i].url + '">' +
                '<img src="' + photos[i].thumb + '" alt="' + photos[i].name + '" class="lineimages '+ active + '" />' + '</a>';
        }
	$(".flags_container").append(miniature);
    });

    // showing/hiding flags name
    $(document).on('mouseenter', '.flags_container img', function(){
    	var pos = $(this).position();
    	console.log(pos);
    	var top = pos.top - 24;
    	var left = pos.left;
    	console.log(top)
    	var upper_text = $(this).parent().prev("span");
    	$(upper_text)
    	    .attr('style', 'top: ' + top + 'px; left: ' + left + 'px;');
    	$(upper_text).fadeIn();
    });
    $(document).on('mouseleave', '.flags_container img', function(){
    	$(this).parent().prev("span").hide();
    });

    // loads team thumbnails based on the screen resolution
    var request_team = $.ajax({
        url: URL_GET_TEAM,
        type: "GET",
        data: {screen: get_screen(), country: COUNTRY},
        dataType: "html"
    });
    request_team.done(function(msg) {
        var images = jQuery.parseJSON(msg);
        for(var i = 0; i < images.length; i++) {
            $("img#"+images[i].id)
		.attr('src', images[i].thumb)
		.attr('alt', images[i].name);
        }
    });

    // disabled cause the client don't want this for now
    // // initial scrolling
    // 
    // var window_h = $(window).height();
    // var header_h = $("header").height();
    // if ( GO_TO_PAGE === undefined | GO_TO_PAGE == 0 ){
    // 	$("body, html")
    // 	    .animate({"scrollTop": "+=" + header_h}, 2000, 'easeInOutExpo');
    // }else{
    // 	var scroll = GO_TO_PAGE*window_h - $(document).scrollTop() + header_h;
    // 	$("body, html")
    // 	    .animate({"scrollTop": "+=" + scroll}, 1500, 'easeInOutExpo');
    // };

    // // setting the correct height to pages containers if necessary
    // var page_containers = $('.global_presence_detail_main_container');
    // if (page_containers.height() < window_h){
    // 	page_containers.height(window_h);
    // };

    // // scroll to next page
    // $(".next_page").click(function() {
    //     var actual = $(document).scrollTop();
    //     var scroll = (Math.ceil(actual/window_h))*window_h - actual + header_h;
    //     $("body, html").animate({"scrollTop": "+=" + scroll}, 1500, 'easeInOutExpo');
    // });

    // if the window can't show the entire page, then let's move the page
    // to the content
    var window_h = $(window).height();
    var page_h = $('body').height();

    if (page_h > window_h){
	if($(document).scrollTop() == 0) {
            $("body, html").animate({"scrollTop": "+=" + $("header").height()}, 2000, 'easeInOutExpo');
	}
    }

});
