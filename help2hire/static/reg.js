// main.js

// Function to validate the registration form
function validateForm() {
    // Get references to form fields
    var fullName = document.getElementById("fullName");
    var email = document.getElementById("email");
    var password = document.getElementById("pw");
    var confirmPassword = document.getElementById("cp");
    var gender = document.getElementById("gender");
    var dob = document.getElementById("dob");
    var nationality = document.getElementById("nation");
    var qualification = document.getElementById("qualification");
    var languages = document.getElementById("lang");
    var skills = document.getElementById("skills");
    var phoneNum = document.getElementById("phonenum");
    var alternateNum = document.getElementById("alter num");
    var address = document.getElementById("Address");
    var aadharNumber = document.getElementById("Aadhar Number");

    // Get references to error elements
    var fullNameError = document.getElementById("fullNameError");
    var emailError = document.getElementById("emailError");
    var passwordError = document.getElementById("passwordError");
    var confirmPasswordError = document.getElementById("confirmPasswordError");
    var genderError = document.getElementById("genderError");
    var dobError = document.getElementById("dobError");
    var nationalityError = document.getElementById("nationalityError");
    var qualificationError = document.getElementById("qualificationError");
    var languagesError = document.getElementById("languagesError");
    var skillsError = document.getElementById("skillsError");
    var phoneNumError = document.getElementById("phoneNumError");
    var alternateNumError = document.getElementById("alternateNumError");
    var addressError = document.getElementById("addressError");
    var aadharNumberError = document.getElementById("aadharNumberError");

    // Flag to track if there are any validation errors
    var hasErrors = false;

    // Regular expression to validate email format
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    // Validate Full Name
    if (fullName.value.trim() === "") {
        fullNameError.textContent = "Full Name is required.";
        hasErrors = true;
    } else {
        fullNameError.textContent = "";
    }

    // Validate Email
    if (!emailRegex.test(email.value)) {
        emailError.textContent = "Valid email address is required.";
        hasErrors = true;
    } else {
        emailError.textContent = "";
    }

    // Validate Password
    if (password.value.length < 8) {
        passwordError.textContent = "Password must be at least 8 characters long.";
        hasErrors = true;
    } else {
        passwordError.textContent = "";
    }

    // Validate Confirm Password
    if (confirmPassword.value !== password.value) {
        confirmPasswordError.textContent = "Passwords do not match.";
        hasErrors = true;
    } else {
        confirmPasswordError.textContent = "";
    }

    // Validate Gender
    if (gender.value === "") {
        genderError.textContent = "Please select a gender.";
        hasErrors = true;
    } else {
        genderError.textContent = "";
    }

    // Add more validation for other fields as needed...

    // If there are validation errors, prevent form submission
    if (hasErrors) {
        event.preventDefault(); // Prevent form submission
    }
}

// Attach the validateForm function to the form's submit event
var registrationForm = document.querySelector("form");
if (registrationForm) {
    registrationForm.addEventListener("submit", validateForm);
}
