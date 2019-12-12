window.addEventListener('load', function() {
  const offsetToShow = 100;

  const header = document.querySelector('header');
  handleHideShowElement(header);

  document.addEventListener('scroll', function() {
    handleHideShowElement(header);
  });

  function handleHideShowElement(element) {
    const topOffset = getTopOffset();

    if (topOffset < offsetToShow) {
      element.style.opacity = '0';
    } else {
      element.style.opacity = '1';
    }
  }
});

function getTopOffset() {
  return window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
}