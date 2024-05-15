const loginText = document.querySelector(".title-text .login");
const loginForm = document.querySelector("form.login");
const loginBtn = document.querySelector("label.login");
const signupBtn = document.querySelector("label.signup");
const signupLink = document.querySelector("form .signup-link a");
signupBtn.onclick = (()=>{
 loginForm.style.marginLeft = "-50%";
 loginText.style.marginLeft = "-50%";
});
loginBtn.onclick = (()=>{
 loginForm.style.marginLeft = "0%";
 loginText.style.marginLeft = "0%";
});
signupLink.onclick = (()=>{
 signupBtn.click();
 return false;
});

document.addEventListener("DOMContentLoaded", function () {
    // Select the login and signup forms
    var loginForm = document.querySelector('.login form');
    var signupForm = document.querySelector('.signup form');

    // Add event listener for the login form submission
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Get the input values from the login form
        var email = loginForm.querySelector('input[type="text"]').value;
        var password = loginForm.querySelector('input[type="password"]').value;

        // Perform login logic (simulated for example purposes)
        if (email === "user@example.com" && password === "password") {
            alert("Login successful! Redirecting...");
            // You might want to redirect to a new page or update the UI accordingly.
        } else {
            alert("Login failed. Please check your credentials.");
        }
    });

    // Add event listener for the signup form submission
    signupForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        // Get the input values from the signup form
        var email = signupForm.querySelector('input[type="text"]').value;
        var password = signupForm.querySelector('input[type="password"]').value;
        var confirmPassword = signupForm.querySelector('input[name="confirmPassword"]').value;

        // Perform signup logic (simulated for example purposes)
        if (password === confirmPassword) {
            alert("Sign Up successful! Redirecting...");

            // You might want to redirect to a new page or update the UI accordingly.
        } else {
            alert("Passwords do not match. Please try again.");
        }
    });
});

