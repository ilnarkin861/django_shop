
function addCart (product_id, quantity) {

    var cart_message = $('.cart-message');
    var cart_success_message = 'Товар успешно добавлен в корзину';
    var cart_error_message = 'Ошибка при добавлении товара в корзину';


    $.ajax({

            url: '/cart/add/'+product_id,
            type:'GET',
            dataType:'json',
            data: {'quantity':quantity},
            success: function (data) {
                $('.cart-items-count b').html(data.items_count);
                cart_message.text(cart_success_message);
                cart_message.addClass('success-message');
                cart_message.css('display', 'block');
                cart_message.fadeOut(2000)

            },
            error: function (data) {
                cart_message.text(cart_error_message);
                cart_message.addClass('error-message');
                cart_message.css('display', 'block');
                cart_message.fadeOut(3000)

            }
        }
    )

}

$(document).ready( function () {

    $('#cart-form').on('submit', function (event) {

        formData = $(this).serializeArray();
        addCart(formData[0].value, formData[1].value)
        return false;
    })



});
