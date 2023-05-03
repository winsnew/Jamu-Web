// Array untuk menyimpan data barang yang telah dipesan
let items = [];

// Fungsi untuk menampilkan data barang pada tabel
function renderTable() {
  const tbody = document.getElementById("items-tbody");
  tbody.innerHTML = "";

  items.forEach((item, index) => {
    const row = document.createElement("tr");

    const indexCell = document.createElement("td");
    indexCell.textContent = index + 1;
    row.appendChild(indexCell);

    const nameCell = document.createElement("td");
    nameCell.textContent = item.name;
    row.appendChild(nameCell);

    const quantityCell = document.createElement("td");
    quantityCell.textContent = item.quantity;
    row.appendChild(quantityCell);

    const priceCell = document.createElement("td");
    priceCell.textContent = item.price;
    row.appendChild(priceCell);

    const totalCell = document.createElement("td");
    totalCell.textContent = item.price * item.quantity;
    row.appendChild(totalCell);

    const actionsCell = document.createElement("td");
    const editButton = document.createElement("button");
    editButton.classList.add("px-2", "py-1", "bg-blue-500", "text-white", "rounded-md", "hover:bg-blue-600", "focus:outline-none", "mr-2");
    editButton.textContent = "Edit";
    editButton.addEventListener("click", () => editItem(index));

    const deleteButton = document.createElement("button");
    deleteButton.classList.add("px-2", "py-1", "bg-red-500", "text-white", "rounded-md", "hover:bg-red-600", "focus:outline-none");
    deleteButton.textContent = "Hapus";
    deleteButton.addEventListener("click", () => deleteItem(index));

    actionsCell.appendChild(editButton);
    actionsCell.appendChild(deleteButton);

    row.appendChild(actionsCell);

    tbody.appendChild(row);
  });
}

// Fungsi untuk menambahkan barang ke dalam array `items`
function addItem() {
  const nameInput = document.getElementById("name-input");
  const quantityInput = document.getElementById("quantity-input");
  const priceInput = document.getElementById("price-input");

  const name = nameInput.value;
  const quantity = parseInt(quantityInput.value);
  const price = parseInt(priceInput.value);

  const item = { name, quantity, price };
  items.push(item);

  renderTable();
}

// Fungsi untuk mengedit data barang yang telah dipesan
function editItem(index) {
  const item = items[index];
  const name = prompt("Masukkan nama barang", item.name);
  const quantity = parseInt(prompt("Masukkan jumlah barang", item.quantity));
  const price = parseInt(prompt("Masukkan harga barang", item.price));

  const updatedItem = { name, quantity, price };
  items[index] = updatedItem;

  renderTable();
}

// Fungsi untuk menghapus data barang yang telah dipesan
function deleteItem(index) {
  items.splice(index, 1);

  renderTable();
}

renderTable();
