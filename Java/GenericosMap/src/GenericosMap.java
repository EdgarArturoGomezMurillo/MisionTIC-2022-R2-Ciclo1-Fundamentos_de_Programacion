import java.util.Scanner;

public class GenericosMap {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        var map = new Mapa<String, Integer>();
        System.out.println("digite el nombre del estudiante : ");
        map.setK(sc.nextLine());
        System.out.println("digite la cantidad de asignaturas que ve el estudiante : ");
        map.setV(sc.nextInt());
        System.out.println(map.toString());
        //recibir el numero de cedula y las notas
        var map2 = new Mapa<Integer, Double>();
        System.out.println("digite su numero de cedula: ");
        map2.setK(sc.nextInt());
        System.out.println("digite su promedio final: ");
        map2.setV(sc.nextDouble());
        System.out.println("El estudiante "+map.getK()+" identificado con cedula : "+map2.getK()+" ve "+map.getV()+" asignaturas y obtuvo un promedio de :"+map2.getV() ); 
    }
}