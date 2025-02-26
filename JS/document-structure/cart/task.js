document.addEventListener('DOMContentLoaded', () => {
    const cartProducts = document.querySelector('.cart__products');

    function addToCart(productId, productImage, productCount) {
        let cartItem = cartProducts.querySelector(`.cart__product[data-id="${productId}"]`);

        if (cartItem) {

            const cartProductCount = cartItem.querySelector('.cart__product-count');
            cartProductCount.textContent = parseInt(cartProductCount.textContent) + productCount;
        } else {

            const newCartItem = document.createElement('div');
            newCartItem.classList.add('cart__product');
            newCartItem.setAttribute('data-id', productId);

            newCartItem.innerHTML = `
                <img class="cart__product-image" src="${productImage}" alt="Товар">
                <div class="cart__product-count">${productCount}</div>
            `;

            cartProducts.appendChild(newCartItem);
        }
    }

    document.querySelectorAll('.product').forEach(product => {
        const decButton = product.querySelector('.product__quantity-control_dec');
        const incButton = product.querySelector('.product__quantity-control_inc');
        const quantityValue = product.querySelector('.product__quantity-value');
        const addToCartButton = product.querySelector('.product__add');

        decButton.addEventListener('click', () => {
            let currentQuantity = parseInt(quantityValue.textContent);
            if (currentQuantity > 1) {
                quantityValue.textContent = currentQuantity - 1;
            }
        });

        incButton.addEventListener('click', () => {
            let currentQuantity = parseInt(quantityValue.textContent);
            quantityValue.textContent = currentQuantity + 1;
        });

        addToCartButton.addEventListener('click', () => {
            const productId = product.getAttribute('data-id');
            const productImage = product.querySelector('.product__image').src;
            const productCount = parseInt(quantityValue.textContent);

            addToCart(productId, productImage, productCount);
        });
    });
});
