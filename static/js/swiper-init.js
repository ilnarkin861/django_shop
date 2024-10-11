var swiper = new Swiper('.main-slider', {

           autoplay: {
                delay: 10000,
            },
            speed: 2000,
            autoHeight: true,
            pagination: {
                el: '.swiper-pagination',
                type: 'bullets',
                clickable: true,

            },
    });