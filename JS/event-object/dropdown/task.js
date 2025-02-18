const dropdowns = document.querySelectorAll('.dropdown');

dropdowns.forEach(dropdown => {
    const valueElement = dropdown.querySelector('.dropdown__value');
    const listElement = dropdown.querySelector('.dropdown__list');
    const items = dropdown.querySelectorAll('.dropdown__item');

    valueElement.addEventListener('click', (e) => {
        e.preventDefault();
        listElement.classList.toggle('dropdown__list_active');
    });

    items.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            const selectedValue = item.querySelector('.dropdown__link').textContent;
            valueElement.textContent = selectedValue;
            listElement.classList.remove('dropdown__list_active');
        });
    });
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('.dropdown')) {
        dropdowns.forEach(dropdown => {
            const listElement = dropdown.querySelector('.dropdown__list');
            listElement.classList.remove('dropdown__list_active');
        });
    }
});