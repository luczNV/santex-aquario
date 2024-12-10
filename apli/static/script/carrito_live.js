<script>
document.addEventListener('DOMContentLoaded', function () {
	// Función para actualizar el contador del carrito
	function actualizarCarrito() {
		fetch("{% url 'global_carrito_cantidad' %}", {
			method: 'GET',
			headers: {
				'X-Requested-With': 'XMLHttpRequest'
			}
		})
		.then(response => response.json())
		.then(data => {
			const contador = document.getElementById('cart-counter');
			contador.textContent = data.cantidad;
		})
		.catch(error => console.error('Error al obtener cantidad del carrito:', error));
	}

	// Llamar a la función al cargar la página
	actualizarCarrito();

	// Actualiza el carrito después de agregar un producto
	const botonesAgregar = document.querySelectorAll('.agregar-al-carrito');

	botonesAgregar.forEach(boton => {
		boton.addEventListener('click', function () {
			const productoId = this.dataset.productoId;

			fetch(`/agregar-al-carrito/${productoId}/`, {
				method: 'GET',
				headers: {
					'X-Requested-With': 'XMLHttpRequest'
				},
			})
			.then(response => response.json())
			.then(data => {
				alert(data.message);
				actualizarCarrito(); // Actualiza el contador después de agregar
			})
			.catch(error => console.error('Error al agregar producto al carrito:', error));
		});
	});
});
</script>