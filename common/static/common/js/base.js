// REALLY IMPORTANTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
// AFTER DEVELOPING REPLACE 1580 BY 1600
// ALSO REVIEW THE BASE.LESS to replace the 1599 for 1600
var intervals = [689, 1199, 1410, 1580];
var screens = ["tiny", "short", "medium", "large", "huge"];

var get_screen = function() {
    var width = $(window).width();
    var i;
    for(i=0; i<intervals.length; i++) {
        if(width <= intervals[i])
            return screens[i];
    }
    return screens[i];
};

var append_node = function(node, html, css) {
    var elem = $(html);
    node.append(elem);
    elem.css(css);
};

$(document).ready(function() {

    homepage = (typeof homepage === 'undefined')? false: homepage;

    // custom handler that:
    // if we're on the homepage the menu gray background will be shown
    // only when the second level of items are displayed
    if (homepage){
	activate_handler = function(event, ui){
	    if ($('ul.ui-accordion-content').is(':visible')) {
		$('div.menu').removeClass('no_bg');
	    }else{
		$('div.menu').addClass('no_bg');
	    }
	};
    }else{
	activate_handler = function(event, ui){};
    };

    $(function(){
	$(".menu ul").accordion({
            active: false,
            collapsible: true,
            // event: 'mouseover',
	    event: "hoverintent",
            // animate: 1000, //'easeInOutCirc',
            heightStyle: "content",
	    activate: activate_handler
	});
    });

    $.event.special.hoverintent = {
	setup: function() {
	    $( this ).bind( "mouseover", jQuery.event.special.hoverintent.handler );
	},
	teardown: function() {
	    $( this ).unbind( "mouseover", jQuery.event.special.hoverintent.handler );
	},
	handler: function( event ) {
	    var currentX, currentY, timeout,
	    args = arguments,
	    target = $( event.target ),
	    previousX = event.pageX,
	    previousY = event.pageY;
	    function track( event ) {
		currentX = event.pageX;
		currentY = event.pageY;
	    };
	    function clear() {
		target
		    .unbind( "mousemove", track )
		    .unbind( "mouseout", clear );
		clearTimeout( timeout );
	    }
	    function handler() {
		var prop,
		orig = event;
		if ( ( Math.abs( previousX - currentX ) +
		       Math.abs( previousY - currentY ) ) < 7 ) {
		    clear();
		    event = $.Event( "hoverintent" );
		    for ( prop in orig ) {
			if ( !( prop in event ) ) {
			    event[ prop ] = orig[ prop ];
			}
		    }
		    // Prevent accessing the original event since the new event
		    // is fired asynchronously and the old event is no longer
		    // usable (#6028)
		    delete event.originalEvent;
		    target.trigger( event );
		} else {
		    previousX = currentX;
		    previousY = currentY;
		    timeout = setTimeout( handler, 250 );
		}
	    }
	    timeout = setTimeout( handler, 250 );
	    target.bind({
		mousemove: track,
		mouseout: clear
	    });
	}
    };


    $(".trigger_message").click(function() {
        if(show) {
            $(".message").slideUp("slow", "easeInOutCirc");
            show = false;
        }
        else {
            $(".message").slideDown("slow", "easeInOutCirc");
            show = true;
        }
    });

    $(".triangle").click(function() {
        if(menu_state) {
            $(".menu>ul").hide("slow");
            $(this).addClass("active");
	    $(this).siblings().addClass("no_bg");
            menu_state = false;
        }
        else{
            $(".menu>ul").show("slow");
            $(this).removeClass("active");
	    if (!homepage || $('ul.ui-accordion-content').is(':visible')){
		$(this).siblings().removeClass("no_bg");
	    };
            menu_state = true;
        }
    });

    if (!homepage) {
	var msg_hide = setTimeout(function() {
            if(show) {
		$(".message").slideUp("slow");
		show = false;
            }
	}, 6000);
    };

});
