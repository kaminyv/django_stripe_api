document.addEventListener("DOMContentLoaded", function (event) {
    const stripe_key = 'pk_test_51MaWhcGRiDOXpR1FbpbOl34zMjt3NbqSeAQGnjvPcS8XlwEB7QLBik0nMultYoNHoOWsek10JD8DPyTBWeIhu8DR00HHUNPPxd'
    const stripe = Stripe(stripe_key);
    const card = document.getElementsByClassName('card')[0]
    const buyBtn = document.getElementById('buy')

    buyBtn.addEventListener('click', () => {
        fetch('/buy/' + card.id, {
            method: 'GET',
        })
            .then(function (response) {
                return response.json();
            })
            .then(function (session) {
                return stripe.redirectToCheckout({sessionId: session.session_id});
            })
            .then(function (result) {
                if (result.error) {
                    alert(result.error.message);
                }
            });
    });
});