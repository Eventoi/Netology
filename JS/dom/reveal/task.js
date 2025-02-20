document.addEventListener('scroll', function() {
    // Получаем все элементы с классом 'reveal'
    const reveals = document.querySelectorAll('.reveal');
    
    // Для каждого элемента с классом 'reveal' проверяем его положение
    reveals.forEach(function(reveal) {
        // Получаем положение элемента относительно окна
        const rect = reveal.getBoundingClientRect();
        
        // Если элемент находится в поле зрения (когда верхняя граница элемента видна)
        if (rect.top <= window.innerHeight && rect.bottom >= 0) {
            // Добавляем класс 'reveal_active', чтобы отобразить элемент
            reveal.classList.add('reveal_active');
        }
    });
});
