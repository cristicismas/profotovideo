window.addEventListener('load', function() {
  const offsetToShow = 100;

  const header = document.querySelector('header');

  document.addEventListener('scroll', function() {
    handleHideShowElement(header);
  });

  function handleHideShowElement(element) {
    const topOffset = getTopOffset();

    if (topOffset > offsetToShow) {
      element.style.display = 'flex';
    }
  }
});

function getTopOffset() {
  return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
}
