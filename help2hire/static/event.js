const images = document.querySelectorAll('.image-carousel img');
let currentIndex = 0;

function showImage(index) {
    images.forEach((image, i) => {
        if (i === index) {
            image.style.display = 'block';
        } else {
            image.style.display = 'none';
        }
    });
}

function rotateCarousel() {
    currentIndex = (currentIndex + 1) % images.length;
    showImage(currentIndex);
}

images.forEach((image, index) => {
    image.addEventListener('click', () => {
        
        rotateCarousel(); 
    });
});


setInterval(rotateCarousel, 3000); 
showImage(currentIndex);

document.addEventListener("DOMContentLoaded", function () {
    const definitionDiv = document.querySelector(".definition");
    definitionDiv.classList.add("slide-in");
  });