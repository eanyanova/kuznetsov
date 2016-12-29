$(function(){
    $('[data-confirm-action]').on('click', function(e){
        if (!confirm($(this).data('confirm-action'))) {
            e.preventDefault();
        }
    });
});