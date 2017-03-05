$(document).ready(function() {
	// get current URL path and assign 'active' class
	var pathname = window.location.pathname;
	$('.nav > li > a[href="' + pathname + '"]').parent().addClass('active');
})

$(document).ready(function(){
    $('[data-toggle="popover"]').popover(); 
});

$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});