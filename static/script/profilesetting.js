function validateEmail(emailInput) {
    var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
    if (emailInput.value.match(validRegex)) {
        alert("Valid email address!");
        return true;
    } else {
        alert("Invalid email address!");
        return false;
    }
}

// Add event listener for email input validation
var emailInput = document.getElementById('emailInput');
emailInput.addEventListener('blur', function() {
    validateEmail(this);
});




