// menyimpan data barang dalam array
let cart = [];

function addToCart(itemId) {
    // mendapatkan kuantitas dari barang
    let jumlah = parseInt(document.getElementById(`jumlah-${itemId}`).textContent);
    // jika kuantitas lebih dari 0 tambah item ke keranjang
    if (jumlah > 0) {
        let item = {
            id: itemId,
            jumlah: jumlah
        };
        cart.push(item);
        updateCart();
        // Reset jumlah to 0
        document.getElementById(`jumlah-${itemId}`).textContent = 0;
    }
}

// Function untuk menambah kuantitas barang
function increasejumlah(itemId) {
    let jumlah = parseInt(document.getElementById(`jumlah-${itemId}`).textContent);
    document.getElementById(`jumlah-${itemId}`).textContent = jumlah + 1;
}

// Function untuk mengurangi kuantitas barang
function decreasejumlah(itemId) {
    let jumlah = parseInt(document.getElementById(`jumlah-${itemId}`).textContent);
    if (jumlah > 0) {
        document.getElementById(`jumlah-${itemId}`).textContent = jumlah - 1;
    }
}

// Function untuk update keranjang
function updateCart() {
    let cartItems = "";
    for (let i = 0; i < cart.length; i++) {
        let item = cart[i];
        cartItems += `<div class="flex justify-between items-center border-b-2 py-2">
                        <p>Item ${item.id}</p>
                        <p>jumlah: ${item.jumlah}</p>
                    </div>`;
    }
    document.getElementById("cart-items").innerHTML = cartItems;
    document.getElementById("shopping-cart").style.display = "block";
}

function clearCart() {
    cart = [];
    updateCart();
    document.getElementById("shopping-cart").style.display = "none";
    }