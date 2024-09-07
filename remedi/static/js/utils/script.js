function loadHTML(id, url) {
    $.get(url)
        .done(data => {
            $('#' + id).html(data);
        })
        .fail(error => {
            console.error('Error loading HTML:', error);
        });
}

// Load header and footer
$(document).ready(function() {
    loadHTML('header', 'Assets/Pages/Header/header.html');
    loadHTML('footer', 'assets/footer.html');
});

function page4Animation() {
    var $elemC = $("#elem-container");
    var $fixed = $("#fixed-image");

    $elemC.on("mouseenter", function () {
        $fixed.show();
    });

    $elemC.on("mouseleave", function () {
        $fixed.hide();
    });

    $(".elem").each(function() {
        $(this).on("mouseenter", function () {
            var image = $(this).data("image");
            $fixed.css("background-image", `url(${image})`);
        });
    });
}

// Swiper Animation
function swiperAnimation() {
    var swiper = new Swiper(".mySwiper", {
        slidesPerView: "auto",
        centeredSlides: true,
        spaceBetween: 100,
    });
}

// Menu Animation
function menuAnimation() {
    var $menu = $("nav h3");
    var $full = $("#full-scr");
    var $navimg = $("nav img");
    var flag = 0;

    $menu.on("click", function () {
        if (flag === 0) {
            $full.css("top", 0);
            $navimg.css("opacity", 0);
            flag = 1;
        } else {
            $full.css("top", "-100%");
            $navimg.css("opacity", 1);
            flag = 0;
        }
    });
}

// Loader Animation
function loaderAnimation() {
    var $loader = $("#loader");
    setTimeout(function () {
        $loader.css({
            top: "-100%",
            display: "none"
        });
    }, 4200);
}

loaderAnimation()