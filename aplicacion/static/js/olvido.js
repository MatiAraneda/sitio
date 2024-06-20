function validarRegistro() {
const correo = document.getElementById('correo').value;
if (correo === "") {
    document.getElementById('errorCorreo').textContent = "Por favor, ingresa tu correo electrónico.";
    return;
} else {
    document.getElementById('errorCorreo').textContent = "";
}

const regexCorreo = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
if (!regexCorreo.test(correo)) {
    document.getElementById('errorCorreo').textContent = "Por favor, ingresa un correo electrónico válido.";
    return;
} else {
    document.getElementById('errorCorreo').textContent = "";
}
window.location.href = "mensaje.html";
}