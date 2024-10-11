$(document).ready( function () {

    $('.product-summary-thumb img').on('click', function () {
        var images = $('.product-summary-thumb img');
        images.removeAttr('class')
        src = $(this).attr('src')
        $('.zoom-gallery a').attr('href', src)
        $('.zoom-gallery a img').attr('src', src)
        $(this).addClass('product-summary-thumb-active')

    })

});