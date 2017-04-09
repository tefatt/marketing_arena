$(document).ready(function () {

    $(function () {
        $('a').each(function () {
            if ($(this).prop('href') == window.location.href) {
                $(this).addClass('active');
                //$(this).parents('li').addClass('active');
            }
        });
    });
});

$('.pagination-inner a').on('click', function () {
    $(this).siblings().removeClass('pagination-active');
    $(this).addClass('pagination-active');
})
$(document).ready(function () {

    var descMinHeight = 120;
    var desc = $('.desc');
    var descWrapper = $('.desc-wrapper');

    // show more button if desc too long
    if (desc.height() > descWrapper.height()) {
        $('.more-info').show();
    }

    // When clicking more/less button
    $('.more-info').click(function () {

        var fullHeight = $('.desc').height();

        if ($(this).hasClass('expand')) {
            // contract
            $('.desc-wrapper').animate({ 'height': descMinHeight }, 'slow');
        }
        else {
            // expand 
            $('.desc-wrapper').css({ 'height': descMinHeight, 'max-height': 'none' }).animate({ 'height': fullHeight }, 'slow');
        }

        $(this).toggleClass('expand');
        return false;
    });

});
