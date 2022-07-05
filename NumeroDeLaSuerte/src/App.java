import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        System.out.println("Dijite su fecha de nacimiento");
        System.out.println("Dia de nacimiento: ");
        int dia = sc.nextInt();
        System.out.println("Mes: ");
        int Mes = sc.nextInt();
        System.out.println("Año: ");
        int Año = sc.nextInt();
        System.out.println("Su numero de la suerte es : "+ numerosuerte(dia, Mes, Año));
        System.out.println("su numero de la suerte en str es :  "+ numerosuerte2(dia, Mes, Año));
    }//end main
    public static int numerosuerte (int dia, int Mes, int Año){
        int suma= dia + Mes + Año;
        int cifra1 = suma/1000;
        int cifra2 = suma/100 % 10;
        int cifra3 = suma/10 % 10;
        int cifra4 = suma % 10;
        int numerosuerte = (cifra1 + cifra2 + cifra3 + cifra4);
        return numerosuerte;

    }
    public static int numerosuerte2 (int dia, int Mes, int Año){
        int suma = dia+Mes+Año;
        String sumaS = String.valueOf(suma);
        int sumaA = 0;
        for (int i=0; i<sumaS.length(); i++){
            int n = Integer.parseInt(sumaS.charAt(i)+"");
            sumaA+=n;
        }
        return sumaA;
    }
}
