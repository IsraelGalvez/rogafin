nav = document.querySelector(".nav")
header = document.querySelector(".header")
menuButton = document.querySelector(".menuButton")

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

