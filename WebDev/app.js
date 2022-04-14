'use strict'

$(document).ready(function() {
    const switchButton = document.querySelector('.btn-dark');

    console.log(switchButton);
    
    switchButton.addEventListener('click', function() {
        document.body.classList.toggle('dark-mode');
    });
});
