var estudiantes = ['Maria', 'Sergio', 'rosa'];

const saludarEstudiantes = (estudiante) => {
    console.log(`Hola!, ${estudiante}`);
};

for (let i = 0; i < estudiantes.length; i++) {
    saludarEstudiantes(estudiantes[i]);
}

// for (const estudiante of estudiantes) {
//     saludarEstudiantes(estudiante);
// }

function solution(estudiantes, deathCount, nuevo) {
    // Tu código aquí 👈
    if (deathCount === 0) {
      estudiantes.push(nuevo);
    } else if (deathCount > 0) {
      for (let i = 0; i < deathCount; i++){
        estudiantes.pop();
      } 
      estudiantes.push(nuevo);
    }
    return estudiantes;
  }

let ejemplo1 = solution(["Nico", "Zule"], 0, "Santi");
let ejemplo2 =solution(["Juan", "Juanita", "Daniela"], 2, "Julian");

console.log(ejemplo1)
console.log(ejemplo2)