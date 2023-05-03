let orders = [];

        function addOrder() {
            const name = document.getElementById('name').value;
            const item = document.getElementById('item').value;

            orders.push({
                name,
                item
            });

            showOrders();
        }

        function showOrders() {
            const table = document.getElementById('orderTable');
            table.innerHTML = `
                <tr>
                    <th>Nama</th>
                    <th>Item</th>
                    <th>Aksi</th>
                </tr>
            `;

            orders.forEach((order, index) => {
                const row = table.insertRow();
                const nameCell = row.insertCell(0);
                const itemCell = row.insertCell(1);
                const actionCell = row.insertCell(2);

                nameCell.innerHTML = order.name;
                itemCell.innerHTML = order.item;

                const deleteButton = document.createElement('button');
                deleteButton.innerText = 'Hapus';
                deleteButton.onclick = () => deleteOrder(index);
                actionCell.appendChild(deleteButton);
            });
        }

        function deleteOrder(index) {
            orders.splice(index, 1);
            showOrders();
        }