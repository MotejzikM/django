const menuToggle = document.getElementById('menuToggle');
const nav = document.querySelector('nav');

menuToggle.addEventListener('click', () => {
    if (nav.classList.contains("hidden")) {
        document.body.classList.add("nav");
        nav.classList.remove("hidden");
    } else {
        document.body.classList.remove("nav");
        nav.classList.add("hidden");
    }
});