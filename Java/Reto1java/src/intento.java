/*import java.util.Scanner;

public class intento {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite el tiempo: ");
        int pTiempo = sc.nextInt();
        System.out.println("Digite el Monto: ");
        double pMonto = sc.nextDouble();
        System.out.println("Digite el interes: ");
        double pInteres = sc.nextDouble();
        System.out.println("la diferencia es: "+ compararInversion(double calcularInteresCompuesto, double calcularInteresSimple));



    }//end main
    public static double calcularInteresSimple(int pTiempo, double pInteres, double pMonto) {

        double interesSimple = ( pMonto * pInteres /100 *pTiempo);
        return interesSimple;
    }

    public static double calcularInteresCompuesto(int pTiempo, double pInteres, double pMonto) {

        double interesCompuesto = ( pMonto * (1 + pInteres/100));
        double interesCompuesto2 = (Math.pow(interesCompuesto, pTiempo)-1);
        return interesCompuesto2;
    }

    public static double  compararInversion(double calcularInteresCompuesto, double calcularInteresSimple){
        double compararinversion = (calcularInteresCompuesto - calcularInteresSimple);
        return compararinversion;
    }


}

*/