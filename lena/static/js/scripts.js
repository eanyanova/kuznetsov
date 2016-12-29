$(function(){
    $('.js-confirm').on('click', function(e){
        if (!confirm($(this).data('confirm'))) {
            e.preventDefault();
        }
    });
});