import java.util.Scanner;

public class condicion {
    public static void main(String[] args) throws Exception {
        
        Scanner sc = new Scanner(System.in);
        System.out.println("Porfavor ingrese un numero entero : ");
        int numero = sc.nextInt();
        System.out.println("El numero " + numero + " es = "+paroInpar(numero) );
    }//End main
    public static String paroInpar (int numero) {
        String parinpar = (numero % 2 == 0) ? "Par" : "Inpar";
        return parinpar;  
    }

}
