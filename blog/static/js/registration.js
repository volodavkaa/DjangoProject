document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registrationForm");

    form.addEventListener("submit", function (event) {
        if (!form.checkValidity()) {
            event.preventDefault();
            event.stopPropagation();
        }
        form.classList.add("was-validated");
    });
    const password1 = document.getElementById("id_password1");
    const password2 = document.getElementById("id_password2");

    password2.addEventListener("input", function () {
        if (password1.value !== password2.value) {
            password2.setCustomValidity("Паролі не співпадають.");
        } else {
            password2.setCustomValidity("");
        }
    });
});
