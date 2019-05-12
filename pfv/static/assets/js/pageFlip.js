var Page = (function () {

  var albums = $('#albums');

  return {
    init: function() {
      albums.find('div.album').each(function(i) {
        var album = $(this);
        var nav = album.next().children('a');
        var bb = album.bookblock({
          speed: 800,
          shadowSides: 0.8,
          shadowFlip: 0.7
        });

        nav.each(function(i) {
          $(this).on('click', function () {
            if ($(this).context.className == 'next') {
              bb.bookblock('next');
            } else {
              bb.bookblock('prev');
            }
            return false;
          });
        });
      });
    }
  }
})();

Page.init();