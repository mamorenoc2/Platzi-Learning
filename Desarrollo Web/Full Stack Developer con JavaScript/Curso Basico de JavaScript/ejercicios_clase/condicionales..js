let piedra = 1;
let papel = 2;
let tijera = 3;

let juego = (usuario, computador) => {
    let resultado = 0;
    if (usuario != computador) {
        if (usuario === 1 && computador === 3 ) {
            resultado = "Ganó el usuario";
        } else if(usuario === 2 && computador === 1 ){
            resultado = "Ganó el usuario";
        } else if(usuario === 3 && computador === 2 ){
            resultado = "Ganó el usuario";
        } else {
            resultado = "Gano el computador";
        }
    } else {
        resultado = "Empate"
    }
    return resultado;
};

console.log(juego(3,1));