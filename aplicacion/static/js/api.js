const apiUrl = 'https://dog.ceo/api/breeds/image/random';

fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        const imageUrl = data.message;
        const imgElement = document.createElement('img');
        imgElement.src = imageUrl;
        
        document.getElementById('imagen-container').appendChild(imgElement);
    })
    .catch(error => {
        console.error('Error al obtener la imagen', error);
    });