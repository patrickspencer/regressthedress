$(document).ready(function(){
    $(".pre-descr").click(function(){
	var text = $(this).text()
	$("#description").val(text);
    });
});
