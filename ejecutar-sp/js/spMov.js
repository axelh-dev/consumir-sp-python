const cuentaOrigenSelect = document.getElementById("cuentaOrigen");
const cuentaDestinoSelect = document.getElementById("cuentaDestino");

fetch("http://127.0.0.1:8000/api/v1/Cuentas/")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((option) => {
      const newOption = document.createElement("option");
      newOption.value = option.id_cuenta;
      newOption.textContent = option.id_cuenta;

      cuentaOrigenSelect.appendChild(newOption.cloneNode(true));
      cuentaDestinoSelect.appendChild(newOption);
    });
  })
  .catch((error) => console.error("Error al obtener datos de la API:", error));

document
  .getElementById("miFormulario")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    try {
      // Obtener valores del formulario
      const cuentaOrigen = document.getElementById("cuentaOrigen").value;
      const cuentaDestino = document.getElementById("cuentaDestino").value;
      let monto = document.getElementById("monto").value;

      const endPoint = `http://127.0.0.1:8000/api/spMovimiento/${cuentaOrigen}/${cuentaDestino}/${monto}`;

      if (cuentaDestino === "" || cuentaOrigen === "" || monto === "") {
        mostrarModalExito("Campos vacios");
      } else {
        monto = parseFloat(monto);

        fetch(endPoint, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            if (data.error) {
              mostrarModalExito(data.error);
            } else {
              mostrarModalExito("Transacción exitosa");
            }
          })
          .catch((error) => {
            console.error("Error al realizar la solicitud a la API:", error);
          });
      }
    } catch (error) {
      alert(error);
    }

    function mostrarModalExito(mensaje) {
      document.getElementById("message-seccess").textContent = mensaje;
      const modal = new bootstrap.Modal(document.getElementById("mesageSP"));
      modal.show();
    }
  });
