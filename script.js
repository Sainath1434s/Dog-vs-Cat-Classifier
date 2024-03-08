function previewImage() {
    var preview = document.getElementById('image-preview');
    var file = document.getElementById('upload').files[0];
    var reader = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    }

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = '';
    }
}

function classifyImage() {
    var file = document.getElementById('upload').files[0];
    var formData = new FormData();
    formData.append('image', file);

    fetch('/classify', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('result').innerText = data.result;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
