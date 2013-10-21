/*
 *
 * ------------------------------------------------------------------------------
 * OverSlider: Slider para jQuery
 *
 * Slider para cualquier tipo de elementos
 * ------------------------------------------------------------------------------
 * Autor: Luis Jarufe
 * Versión: 0.5
 *
 * Las opciones son:
 * controls_container: Elemento del DOM donde se colocaran los navegadores
 * controls_type: Por defecto no se muestran controles, las opciones son:
 *      - NONE para no mostrar controles.
 *      - PREV_NEXT para mostrar controles para mover al anterior y siguiente elemento
 *      - NUMBERS para mostrar controles por cada elemento
 * controls_play: Coloca un control para activar y otro para desactivar el autoplay
 * controls_labels: Muestra u oculta los textos de los controles para reemplazarlos por imágenes
 * controls_id: Le coloca un id a cada control de navegación de la clase "num".
 * controls_id_prefix: Prefijo para el id de los controles de la clase "num" si la opción
 *                     controls_id está activada, por defecto es "id_"
 * autoplay: Si es true el slider rota sus elementos automáticamente, por
 *           default es false
 * autoplay_time: Tiempo en segundos entre transiciones si autoplay es true
 * height: Altura de los elementos del slider, puede ser autocalculada, pero es
 *         recomendable añadir la opción en pixeles.
 * easing: Efecto easing para las transiciones, por defecto se usa 'swing', otros
 *         tipos de easing se encuentran en jQuery UI
 * speed: Tiempo en milisegundos para la animación de la transición
 * mousewheel: habilita o inhabilita la función de la rueda del mouse, para activarlo
 *             es necesario usar un plugin como el de:
 *             http://www.ogonek.net/mousewheel/jQuery_mousewheel_plugin.js
 *
 * Ejemplo:
 * 1. Es necesario añadir la hoja de estilo jquery.over-slider.css
 *
 * 2. Para utilizarlo sobre un elemento del DOM, pasándole un diccionario con
 *    las opciones, ninguna es obligatoria.
 *
 *      $("#id_slider").OverSlider({
 *           controls_container: $("#id_controls_container"),
 *           controls_type: NUMBERS,
 *           controls_play: true,
 *           controls_labels: false,
 *           controls_id: true,
 *           controls_id_prefix: "id_slider_",
 *           autoplay: true,
 *           autoplay_time: 10,
 *           height: 400,
 *           easing: 'linear',
 *           speed: 1000,
 *           mousewheel: true
 *      });
 *
 * */

// TODO: Arrastrar las imágenes para cambiar

// Tipos de controles de navegación
var NONE = 0;
var PREV_NEXT = 1;
var NUMBERS = 2;
var BOTH = 3;

(function ($) {
    var methods = {
        init: function(user_options) {
            var options = $.extend({}, $.fn.OverSlider.defaultSettings, user_options);

            // Cantidad de elementos en el slider sin contar al navegador
            var $this = $(this);
            var elem_selector = "*:not('." + options.controls_container.attr("class") + "')";
            var num_elem = $this.children(elem_selector).size();

            // Ajustar el tamaño del slider
            if(options.height) $this.css("height", options.height);
            else $this.css("height", $this.children(elem_selector).height());

            // Estilos necesarios para el slider
            $this.addClass("over_slider_container");

            return this.each(function() {
                // Añadir los controles prev next
                var append_prevnext = function() {
                    var label_up, label_down;
                    if(options.controls_labels.label_up)
                        label_up =  options.controls_labels.label_up;
                    else
                        label_up = "▲";
                    if(options.controls_labels.label_down)
                        label_down =  options.controls_labels.label_down;
                    else
                        label_down = "▼";
                    options.controls_container.append(
                        "<div class='nav prev'>" + label_up + "</div>" +
                        "<div class='nav next'>" + label_down + "</div>"
                    );
                };

                // Añadir los controles con números
                var append_numbers = function() {
                    var label = 1;
                    if(options.controls_labels)
                        label = options.controls_labels.numbers[0];
                    var id = "";
                    if(options.controls_id)
                        id = 'id="' + options.controls_id_prefix + label + '"';
                    options.controls_container.append(
                        "<div class='nav num active' " + id + " position='1'>" + label + "</div>"
                    );
                    for(var i = 1; i < num_elem; i++) {
                        if(options.controls_labels)
                            label = options.controls_labels.numbers[i];
                        else
                            label = i + 1;
                        id = "";
                        if(options.controls_id)
                            id = 'id="' + options.controls_id_prefix + label + '"';
                        options.controls_container.append(
                            "<div class='nav num' " + id + " position='" + (i+1) + "'>" + label + "</div>"
                        );
                    }
                };

                // Añadir los controles de play/stop
                var append_playpause = function() {
                    options.controls_container.append(
                        "<div class='nav play'>►</div>" +
                        "<div class='nav stop'>■</div>"
                    );
                };

                // Play/Stop
                var timer;
                // Posición actual
                var position = 1;

                var play = function() {
                    timer = setInterval(function() {
                        if (position < num_elem)
                            move_forward(1);
                        else
                            move_afterward(num_elem-1);
                    }, options.autoplay_time*1000);
                };

                var stop = function() {
                    clearInterval(timer);
                };

                var move_forward = function(positions) {
                    var height;
                    if(options.height)
                        height = options.height;
                    else
                        height = $this.children(elem_selector).height();
                    slider.animate({"scrollTop": "+=" + height*positions}, options.speed, options.easing);
                    change_active(position, position+positions);
                    position+=positions;
                };

                var move_afterward = function(positions) {
                    var height;
                    if(options.height)
                        height = options.height;
                    else
                        height = $this.children(elem_selector).height();
                    slider.animate({"scrollTop": "-=" + height*positions}, options.speed, options.easing);
                    change_active(position, position-positions);
                    position-=positions;
                };

                var move_next = function() {
                    if(position < num_elem)
                        move_forward(1);
                    else
                        move_afterward(num_elem-1);
                    stop();
                };

                var move_prev = function() {
                    if(position > 1)
                        move_afterward(1);
                    else
                        move_forward(num_elem-1);
                    stop();
                };

                var move_pos = function(elem) {
                    var new_position = elem.attr("position");
                    var distance = Math.abs(new_position - position);
                    if(new_position > position)
                        move_forward(distance);
                    else
                        move_afterward(distance);
                    stop();
                };

                var change_active = function(old_pos, new_pos) {
                    options.controls_container.children(".num[position=" + old_pos + "]").removeClass("active");
                    options.controls_container.children(".num[position=" + new_pos + "]").addClass("active");
                };

                // Ocultar el texto de los controles TODO: no funciona
                var hide_control_labels = function() {
                    $(".nav").css("display", "none");
                };

                // Controles de navegación
                switch(options.controls_type) {
                    case PREV_NEXT:
                        append_prevnext();
                        break;
                    case NUMBERS:
                        append_numbers();
                        break;
                    case BOTH:
                        append_prevnext();
                        append_numbers();
                        break;
                }
                if(options.controls_play) {
                    append_playpause();
                }

                // Elementos controladores
                var next = options.controls_container.children(".next");
                var prev = options.controls_container.children(".prev");
                var play_control = options.controls_container.children(".play");
                var stop_control = options.controls_container.children(".stop");
                var slider = $(this);

                // Eventos con los controladores
                next.bind("click", function() {
                    move_next();
                });

                prev.bind("click", function() {
                    move_prev();
                });

                options.controls_container.children(".num").bind("click", function() {
                    move_pos($(this));
                });

                play_control.bind("click", function() {
                    play();
                });

                stop_control.bind("click", function() {
                    stop();
                });

                // Autoplay del slider
                if(options.autoplay) {
                    play();
                }

                if(options.mousewheel) {
                    this.mousewheel(function(objEvent, intDelta) {
                        if (intDelta > 0)
                            move_prev();
                        else if (intDelta < 0)
                            move_next();
                    });
                }
            });
        }
    };

    $.fn.OverSlider = function(method) {
        if(methods[method]) {
            return methods[method].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if(typeof method === 'object' || ! method) {
            return methods.init.apply( this, arguments );
        } else {
            $.error( 'Method ' +  method + ' does not exist on jQuery.tooltip' );
        }
    };

    $.fn.OverSlider.defaultSettings = {
        controls_container: $(this),
        controls_type: NONE,
        controls_play: false,
        controls_labels: false,
        controls_id: false,
        controls_id_prefix: "id_",
        autoplay: false,
        autoplay_time: 8,
        height: false,
        easing: 'swing',
        speed: 400,
        mousewheel: false
    };
})(jQuery);