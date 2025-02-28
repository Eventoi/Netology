const signinForm = document.getElementById('signin__form');
const signinBtn = document.getElementById('signin__btn');
const signinBlock = document.getElementById('signin');
const welcomeBlock = document.getElementById('welcome');
const userIdElement = document.getElementById('user_id');

function checkAuth() {
    const userId = localStorage.getItem('user_id');
    if (userId) {
        welcomeBlock.classList.add('welcome_active');
        userIdElement.textContent = userId;
        signinBlock.classList.remove('signin_active');
    } else {
        signinBlock.classList.add('signin_active');
        welcomeBlock.classList.remove('welcome_active');
    }
}

function login() {
    const formData = new FormData(signinForm);

    fetch('https://students.netoservices.ru/nestjs-backend/auth', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            localStorage.setItem('user_id', data.user_id);
            userIdElement.textContent = data.user_id;
            signinBlock.classList.remove('signin_active');
            welcomeBlock.classList.add('welcome_active');
        } else {
            alert('Неверный логин/пароль');
        }
    })
    .catch(error => {
        alert('Ошибка при отправке данных');
    });
}

signinBtn.addEventListener('click', function(event) {
    event.preventDefault();
    login();
});

checkAuth();
