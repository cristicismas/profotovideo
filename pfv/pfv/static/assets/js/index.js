const carousel = document.querySelector('.video-carousel')

var flkty = new Flickity(carousel, {
  cellAlign: 'center',
  wrapAround: true,
  pageDots: false
});

if (window.innerWidth < 700) {
  flkty.destroy();
}

var lastWidth = window.innerWidth;

window.onresize = function() {
  if (window.innerWidth < 700) {
    flkty.destroy();
  } else if (lastWidth < 700 && window.innerWidth > 700) {
    flkty = new Flickity(carousel, {
      cellAlign: 'center',
      wrapAround: true,
      pageDots: false
    });
  }

  lastWidth = window.innerWidth;
}

