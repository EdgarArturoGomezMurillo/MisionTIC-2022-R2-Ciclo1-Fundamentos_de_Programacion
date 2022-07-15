import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite la velocidad en Km/h: ");
        double velocidadk = sc.nextDouble();
        System.out.println("La velocidad en M/s es: "+ kmAms(velocidadk) );
        


        
    }//end main
    public static double kmAms (double velocidadk){

        double kmams = velocidadk * 1000/3600;
        double kmr = Math.round(kmams*100.0)/100.0;
        return kmr;
    }
}
