class Products {
    requestProducts() {
        // Make a request for a user with a given ID
        const request = axios.get('http://145.44.52.247/slimme-afvalbak/api/getter.py', {
            headers: {
                'Access-Control-Allow-Origin': '*'
            }
        });
        request.catch((error) => {
            console.log(error);
        })
        request.then((response) => {
            console.log(response);
        })


        console.log("test");
    }
}

export default (new Products())