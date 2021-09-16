// Make a request for a user with a given ID
const request = axios.get('http://10.80.17.1/slimme-afvalbak/api/getter.py', {
    headers: {
        'Access-Control-Allow-Origin': '*'
    }
});

request.catch((error) => {
    console.error(error);
});

request.then((response) => {
    let data = eval(response.data);

    data.forEach((product) => {
        document.getElementById('shopping-list-ul')
            .innerHTML = "<li>" + product.product + " - Barcode: " + product.barcode + "</li>";
    });
});
