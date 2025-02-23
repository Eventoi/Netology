document.addEventListener('DOMContentLoaded', function () {
    const book = document.getElementById('book');
    const fontSizeLinks = document.querySelectorAll('.font-size');
    
    // Функция для обновления размера шрифта
    function setFontSize(size) {
        // Удаление всех классов изменения размера
        book.classList.remove('book_fs-small', 'book_fs-big');
        
        // Добавление соответствующего класса в зависимости от выбранного размера
        if (size === 'small') {
            book.classList.add('book_fs-small');
        } else if (size === 'big') {
            book.classList.add('book_fs-big');
        } else {
            // По умолчанию — обычный шрифт
            book.classList.add('book_fs-normal');
        }
    }

    // Обработчик кликов на элементы управления шрифтами
    fontSizeLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            
            // Удаление класса активного элемента у всех ссылок
            fontSizeLinks.forEach(link => {
                link.classList.remove('font-size_active');
            });
            
            // Добавление активного класса к текущему элементу
            this.classList.add('font-size_active');
            
            // Получение значения из атрибута data-size
            const size = this.getAttribute('data-size');
            
            // Установка соответствующего размера шрифта
            setFontSize(size);
        });
    });
});
