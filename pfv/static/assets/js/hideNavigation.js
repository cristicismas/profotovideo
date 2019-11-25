var lastTopOffset;

window.addEventListener('load', function() {
  const header = document.querySelector('header');
  lastTopOffset = getTopOffset();

  lastTopOffset = hideShowElement(header, lastTopOffset);

  document.addEventListener('scroll', function() {
    lastTopOffset = hideShowElement(header, lastTopOffset);
  });
});

function hideShowElement(element, lastTopOffset) {
  const topOffset = getTopOffset();

  if (topOffset < lastTopOffset) {
    element.style.top = '0';
  } else {
    element.style.top = `-${element.clientHeight + 5}px`;
  }

  return topOffset
}

function getTopOffset() {
  return topOffset = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0;
}