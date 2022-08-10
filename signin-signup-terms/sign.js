const email = document.getElementById("email")
const password = document.getElementById("password")


const form = document.getElementsByTagName('form')[0];


const emailError = document.querySelector('#email + .error');

email.addEventListener('input', function (event) {


    if (email.validity.valid) {

        emailError.textContent = '';
        emailError.className = 'error';
    } else {
        // If there is still an error, show the correct error
        showError();
    }
});

form.addEventListener('submit', function (event) {
    // if the email field is valid, we let the form submit

    if (!email.validity.valid) {
        // If it isn't, we display an appropriate error message
        showError();
        // Then we prevent the form from being sent by canceling the event
        event.preventDefault();
    }
});

function showError() {
    if (email.validity.valueMissing) {
        // If the field is empty,
        // display the following error message.
        emailError.textContent = 'You need to enter an e-mail address.';
    } else if (email.validity.typeMismatch) {
        // If the field doesn't contain an email address,
        // display the following error message.
        emailError.textContent = 'Entered value needs to be an e-mail address.';
    }
    emailError.className = 'error';
    email.onblur() = function () {

        emailError.textContent = '';
    }
}
