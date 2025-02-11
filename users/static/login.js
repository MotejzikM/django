const form = document.querySelector('form');

const usernameDiv = form.querySelector('div');
const passwordDiv = usernameDiv.nextElementSibling;

usernameDiv.setAttribute('style', '');
passwordDiv.setAttribute('style', '');

const usernameLabel = document.querySelector('#id_username').previousElementSibling;
const passwordLabel = document.querySelector('#id_password').previousElementSibling;

usernameLabel.textContent = 'Uživatelské jméno:';
passwordLabel.textContent = 'Heslo:';