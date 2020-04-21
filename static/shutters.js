
var API_ENDPOINT = "/api/shutter"

$("button").click(function() {
    var id = $(this).parent().parent().attr("id")
    var type = ""
    if ($(this).hasClass("btn-success"))
        var url = `${API_ENDPOINT}/${id}/up`
    if ($(this).hasClass("btn-danger"))
        var url = `${API_ENDPOINT}/${id}/down`
    if ($(this).hasClass("btn-light"))
        var url = `${API_ENDPOINT}/allup`
    if ($(this).hasClass("btn-dark"))
        var url = `${API_ENDPOINT}/alldown`
    if ($(this).hasClass("btn-primary"))
        var url = `${API_ENDPOINT}/group/${id}/up`
    if ($(this).hasClass("btn-secondary"))
        var url = `${API_ENDPOINT}/group/${id}/down`
    console.log(url)
    $.get(url)
});