/*-----------  FUNCIONES EN JAVASCRIPT---------*/

// Declaración
function suma (a,b){
    return a + b
}
/* 
function nombre (parámetros) {
    contenido
    return valor
} 
*/


// Invocación
suma(2,3)
// nombre(argumentos)

var resultado1 = suma(2,3)
var resultado2 = suma(4,6)
var resultado3 = suma(10,12)

console.log(resultado1) //5
console.log(resultado2) //10
console.log(resultado3) //22



// Declaración
function saludar(nombre){
    console.log("Hola " + nombre) 
}
// Invocaciones
saludar("JavaScript") //"Hola JavaScript"
saludar("Platzi") // "Hola Platzi"



console.log(`Hola ${nombre}`)


// Declaración
var suma = function (a, b) {
    return a + b
  }
  // Invocación
  var resultado = suma(2, 2)
  
  console.log(resultado) //4

//Scope global
var nombre = "JavaScript"

function saludar(){
    console.log("Hola " + nombre)
}

saludar()

//Scope local
function saludo() {
    let nombre = "Andres"
    console.log(nombre)
}

saludo() // "Andres"
console.log(nombre) 
// ReferenceError: nombre is not defined


// ------------------- HOISTING

console.log(nombre) // undefined
var nombre = "Andres" 

/*
// Hoistin: Declara y asigna undefined
var nombre = undefined
console.log(nombre) // undefined
nombre = "Andres"

*/


console.log( saludar() )

function saludar() {
    return "Hola"
}

/**
 * // Hoisting: Declara la función antes 
 * de ser invocada
function saludar() {
    return "Hola"
}

console.log( saludar() ) // "Hola"
 */