const inputPieceId = document.querySelector('input[name="piece_id"]');
const btnFind = document.querySelector('input[name="btn_find"]');
const messageElement = document.querySelector('#message')

let map = L.map('map').setView([64.3218280993964, 91.66992187500001], 3);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    foo: '<h1>fdsf</h1>',
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

btnFind.addEventListener('click', () => {
    if (inputPieceId.value == '') {
        messageElement.innerText = 'No plot number is entered!';
        messageElement.style = 'background-color: red; display: block'
    } else {
        messageElement.innerText = 'Searching';
        messageElement.style = 'background-color: green; display: block';
        getPiece()
    }
});

async function getPiece() {
    const url = '/get-piece/' + inputPieceId.value
    await fetch(url)
        .then(
            response => response.json()
        )
        .then(json => {
            messageElement.style = 'display: none';
            clearMap();
            map.setView([64.3218280993964, 91.66992187500001], 3);
            if (json.message) {
                messageElement.innerText = json.message;
                messageElement.style = 'background-color: red; display: block'
            } else {
                map.setView([json.properties.center.y, json.properties.center.x], 19)
                let polygon = L.geoJSON(json).addTo(map);
            }
        })
        .catch(e => {
            messageElement.innerText = e
            messageElement.style = 'background-color: red';
        });
}

function clearMap() {
    for (i in map._layers) {
        if (map._layers[i]._path != undefined) {
            try {
                map.removeLayer(map._layers[i]);
            } catch (e) {
                console.log("problem with " + e + map._layers[i]);
            }
        }
    }
}