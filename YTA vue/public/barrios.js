

let url = "http://127.0.0.1:4000/barrios"
$for.get(url, function(respuesta) {
    respuesta.forEach(function(item) {
        console.log(item)
    })

    $for("#barrios2").text(barrios2)
    
    

}, "json")