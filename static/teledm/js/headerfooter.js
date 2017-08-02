$(".nav.navbar-nav > li").on('click', function (e) {
	var href = window.location.href;
	alert(href);
    e.preventDefault();
    $('.nav.navbar-nav > li').removeClass('active');
    $(this).addClass('active');
});
