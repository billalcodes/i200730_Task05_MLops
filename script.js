document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('infoForm');

    form.addEventListener('submit', async function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = {
            name: formData.get('name'),
            email: formData.get('email')
        };

        try {
            const response = await fetch('http://backend:5000/store-info', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            });
            if (response.ok) {
                alert('Information submitted successfully!');
                form.reset();
            } else {
                throw new Error('Failed to submit information.');
            }
        } catch (error) {
            console.error(error);
            alert('An error occurred. Please try again later.');
        }
    });
});
