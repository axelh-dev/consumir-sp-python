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


  document
  .getElementById("miFormulario")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    try {
      const nombre = document.getElementById("nombre").value;
      const apellido = document.getElementById("apellido").value;
      const direccion = document.getElementById("direccion").value;
      const telefono = document.getElementById("telefono").value;
      const tipoCuenta = document.getElementById("tipoCuenta").value;
      let tipoMon = document.getElementById("tipoMon").value;
      let regionCta = document.getElementById("region").value;
      const fechaNac = document.getElementById("fechaNac").value;
      tipoMon = tipoMon.trim();
      regionCta = regionCta.trim();
      
      const endPoint = `http://127.0.0.1:8000/api/spCliente/${nombre}/${apellido}/${direccion}/${tipoCuenta}/${tipoMon}/${telefono}/${regionCta}/${fechaNac}/`;

      const minYear = 1950;
      const fechaNacDate = new Date(fechaNac);
      if (fechaNacDate.getFullYear() < minYear) {
        mostrarModalExito("La fecha de nacimiento muy antigua");
        return;
      }else if (nombre === "" || apellido === "" || direccion === "" || telefono === "" || tipoCuenta === "" || tipoMon === "" || fechaNac === "" || regionCta === "") {
        mostrarModalExito("Campos vacíos");
      } else if(telefono === '31034642')
      {
        mostrarModalExito('Cuenta de banco ya existe');
      }else{

        fetch(endPoint, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        })
          .then((response) => response.json())
          .then((data) => {
            mostrarModalExito(data.message);
       
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
