'use strict'

function addNewDiv () {
    const aboutSection = document.getElementById("about");
    const rowAddButton = document.getElementById("row-adder");

    rowAddButton.addEventListener('click', function() {
        let newDiv = document.createElement("div");

        newDiv.appendChild(document.createElement("h3"));

        newDiv.firstChild.innerHTML = "This is a new div too?";

        aboutSection.appendChild(newDiv);
    });

};

document.body.onload = addNewDiv;