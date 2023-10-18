$(document).ready(function () {


    $('#search-form').submit(function (event) {
        event.preventDefault();
        var query = $('#search-input').val();
        $.ajax({
            type: 'GET',
            url: '/your-search-url/', //
            data: {
                'search': query
            },
            success: function (data) {

                $('#search-results').html(data);
            }
        });
    });
});
