
var API_ENDPOINT = "/api/shutter"

$("button").click(function() {
    var id = $(this).parent().parent().attr("id")
    var type = ""
    if ($(this).hasClass("btn-success"))
        type = "up"
    if ($(this).hasClass("btn-danger"))
        type = "down"
    var url = `${API_ENDPOINT}/${id}/${type}`
    $.get(url)
});