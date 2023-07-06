function autoConstructor (marca, modelo, annio) {
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
}

listaDeMarca = ['Toyota', 'Hyndai', 'Renolt'];
listaDeModelo = ['Modelo 1', 'Modelo 2', 'Modelo 3'];
listaDeAnnio = [2020, 2021, 2022];
let autos = [];

function creadorDeAutos (listaDeMarca,listaDeAnnio,listaDeModelo) {
    for (let i = 0; i < listaDeAnnio.length; i++){
        let carro = new autoConstructor(listaDeMarca[i],listaDeModelo[i],listaDeAnnio[i]);
        autos.push(carro);
    }
    console.log(autos);
}

creadorDeAutos(listaDeMarca,listaDeAnnio,listaDeModelo);