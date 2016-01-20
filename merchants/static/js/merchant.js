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



    /*
    $('a[data-target=#order-cart-modal]').click(function(e) {
        e.preventDefault();
        console.log("here");
        var target = $(this).attr('href');
        $(this).find('.modal-body').load(target, function() {
            $('#order-cart-modal').modal('show');
        });
        var cartModal = $('#order-cart-modal');
        var modalBody = cartModal.find('.modal-body');
        modalBody.load(target, function() {
            cartModal.modal('show');
        });
    });
    */

    $('a[data-target=#order-cart-modal]').click(function(e) {
        e.preventDefault();

        // get the data target attribute
        var target_modal = $(e.currentTarget).data('target');
        // get remote url content
        var remote_content = e.currentTarget.href;

        // get target modal and its body div
        var cart_modal = $(target_modal);
        var modal_body = $(target_modal + ' .modal-body');

        // show the modal with remote url content in body div
        cart_modal.on('show.bs.modal', function() {
            modal_body.load(remote_content);
        }).modal();

        return false;
    });



    $('#order-cart-modal').on('shown.bs.modal', function() {

        $('span.remove-item').on('click', function () {
            var cartitem = $(this).parents('tr:first').attr('id');
            var here = this;
            //console.log(cartitem);

            $.ajax({
                url: '/cart/remove/',
                data: {
                    'cartitem': cartitem
                },
                type: 'post',
                cache: false,
                success: function (json) {
                    //console.log('success');
                    //console.log(json);
                    $(here).closest('tr').find('td').fadeOut(400, function () {
                        $(here).parents('tr:first').remove();
                    });

                    // If cart becomes emtpy, reload the modal
                    if (json['size'] == 0) {
                        console.log('becomes empty');
                        $('#order-cart-modal').fadeOut('slow', function () {
                            $(this).modal('hide');
                        }).fadeIn('slow', function() {
                            $(this).modal('show');
                        });
                    }
                }
            });
        });

        $('#updateForm').on('submit', function(e) {
            e.preventDefault();
            console.log('here update');

            $.ajax({
                url: $(this).attr('action'),
                type: $(this).attr('method'),
                data: $(this).serialize(),

                success: function(json) {
                    //console.log(json);
                    // reload modal content upon update
                    $('#order-cart-modal').fadeOut('slow', function() {
                        $(this).modal('hide');
                    }).fadeIn('slow', function() {
                        $(this).modal('show');
                    });
                }
            });
        });

    });

});

