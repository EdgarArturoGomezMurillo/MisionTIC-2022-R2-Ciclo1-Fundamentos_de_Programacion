//esto es un archivo externo script.js
//otra forma de visualicacion alert
// alert("hola mundo");
//otra forma de viaualizcion
console.log("mensaje en consola");
console.log("mensaje en consola");
var a = 10;
document.write("el valor de a es : " + a);
document.write("<br>");
// const y let no se pueden volver a utilizar en el codigo
const PI = 3.1416;
document.write("el valor de PI es : " + PI);
document.write("<br>");
var parrafos = document.getElementsByTagName("p");
document.write("<h2>los usuarios de js</h2>");
document.write("<br>");
document.write(parrafos[0].innerHTML);
// recorrewr con for
for (var i = 0; i < parrafos.length; i++) {
  document.write(parrafos[i].innerHTML);
  document.write("<br>");
}
// funcion
function holamundofuncion() {
  alert("hola mundo desde funcion");
}
function encender() {
  document.getElementById("foco").src = "img/focoencendido.gif";
}
function apagar() {
  document.getElementById("foco").src = "img/foco.gif";
}
function datosbasicos() {
  var nombre = document.getElementById("nombre").value;
  var apellidos = document.getElementById("apellido").value;
  var ciudad = document.getElementById("ciudad").value;
  alert(
    "Esta seguro que desea registrar en el sistema los siguientes datos: \nNombre: " +
      nombre +
      "\nApellidos: " +
      apellidos +
      "\nCiudad: " +
      ciudad
  );
}
