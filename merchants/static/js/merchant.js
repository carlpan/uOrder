$(function() {
    $('.item-description').each(function() {
        var $this = $(this);
        $this.popover({
            trigger: 'hover',
            placement: 'top',
            html: true,
            content: $this.html()
        });
    });

    /* CartItem price update */
    /*
    $('#quantity-6').change(function() {
        var item_id = $('.modal').attr('id');
        console.log(item_id);
        var quantity = $(this).val();
        var price = parseFloat($('.item-price-'+item_id).val());
        var total = quantity * price;
        $('.total-price-'+item_id).html(total.toFixed(2));
    });
    */


    /* Add item to cart form submission */
    $('.add-cart-form').on('submit', function(e) {
        e.preventDefault();
        //console.log("form submitted!");
        console.log($(this).serialize());
        //var item_id = $(this).attr('id');
        //console.log(item_id);

        /* AJAX for posting */
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: $(this).serialize(),

            // handle successful response
            success: function(json) {
                console.log(json);
                //console.log(json['count']);
                //$('#cart-count').html(json.count);
                $('.modal').modal('hide');
            }
        });
    });


});

