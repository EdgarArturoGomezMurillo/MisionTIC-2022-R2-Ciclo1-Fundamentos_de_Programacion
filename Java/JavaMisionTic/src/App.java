import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;


public class App {
    public static void main(String[] args) throws IOException {

        System.out.println("Hello, World!");
        System.out.println("Hola mundo en java");
        // hola mundo en java
        /*
        comentario
        varias lineas
        */
        //recibir por teclado 
        // scanner --- clases 
        Scanner sc = new Scanner(System.in, "UTF-8");
        System.out.println("porfavor dijite su nombre: ");
        String nombre = sc.nextLine();
        System.out.println("su nombre es: "+nombre);
        //sc.close();

        Scanner ed = new Scanner(System.in);
        System.out.println("porfavor dijite su edad: ");
        int Edad = ed.nextInt();
        System.out.println("su edad es: " + Edad);
        //ed.close();

        //segunda forma 
        //Buffer....
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in, "UTF-8"));
        System.out.println("porfavor dijite su apellido: ");
        String apellido = br.readLine();
        System.out.println("su apellido es: "+apellido);

        //condicional
        /*
         if codicion:
            cod
            cod 
         */
        //no existe la identacion
        
            
    
    }
    
}