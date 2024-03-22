
document
  .getElementById("miFormulario")
  .addEventListener("submit", function (event) {
    event.preventDefault();

    try {
      // Obtener valores del formulario
      const TpoBack = document.getElementById("TpoBack").value;
      const Dir = document.getElementById("Dir").value;

      const endPoint = `http://127.0.0.1:8000/api/spbackup/${encodeURIComponent(Dir)}/${TpoBack}`;


      if (TpoBack === "" || Dir === "") {
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
