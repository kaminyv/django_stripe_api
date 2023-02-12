function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}
document.addEventListener("DOMContentLoaded", function (event) {
    const stripe_key = getCookie('stripe_public_key');
    const stripe = Stripe(stripe_key);
    const card = document.getElementsByClassName('card')[0];
    const buyBtn = document.getElementById('buy');

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