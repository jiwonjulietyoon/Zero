$(document).ready(function(){
    $('.label_btn').click(function(){
        if ($('.label_select_box').css('display') == 'none') {
            $('.label_select_box').css({
                display: 'block',
            });
        }
        else {
            $('.label_select_box').css({
                display: 'none',
            });
        }
    });
    $('.stt_btn').click(function(){
        if ($('.stt_box').css('display') == 'none') {
            $('.stt_box').css({
                display: 'block',
            });
        }
        else {
            $('.stt_box').css({
                display: 'none',
            });
        }
    });

});