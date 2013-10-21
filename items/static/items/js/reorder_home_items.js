$(document).ready(function() {
    $("#sortable").sortable({
        placeholder: "ui-state-highlight",
        opacity: 0.8,
        cursor: "move"
    });
    $("#sortable").disableSelection();

    $("#save_input").click(function(event) {
        event.preventDefault();
        var order = "";
        $("#sortable li").each(function() {
            order += $(this).attr("id_item") + " ";
        });
        $("#id_order").val(order);
        $("#id_form").submit();
    });
});