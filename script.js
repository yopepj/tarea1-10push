function mostrarMensaje() {
    alert("JavaScript funcionando correctamente 🚀");
}

document.addEventListener("DOMContentLoaded", function () {
    const formulario = document.getElementById("formulario");

    if (formulario) {
        formulario.addEventListener("submit", function (e) {
            e.preventDefault();

            const nombre = document.getElementById("nombre").value;

            alert("Gracias por tu mensaje, " + nombre + " 😊");

            formulario.reset();
        });
    }
});
