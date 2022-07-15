import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dijite su nombre : ");
        String nombre = sc.nextLine();
        System.out.println("Dijite sus apellidos : ");
        String apellido = sc.nextLine();
        String nombreApellido = nombre + " " + apellido;
        System.out.println("Bienvenido : "+  nombreApellido);
        System.out.println("la longitud de la cadena es : "+nombreApellido.length());
        System.out.println("el indice de la letra e es : "+nombreApellido.indexOf("e"));
        System.out.println("el indice de la ultima letra e es : "+nombreApellido.lastIndexOf("e"));
        System.out.println("el caracter en la posicion 4 es : "+nombreApellido.charAt(4));
        System.out.println("El substring de calletana para ana es 6,9 : "+nombreApellido.substring(6, 10));
        System.out.println("convertir en mayuscula : "+nombreApellido.toUpperCase());
        System.out.println("convertir en minuscula : "+nombreApellido.toLowerCase());
        System.out.println("sin espacion al inicio y final "+nombreApellido.trim());
        //comparacion de string
            if(nombre.equals(apellido)){
            System.out.println("el nombre es igual a apellido");
            }
            if (nombre.equalsIgnoreCase(apellido)){
                System.out.println("son iguales, sin tener en cuenta la mayuscula");
            }
    }
}
