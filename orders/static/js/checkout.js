$(function () {
    var sticky_relocate = function() {
        var window_top = $(window).scrollTop();
        var div_top = $('#sticky-anchor').offset().top;
        if (window_top > div_top) {
            $('#sticky-cart').addClass('stick');
        } else {
            $('#sticky-cart').removeClass('stick');
        }
    };

    $(window).scroll(sticky_relocate);
    sticky_relocate();
});