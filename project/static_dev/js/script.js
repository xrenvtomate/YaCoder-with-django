$(document).ready(function(){
    $('.like-form').submit(function(e){
        e.preventDefault();
        form = $(e.target)
        $.ajax({
            type: 'POST',
            url: $(e.target).attr('action'),
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function(data) {
                likes = data.likes;
                if (form.hasClass('liked')) {
                    form.removeClass('liked');
                }
                else form.addClass('liked');
                form.find('button').text(`${likes} likes`)
            }
        })
    });
});