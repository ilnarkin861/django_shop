$(document).ready(function () {

    $('#checkout-form').validate({

        rules:{
            name:{
                required: true
            },
            email: {
                required:true,
                email: true
            },

            phone: {
                required:true,

            },

            city: {
                required:true,

            },

            address: {
                required:true,

            }
        },

        messages: {
            name: {
                required: 'Поле обязательно для заполнения'
            },
            email: {
                required: 'Поле обязательно для заполнения',
                email: 'Электронный адрес заполнен неверно'
            },
            phone: {
                required: 'Поле обязательно для заполнения'
            },
            city: {
                required: 'Поле обязательно для заполнения'
            },
            address: {
                required: 'Поле обязательно для заполнения'
            }
        }
    });

    $('#contact_form').validate({
            rules:{
                name:{
                    required: true
                },
                email: {
                    required:true,
                    email: true
                },

                message: {
                    required: true,
                }


            },

        messages: {
            name: {
                required: 'Поле обязательно для заполнения'
            },
            email: {
                required: 'Поле обязательно для заполнения',
                email: 'Электронный адрес заполнен неверно'
            },
            message: {
                required: 'Поле обязательно для заполнения'
            }
        }

    });



});