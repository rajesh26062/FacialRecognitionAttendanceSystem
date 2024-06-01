document.addEventListener('DOMContentLoaded', function () {
    const tryItButton = document.getElementById('try-it-button');

    tryItButton.addEventListener('click', function () {
        fetch('/run', {
            method: 'POST'
        })
        .then(response => response.text())
        .then(data => {
            console.log(data); // Handle the script output here
        })
        .catch(error => {
            console.error('An error occurred:', error);
        });
    });
});
