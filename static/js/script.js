// Example JavaScript for form submission and results display
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('predict-form');
    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const formData = new FormData(form);
        fetch('/predict', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(result => {
            document.getElementById('results').innerHTML = result;
        });
    });
});
