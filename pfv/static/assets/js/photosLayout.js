window.lazySizesConfig = window.lazySizesConfig || {};
photos = $('#photos');

photos.masonry({
  itemSelector: '.photo-container a',
  columnWidth: 50,
  gutter: 20,
  fitWidth: true
});

var lastWidth = window.innerWidth;
var isMasonryActive = true;

if (window.innerWidth < 700) {
  photos.masonry('destroy');
  isMasonryActive = false;
}

$(window).on('resize', function() {
  if ($(window).width() < 710 && lastWidth >= 700 && isMasonryActive) {
    photos.masonry('destroy');
    isMasonryActive = false;
  } else if (lastWidth < 710 && $(window).width() >= 700) {
    photos.masonry({
      itemSelector: '.photo-container a',
      columnWidth: 50,
      gutter: 20,
      fitWidth: true
    });

    setTimeout(() => {
      isMasonryActive = true;
      photos.masonry('layout');
    }, 200);
  }

  lastWidth = $(window).width();
});

lazySizesConfig.preloadAfterLoad = true;

$(document).on('lazyloaded', function() {
  $('#photos .photo.lazyloaded').each(function() {
    $(this).css({ opacity: 1 });
  });

  if (isMasonryActive) {
    photos.masonry('layout');
  }
});