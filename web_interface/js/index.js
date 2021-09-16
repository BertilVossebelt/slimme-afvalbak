// Make a request to getter.py to get the data from the database

// Axios is loaded using an external link because not everyone has axios/npm installed yet.
const request = axios.get('http://192.168.1.76/slimme-afvalbak/api/getter.py');

// Log errors if needed
request.catch((error) => {
    console.error(error);
});

// Handle successful request
request.then((response) => {
    /*
    * Probably shouldn't use eval, but JSON.parse is being difficult
    * and it's not too bad for a project like this.
    */
    let data = eval(response.data);
    let list_items = ''

    // Loop over all the products and add them to a string
    data.forEach((product) => {
            list_items = list_items + "<li>" + product.product + " - Barcode: " + product.barcode + "</li>" + "\n";
    });

    // Write string inside of ul tags.
    document.getElementById('shopping-list-ul').innerHTML = list_items;
});
