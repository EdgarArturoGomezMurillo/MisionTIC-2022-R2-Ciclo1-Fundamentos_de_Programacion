import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dijite un numero entero: ");
        int numero = sc.nextInt();
        System.out.println("El numero " + numero + " tiene " + digitosNumero(numero) + " cifras");
    }//end del main
    public static int digitosNumero(int numero) {
        int contar = 0;
        while (numero != 0){
            numero /= 10; //numero = numero /10
            contar ++; //contar = contar +1            
        }
        return contar;
    }
}
