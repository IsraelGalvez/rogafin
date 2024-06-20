const buttonForm = document.querySelector('.form-button-contact');
const loading = document.querySelector('.loading');

const nameInput = document.querySelector('.name-form');
const emailInput = document.querySelector('.email-form');
const subjectInput = document.querySelector('.subject-form');
const messageInput = document.querySelector('.message-form');

// Deshabilitar el botón de enviar al enviar el formulario
document.querySelector('.main_section3_container2_form').addEventListener('submit', function(event) {
    // Deshabilitar el botón de enviar
    document.getElementById('submit-button').disabled = true;

    // Simular una solicitud al servidor
    setTimeout(function() {
        // Habilitar el botón de enviar nuevamente
        document.getElementById('submit-button').disabled = false;
    }, 9000);  // Cambia este valor al tiempo que tarda tu solicitud
});