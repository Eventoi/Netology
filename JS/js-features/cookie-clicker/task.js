const counterElement = document.getElementById('clicker__counter');
const speedElement = document.getElementById('clicker__speed');
const cookieElement = document.getElementById('cookie');

let clickCount = 0;
let lastClickTime = null;
let totalTime = 0;

cookieElement.addEventListener('click', function() {
    const currentTime = new Date().getTime();
    clickCount++;
    counterElement.textContent = clickCount;

    // Если это не первый клик, вычисляем скорость кликов
    if (lastClickTime !== null) {
        const deltaTime = (currentTime - lastClickTime) / 1000;
        const clickSpeed = 1 / deltaTime;
        speedElement.textContent = clickSpeed.toFixed(2);
    }

    lastClickTime = currentTime;

    // Размер печеньки
    if (clickCount % 2 === 0) {
        cookieElement.style.width = '220px';
        cookieElement.style.height = '220px';
    } else {
        cookieElement.style.width = '200px';
        cookieElement.style.height = '200px';
    }
});
