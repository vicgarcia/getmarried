$(document).ready(function() {

    /* select box choice color */
    $('#attending').change(function() { $(this).css('color', '#000'); });

    /* setup map */
    var map = L.mapbox.map('map', 'mapbox.streets').setView([41.995293, -87.6573157], 11),
        layer = L.mapbox.featureLayer().loadURL('/static/markers.json').addTo(map);
    map.touchZoom.disable();
    map.doubleClickZoom.disable();
    map.scrollWheelZoom.disable();

    /* form handling for rsvp */
    $('#rsvp-form').submit(function() {
        event.preventDefault();
        $('#rsvp-feedback').html('');
        $.post('/rsvp/', $('#rsvp-form').serialize(), function(resp) {
            if (resp.success == true) {
                $('#rsvp-wrap').html("<h2>Thanks for the RSVP!</h2><p>We're looking forward to seeing you there!</p>");
            } else {
                var error_message = '';
                for(var i = 0; i < resp.messages.length; i++) {
                    error_message += '<p>' + resp.messages[i] + '</p>';
                }
                $('#rsvp-feedback').html(error_message);
            }
        });
    });

    /* form handling for gift payment */
    $('#gift-form').submit(function() {
        event.preventDefault();
        $('#gift-feedback').html('');
        var card = {
            number: $('#card').val(),
            cvc: $('#cvc').val(),
            exp_month: $('#exp').val().split('/')[0],
            exp_year: $('#exp').val().split('/')[1],
        };
        Stripe.card.createToken(card, function(status, response) {
            if (response.error) {
                var stripe_error;
                if (!card.number) {
                    stripe_error = '<p>Please provide a valid card number.</p>';
                } else if (response.error.message == 'Missing required param: card[exp_year].') {
                    stripe_error = '<p>Please provide a valid expiration date.</p>';
                } else if (response.error.message == 'Could not find payment information') {
                    stripe_error = '<p>Please provide a valid card number.</p>';
                } else {
                    stripe_error = '<p>' + response.error.message + '</p>';
                }
                $('#gift-feedback').html(stripe_error);
            } else {
                var payload = {
                    token: response.id,
                    csrfmiddlewaretoken: '{{ csrf_token }}',
                    amount: $('#gift-amount').val(),
                    name: $('#gift-name').val(),
                    email: $('#gift-email').val(),
                    note: $('#gift-note').val(),
                };
                $.post('/gift/', payload, function(resp) {
                    if (resp.success == true) {
                        $('#gift-wrap').html('<h2>Thank you!</h2><p>We appreciate your gift and are looking forward to seeing you on the big day!</p><p>You will be receiving an email receipt shortly.</p>');
                    } else {
                        var error_message = '';
                        for(var i = 0; i < resp.messages.length; i++) {
                            error_message += '<p>' + resp.messages[i] + '</p>';
                        }
                        $('#gift-feedback').html(error_message);
                    }
                });
            }
        });
    });

});
