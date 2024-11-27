// Función para agregar productos al carrito
function agregarAlCarrito(producto, precio) {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];

    // Verifica si el producto ya está en el carrito
    let productoExistente = carrito.find(item => item.producto === producto);
    if (productoExistente) {
        productoExistente.cantidad += 1;
    } else {
        carrito.push({
            producto: producto,
            precio: precio,
            cantidad: 1
        });
    }

    // Guarda el carrito actualizado en localStorage
    localStorage.setItem('carrito', JSON.stringify(carrito));

    // Actualiza el carrito visual
    actualizarCarrito();
}

// Función para actualizar la vista del carrito
function actualizarCarrito() {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let carritoLista = document.getElementById('productos-lista'); 
    let total = 0;

    // Limpiar la lista actual
    carritoLista.innerHTML = '';

    carrito.forEach(item => {
        total += item.precio * item.cantidad;

        // Crear una fila para cada producto
        let row = document.createElement('div');
        row.className = 'card p-3';
        row.style = 'width: 100%; height: 136px; display: flex; flex-direction: row;';
        row.innerHTML = `
            <img src="/static/descarga.png" alt="Producto" class="rounded"
                style="width: 120px; height: 120px; object-fit: cover;" />
            <div class="ms-3 d-flex flex-column justify-content-between" style="flex: 1;">
                <h5 class="mb-1">${item.producto}</h5>
                <div class="d-flex align-items-center">
                    <button class="btn btn-sm btn-outline-primary" onclick="cambiarCantidad('${item.producto}', -1)">-</button>
                    <span class="mx-2">${item.cantidad}</span>
                    <button class="btn btn-sm btn-outline-primary" onclick="cambiarCantidad('${item.producto}', 1)">+</button>
                </div>
                <h6 class="mt-2 text-end">$${item.precio * item.cantidad}</h6>
            </div>
        `;
        carritoLista.appendChild(row);
    });

    // Actualizar el total
    document.getElementById('total-compra').innerText = total.toFixed(2);
}

// Cambiar cantidad de productos
function cambiarCantidad(producto, cambio) {
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let productoExistente = carrito.find(item => item.producto === producto);

    if (productoExistente) {
        productoExistente.cantidad += cambio;
        if (productoExistente.cantidad <= 0) {
            carrito = carrito.filter(item => item.producto !== producto);
        }
        localStorage.setItem('carrito', JSON.stringify(carrito));
        actualizarCarrito();
    }
}

// Finalizar compra
function finalizarCompra() {
    localStorage.removeItem('carrito');
    actualizarCarrito();
    alert('Compra finalizada con éxito');
}

// Cargar carrito al inicio de la página
document.addEventListener('DOMContentLoaded', actualizarCarrito);