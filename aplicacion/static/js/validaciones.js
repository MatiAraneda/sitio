function enviarFormulario() {
    var username1 = document.getElementById('username1');
    var password1 = document.getElementById('password1');

    var error = document.getElementById('error');
    error.style.color = 'red';

    console.log('Enviando formulario...');

    var mensajesError = [];

    if(username1.value.trim().length < 6) {
        mensajesError.push('Nombre de usuario invalido');
    }

    if(password1.value.trim().length < 6) {
        mensajesError.push('La contraseña no existe');
    }

    error.innerHTML = mensajesError.join(', ');

    if(mensajesError.length > 0) {
        return false;
    }
    
    return true; 
}


