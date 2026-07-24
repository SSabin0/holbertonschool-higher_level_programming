document.addEventListener('click', function (e) {
    if (e.target.id === 'red_header') {
        document.querySelector('header').style.color = '#FF0000';
    }
});
