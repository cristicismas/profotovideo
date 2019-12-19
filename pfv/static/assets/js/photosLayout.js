const photos = $('#photos');
var lastWidth = $(window).width();
var isMasonryActive = true;

function onDebouncedResize(callback) {
  let resizeTimeout;

  $(window).on('resize', function() {
    clearTimeout(resizeTimeout);
    resizeTimeout = setTimeout(callback, 50);
  });
}

function initializeMasonry() {
  photos.masonry({
    itemSelector: '.photo-container a',
    columnWidth: 50,
    gutter: 20,
    fitWidth: true
  });
}

initializeMasonry();

if ($(window).width() < 700) {
  photos.masonry('destroy');
  isMasonryActive = false;
}

onDebouncedResize(function() {
  if ($(window).width() < 700 && isMasonryActive) {
    photos.masonry('destroy');
    isMasonryActive = false;
  } else if ($(window).width() > 700 && !isMasonryActive) {
    initializeMasonry();
    isMasonryActive = true;
    photos.masonry('layout');
  }

  lastWidth = $(window).width();
});


// Run masonry('layout') again on every photo load
$(document).on('lazyloaded', function() {
  $('#photos .photo.lazyloaded').each(function() {
    $(this).css({ opacity: 1 });
  });

  if (isMasonryActive) {
    photos.masonry('layout');
  }
});
