const scrollDownButton = document.getElementById('scrolldown-btn');

scrollDownButton.addEventListener('click', function (e) {
    e.preventDefault();

    document.getElementById('photos').scrollIntoView({
        behavior: 'smooth',
        block: 'start'
    });
});