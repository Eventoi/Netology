async function loadCurrencyData() {
  try {
    const loader = document.getElementById('loader');
    loader.classList.add('loader_active');

    const response = await fetch('https://students.netoservices.ru/nestjs-backend/slow-get-courses');
    const data = await response.json();

    const valutes = data.response.Valute;

    const itemsContainer = document.getElementById('items');
    
    itemsContainer.innerHTML = '';

    Object.keys(valutes).forEach(key => {
      const currency = valutes[key];

      const itemDiv = document.createElement('div');
      itemDiv.classList.add('item');

      itemDiv.innerHTML = `
        <div class="item__code">${currency.CharCode}</div>
        <div class="item__value">${currency.Value}</div>
        <div class="item__currency">руб.</div>
      `;

      itemsContainer.appendChild(itemDiv);
    });

    loader.classList.remove('loader_active');
  } catch (error) {
    console.error('Ошибка при загрузке данных:', error);
    const loader = document.getElementById('loader');
    loader.classList.remove('loader_active');
  }
}

window.onload = loadCurrencyData;
