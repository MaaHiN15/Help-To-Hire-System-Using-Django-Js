document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const navbar = document.getElementById("navbar");
    menuIcon.addEventListener("click", function () {
        navbar.classList.toggle("active");
    });

    const servicesSection = document.getElementById("services");
    const exploreButton = document.getElementById("exploreButton");
    exploreButton.addEventListener("click", function (event) {
        event.preventDefault();
        servicesSection.scrollIntoView({ behavior: "smooth" });
    });
});
