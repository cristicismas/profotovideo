photos = $('#photos');

photos.masonry({
  itemSelector: '.photo-container a',
  columnWidth: 50,
  gutter: 20,
  fitWidth: true
});

if (window.innerWidth < 700) {
  photos.masonry('destroy');
}

var lastWidth = window.innerWidth;

$(window).on('resize', function() {
  if ($(window).width() < 710 && lastWidth >= 700) {
    photos.masonry('destroy');
  } else if (lastWidth < 710 && $(window).width() >= 700) {
    photos.masonry({
      itemSelector: '.photo-container a',
      columnWidth: 50,
      gutter: 20,
      fitWidth: true
    });

    setTimeout(() => {
      photos.masonry('layout');
    }, 200);
  }

  lastWidth = $(window).width();
});

window.lazySizesConfig = window.lazySizesConfig || {};

$(document).on('lazyloaded', function() {
  $('#photos .photo.lazyloaded').each(function() {
    $(this).parent().css({ opacity: 1 });
  });

  photos.masonry('layout');
});