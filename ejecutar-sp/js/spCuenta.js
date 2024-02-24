const cuentaCliente = document.getElementById("cuentaCliente");

fetch("http://127.0.0.1:8000/api/v1/Clientes/")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((option) => {
      if(option.nombre === 'Banco'){

      }else{
        const newOption = document.createElement("option");
        const nombreCliente =
          option.nombre + " " + option.apellido + " " + option.telefono;
  
        newOption.value = option.id_cliente;
        newOption.textContent = nombreCliente;
  
        cuentaCliente.appendChild(newOption.cloneNode(true));
      }
      
    });
  })
  .catch((error) => console.error("Error al obtener datos de la API:", error));
const tipoMon = document.getElementById("tipoMon");

fetch("http://127.0.0.1:8000/api/v1/Moneda/")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((option) => {
      const newOption = document.createElement("option");
      newOption.value = option.id_moneda;
      newOption.textContent = option.moneda;

      newOption.setAttribute("data-id", option.id_moneda);

      tipoMon.appendChild(newOption.cloneNode(true));
    });
  })
  .catch((error) => console.error("Error al obtener datos de la API:", error));

const tipoCuenta = document.getElementById("tipoCuenta");

fetch("http://127.0.0.1:8000/api/v1/tpocuenta/")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((option) => {
      const newOption = document.createElement("option");
      newOption.value = option.id_tipo_c;
      newOption.textContent = option.descripcion;

      newOption.setAttribute("data-id", option.id_tipo_c);

      tipoCuenta.appendChild(newOption.cloneNode(true));
    });
  })
  .catch((error) => console.error("Error al obtener datos de la API:", error));

const regionCta = document.getElementById("region");

  fetch("http://localhost:8000/api/v1/regionCta/")
  .then((response) => response.json())
  .then((data) => {
    data.forEach((option) => {
      const newOption = document.createElement("option");
      newOption.value = option.id_region;
      newOption.textContent = option.region;

      newOption.setAttribute("data-id", option.id_region);

      regionCta.appendChild(newOption.cloneNode(true));
    });
  })
  .catch((error) => console.error("Error al obtener datos de la API:", error));

document
  .getElementById("miFormulario")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    try {
      // Obtener valores del formulario
      const cuentaCliente = document.getElementById("cuentaCliente").value;
      const tipoCuenta = document.getElementById("tipoCuenta").value;
      const tipoMon = document.getElementById("tipoMon").value;
      const regionCta = document.getElementById("region");

      const endPoint = `http://127.0.0.1:8000/api/spCuenta/${cuentaCliente}/${tipoCuenta}/${tipoMon}/${regionCta}`;

      if (cuentaCliente === "" || tipoCuenta === "" || tipoMon === "" || regionCta ==="") {
        mostrarModalExito("Campos vacios");
      } else {

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
