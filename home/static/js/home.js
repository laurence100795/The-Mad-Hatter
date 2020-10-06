/*BackGround Slider Animation*/

const slideshowImages = document.querySelectorAll(".SlideImage");

const nextSlideDelay = 5000;
let currentSlideCounter = 0; 

slideshowImages[currentSlideCounter].style.opacity = 1;

setInterval(nextSlide, nextSlideDelay);

function nextSlide() {
    slideshowImages[currentSlideCounter].style.opacity= 0;
    currentSlideCounter = (currentSlideCounter + 1) % slideshowImages.length;
    slideshowImages[currentSlideCounter].style.opacity = 1;
}

/*BackGround Slider Animation*/

/*Copy Promotion Code*/
document.getElementById("promoCopy").addEventListener("click", copy_promo);

function copy_promo() {
    var copyText = document.getElementById("promoCode");
    var textArea = document.createElement("textarea");
    textArea.value = copyText.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand("Copy");
    textArea.remove();
}
/*Copy Promotion Code*/