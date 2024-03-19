const nav = document.querySelector(".nav")
const header = document.querySelector(".header")
const menuButton = document.querySelector(".menuButton")
const buttonLefts = document.querySelectorAll('.main_section4_container_items_images_slider_buttonLeft');
const buttonRights = document.querySelectorAll('.main_section4_container_items_images_slider_buttonRight');
const sliders = document.querySelectorAll('.main_section4_container_items_images_slider_div');

menuButton.addEventListener("click", () => {
    if (nav.style.display === "none" || window.getComputedStyle(nav).getPropertyValue("display") === "none") {
        nav.style.display = "block";
        nav.style.opacity = "1"; // Muestra suavemente la navegación cambiando la opacidad
        header.style.height = "300px";
    } else {
        nav.style.opacity = "0"; // Oculta suavemente la navegación cambiando la opacidad
        setTimeout(() => {
            nav.style.display = "none";
        }, 600); // Espera a que termine la transición antes de ocultar la navegación completamente
        header.style.height = "84.3px";
    }
});

sliders.forEach((slider, index) => {
    const slide = slider.querySelector('.main_section4_container_items_images_figure');
    const slideStyle = window.getComputedStyle(slide);
    const slideWidth = slide.offsetWidth 
        + parseInt(slideStyle.getPropertyValue('padding-left')) 
        + parseInt(slideStyle.getPropertyValue('padding-right'))
        + parseInt(slideStyle.getPropertyValue('margin-left')) 
        + parseInt(slideStyle.getPropertyValue('margin-right'));

    buttonRights[index].addEventListener('click', function() {
        slider.scrollBy({
            left: slideWidth,
            behavior: 'smooth'
        });
    });

    buttonLefts[index].addEventListener('click', function() {
        slider.scrollBy({
            left: -slideWidth,
            behavior: 'smooth'
        });
    });
});

$(document).ready(function() {
    // Verifica si el parámetro 'sent' está presente en la URL.
    var urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('sent')) {
        // Si el parámetro 'sent' está presente, desplaza la página hasta el mensaje.
        var elem = document.getElementById('message');
        if (elem) {
            elem.scrollIntoView();
        }
    }

    var form = document.querySelector('.main_section3_container2_form');
    form.addEventListener('submit', function(e) {
        // Agrega el parámetro 'sent' a la URL actual.
        var currentUrl = window.location.href;
        window.location = currentUrl + '?sent=true';
        var elem = document.getElementById('message');
        if (elem) {
            elem.scrollIntoView();
        }
    });
});

