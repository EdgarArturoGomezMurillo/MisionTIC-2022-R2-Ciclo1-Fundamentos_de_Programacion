import java.util.Scanner;

public class saludo {
    public static void main(String[] args) throws Exception {
        try (Scanner sc = new Scanner(System.in, "UTF-8")) {
            System.out.println("porfavor dijite su nombre: ");
            String nombre = sc.nextLine();
            System.out.println(saludo(nombre));
        }
    }//end main 
    //metodos
    public static String saludo(String nombre) {
        return "hola " + nombre + " bienvenido a java";       
    }

}
