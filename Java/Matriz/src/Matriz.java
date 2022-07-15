import java.util.Scanner;

public class Matriz {
    /**
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        //tipo de datos [][] nombreMatriz = new tipo de datos [filas][columnas]
        Scanner sc = new Scanner(System.in);
        System.out.println("Digite la cantidad de filas: ");
        int filas = sc.nextInt();
        System.out.println("digite el numero de columnas: ");
        int columnas = sc.nextInt();
        if ((filas < 1) | (columnas < 1)){
            System.out.println("Porfavor dijite una solucion valida: ");
        }
        else{
            int [][] Matriz = new int[filas][columnas];
            int numero;
            int contar=0;
            for (int i = 0; i < filas; i++){
                for (int j = 0  ; j < columnas; j++){
                    System.out.print("Digite el numero "+(++contar)+" : ");
                    numero = sc.nextInt();
                    Matriz[i][j] = numero;
                }
            }
            System.out.println("creando la matriz.....");
            for (int i = 0; i < filas; i++) {
                for (int j = 0; j < columnas; j++){
                    System.out.print(Matriz[i][j]+" ");
                    System.out.println("En el indice "+i+" esta el valor: " + Matriz[i][j]);
                }
                System.out.println();
            }
        }
    }//end main
}
