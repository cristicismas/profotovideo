const scrollDownButton = document.getElementById('scrolldown-btn');

scrollDownButton.addEventListener('click', function (e) {
    e.preventDefault();

    const photosTitle = document.getElementsByClassName('title')[0];

    photosTitle.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
});