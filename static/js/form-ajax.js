$(document).ready(function () {



    $('#contact_form, #reg-form').on('submit', function () {

        var success_tpl = '<p class="success-message">{0}</p>';
        var error_tpl = '<p class="error-message">{0}</p>';

        var message_block = $('#form-message-block');
        var action_btn = $(this).find('#form-action-btn');
        var form = $(this)


       if(form.valid()) {
            var action = $(this).attr('action');
            var data = $(this).serialize();
            var btn_text = action_btn.text();



            $.ajax({
                url: action,
                type: 'POST',
                dataType: 'json',
                data: data,

                beforeSend: function(){
                   message_block.html('');
                   action_btn.prop('disabled', true)
                   action_btn.text('Отправляю...')
                },

                success: function (data) {
                    if (data.message){
                        message_block.append($.validator.format(success_tpl, data.message))
                    }
                    action_btn.prop('disabled', false)
                    action_btn.text(btn_text)
                    form[0].reset()

                },
                error: function (data) {
                    var error_message = data.responseJSON.message;
                    if (error_message){
                        message_block.append($.validator.format(error_tpl, error_message))
                    }

                    var errors_list = data.responseJSON.errors;

                    if(errors_list){

                        $.each(errors, function (k, v) {
                            message_block.append($.validator.format(error_tpl, v))
                        })

                    }

                    action_btn.prop('disabled', false);
                    action_btn.text(btn_text)

                }
            });
       }
        return false

    })

})