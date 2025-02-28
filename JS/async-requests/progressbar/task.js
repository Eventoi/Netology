document.getElementById('form').addEventListener('submit', function(event) {
    event.preventDefault();

    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append('file', file);

    const xhr = new XMLHttpRequest();

    xhr.upload.addEventListener('progress', function(event) {
        if (event.lengthComputable) {
            const percent = (event.loaded / event.total) * 100;
            const progress = document.getElementById('progress');
            progress.value = percent;
        }
    });

    xhr.onload = function() {
        if (xhr.status === 200) {
            alert('Файл успешно загружен!');
        } else {
            alert('Ошибка загрузки файла!');
        }
    };

    xhr.onerror = function() {
        alert('Ошибка при отправке запроса!');
    };

    xhr.open('POST', 'https://students.netoservices.ru/nestjs-backend/upload', true);
    xhr.send(formData);
});
