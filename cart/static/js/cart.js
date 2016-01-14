$(function() {
    $('span.remove-item').click(function() {
        var cartitem = $(this).parents('tr:first').attr('id');
        var here = this;
        console.log(cartitem);
        $.ajax({
            url: '/cart/remove/',
            data: {
                'cartitem': cartitem
            },
            type: 'post',
            cache: false,
            success: function(data) {
                console.log('success');

                $(here).closest('tr').find('td').fadeOut(400, function() {
                    $(here).parents('tr:first').remove();
                });
            }
        });
    });
});