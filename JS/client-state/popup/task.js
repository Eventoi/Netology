const modal = document.getElementById('subscribe-modal');
const closeBtn = document.querySelector('.modal__close_times');

function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = "expires=" + date.toUTCString();
    document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

function getCookie(name) {
    const nameEq = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(nameEq) == 0) {
            return c.substring(nameEq.length, c.length);
        }
    }
    return "";
}

if (!getCookie('modalClosed')) {
    modal.classList.add('modal_active');
}

closeBtn.addEventListener('click', function () {
    modal.classList.remove('modal_active');
    setCookie('modalClosed', 'true', 7);
});