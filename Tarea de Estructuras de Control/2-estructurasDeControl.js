// estructurasDeControl.js

// Ejercicio 1: Condicionales if-else
// Instrucción: Escribe una función que reciba un número y verifique si es par o impar.
// Imprime "El número es par" o "El número es impar" según corresponda.
function verificarParidad(numero) {
    numero = 4
    if (numero % 2 == 0){
        console.log("El numero es par")
    }else{
        console.log("El numero es impar")
    }
}

// Ejercicio 2: Condicionales anidados
// Instrucción: Escribe una función que reciba una edad y determine si la persona es:
// "Menor de edad" (menor a 18), "Adulto" (entre 18 y 65), o "Adulto mayor" (mayor a 65).
function clasificarEdad(edad) {
    edad = 24
    if (edad >= 18 && edad <= 65){
        console.log("Usted es mayor de edad")
    }else if(edad >= 65){
        console.log("Usted es un adulto mayor")
    }else{
        console.log("Usted es menor de edad")
    }
}

// Ejercicio 3: Bucles while
// Instrucción: Crea una función que reciba un número entero positivo y utilice un bucle `while` para imprimir todos los números desde ese número hasta 0.
function cuentaRegresiva(numero) {
    numero = 10
    while (numero > 0){
        console.log(numero)
        numero--
    }
}

// Ejercicio 4: Bucles do-while
// Instrucción: Escribe una función que imprima "Estoy aprendiendo JavaScript" 5 veces utilizando un bucle `do-while`.
function repetirMensaje() {
    let i = 5
    do{
        console.log("Estoy aprendiendo JavaScript")
        i--
    }while(i > 0)
}

// Ejercicio 5: Bucle for
// Instrucción: Escribe una función que reciba un número entero positivo y utilice un bucle `for` para imprimir todos los números pares entre 0 y ese número.
function imprimirPares(numero) {
    numero = 10
    for (i = 0; i <= 10; i++){
        if (i % 2 == 0){
            console.log(i)
        }
    }
}

// Ejercicio 6: Uso de break
// Instrucción: Escribe una función que recorra los números del 1 al 10, pero detén el bucle cuando el número sea igual a 6.
function detenerEnSeis() {
    for (i = 1; i <= 10; i++){
        if (i === 6){
            break
        }
        console.log(i)
    }
}

// Ejercicio 7: Uso de continue
// Instrucción: Crea una función que recorra los números del 1 al 10, pero que se salte el número 5 usando `continue`.
function saltarCinco() {
    for (i = 1; i <= 10; i++){
        if (i === 5){
            continue
        }
        console.log(i)
    }
}

// Ejercicio 8: Switch básico
// Instrucción: Escribe una función que reciba un número del 1 al 7 y devuelva el día de la semana correspondiente (1 es "Lunes", 2 es "Martes", ..., 7 es "Domingo"). Usa la estructura `switch`.
function obtenerDiaSemana(dia) {
    dia = 2
    switch (dia) {
        case 1:
            console.log("Hoy es Domingo")
            break
        case 2:
            console.log("Hoy es Lunes")
            break
        case 3:
            console.log("Hoy es Martes")
            break
        case 4:
            console.log("Hoy es Miercoles")
            break
        case 5:
            console.log("Hoy es Jueves")
            break
        case 6:
            console.log("Hoy es Viernes")
            break
        case 7:
            console.log("Hoy es Sabado")
            break
        default:
            break
    }
}

// Ejercicio 9: Switch con múltiples casos
// Instrucción: Escribe una función que reciba un carácter y devuelva si es una vocal. Utiliza un `switch` y agrupa los casos para las vocales (a, e, i, o, u).
function esVocal(letra) {
    letra = "a"
    switch (letra){
        case "a":
        case "e":
        case "i":
        case "o":
        case "u":
            console.log(`${letra} Es una vocal`)
            break;
        default:
            console.log(`${letra} No es una vocal`)
            break
    }
}

// Ejercicio 10: Condicionales complejos con operadores lógicos
// Instrucción: Escribe una función que reciba tres números y determine si todos son positivos, al menos uno es negativo, o todos son negativos. Usa operadores lógicos (`&&`, `||`).
function evaluarNumeros(a, b, c) {
    a = -1; b = 2; c = -3

    if (a > 0 && b > 0 && c > 0){
        console.log("Todos los numeros son positivos")
    }else if (a > 0 || b > 0 || c > 0){
        console.log("Al menos uno de los numeros son negativos")
    }else{
        console.log("Todos los numeros son negativos")
    }
}

// Exportar todas las funciones
/*
export {
    verificarParidad,
    clasificarEdad,
    cuentaRegresiva,
    repetirMensaje,
    imprimirPares,
    detenerEnSeis,
    saltarCinco,
    obtenerDiaSemana,
    esVocal,
    evaluarNumeros,
};*/
verificarParidad()
clasificarEdad()
cuentaRegresiva()
repetirMensaje()
imprimirPares()
detenerEnSeis()
saltarCinco()
obtenerDiaSemana()
esVocal()
evaluarNumeros()