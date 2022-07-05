import java.util.Scanner;

public class ejercicioNO4 {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Escriba los grados Celsius que quiere convertir a Fahrenheit : ");
        int celsius = sc.nextInt();
        System.out.println("Los " + celsius + " grados Celsius en Fahrenheit son = "+Fahrenheit(celsius));
    }//end main
    public static float Fahrenheit(float celsius){
        return 32 + (9*celsius/5);
    }
}
