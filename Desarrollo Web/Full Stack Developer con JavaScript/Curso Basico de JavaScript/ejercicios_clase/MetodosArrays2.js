var articulos = [
    { nombre: 'Bici',costo: 3000},
    { nombre: 'Tv', costo: 2500},
    { nombre: 'Libro', costo: 320},
    { nombre: 'Celular', costo: 10000},
    { nombre: 'Laptop', costo: 20000},    
    { nombre: 'Teclado', costo: 500},    
    { nombre: 'Audifonos', costo: 1700},    
];
var encuentraArticulo = articulos.find(function(articulo){
    return articulo.nombre === 'Laptop';
});

let teclado = articulos.find( (articulo) => {
    return articulo.nombre === 'Teclado';
});

//Modificar el array original

articulos.forEach((articulo) => {
    console.log(articulo.costo);
});

var articulosBaratos = articulos.some((articulo) => {
    return articulo.costo <= 700;
});

console.log(encuentraArticulo);
console.log(teclado);

console.log(articulosBaratos);