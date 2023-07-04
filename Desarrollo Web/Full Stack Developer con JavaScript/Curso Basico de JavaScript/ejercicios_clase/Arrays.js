var frutas = ['papaya', 'Manzana', 'Platano'];

console.log(frutas);

console.log(frutas[0]);
//Ingresa en el ultimo puesto
var masFrutas = frutas.push('Fresa');


console.log(frutas);

//Elimina en el ultimo puesto
var ultimo = frutas.pop("Fresa");

console.log(frutas);

//Ingresa en el primer puesto
var muchasMasfrutas = frutas.unshift('Mango');

console.log(frutas);

//Ingresa en el primer puesto
var eliminarMasFrutas = frutas.shift();

console.log(frutas);

//Dice el indice del elemento
var buscarElemento = frutas.indexOf('Manzana');

console.log(buscarElemento);
