import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeMap;

import javax.xml.namespace.QName;

public class conjuntos {
    public static void main(String[] args) throws Exception {
        /*
         * Scanner sc = new Scanner(System.in);
         * Set<Integer> conjuntoEnteros = new HashSet<Integer>();
         * //por asignacion
         * conjuntoEnteros.add(5);
         * conjuntoEnteros.add(5);
         * conjuntoEnteros.add(2);
         * conjuntoEnteros.add(1);
         * //recorrer el conjunto
         * for (Integer i: conjuntoEnteros) {
         * System.out.println(i);
         * }
         * System.out.println("el tamaño del conjunto es : "+ conjuntoEnteros.size());
         * System.out.println("porfavor dijite el numero a buscar: ");
         * int numero = sc.nextInt();
         * if ( conjuntoEnteros.contains(numero)) {
         * System.out.println("el numero "+ numero + " si esta");
         * }
         * else{
         * System.out.println("el numero "+ numero + " no esta");
         * }
         */
        /*
         * System.out.
         * println("----------------------------------- COLAS ----------------------------------------"
         * );
         * Queue<Integer> colaEnteros = new PriorityQueue<>();
         * colaEnteros.add(1);
         * colaEnteros.add(10);
         * colaEnteros.add(5);
         * colaEnteros.offer(3);
         * colaEnteros.offer(5);
         * for (Integer i : colaEnteros){
         * System.out.println(i);
         * }
         * System.out.println("el tamaño de la cola: "+colaEnteros.size());
         * colaEnteros.remove();
         * for (Integer i : colaEnteros){
         * System.out.println(i);
         * }
         */
        /*System.out.println("--------------------------------------MAPAS----------------------------------------");
        // datos persona cedula nombre y apellidos
        Map<Integer, String> mapa = new HashMap<>();
        // por asignacion
        mapa.put(1001300243, " arturo gomez murillo");
        mapa.put(1001300242, " daniel gomez murillo");
        mapa.put(1001300241, " pepe gomez murillo");
        System.out.println("datos de las personas: " + mapa);
        System.out.println("ORDENADO");
        // datos persona cedula nombre y apellidos
        Map<Integer, String> mapa2 = new TreeMap<>();
        // por asignacion
        mapa2.put(1001300253, " julian gomez murillo");
        mapa2.put(1001300252, " daniel gomez murillo");
        mapa2.put(1001300251, " pepe gomez murillo");
        System.out.println("datos de las personas: " + mapa2);
        System.out.println("ORDENADO POR INSERCION");
        // datos persona cedula nombre y apellidos
        Map<Integer, String> mapa3 = new LinkedHashMap<>();
        // por asignacion
        mapa3.put(1001300253, " julian gomez murillo");
        mapa3.put(1001300252, " daniel gomez murillo");
        mapa3.put(1001300251, " pepe gomez murillo");
        System.out.println("datos de las personas: " + mapa3);*/

        System.out.println("dinamica");
        Map<Integer, String> mapa4 = new TreeMap<>();
        Scanner sc = new Scanner(System.in);
        System.out.print("cuantos clientes desea ingresar:  ");
        int nC = sc.nextInt();
        for (int i = 0; i < nC; i++) {
            System.out.println("digite la cedula: " + (i + 1) + ":");
            int cedula = sc.nextInt();
            System.out.println("digite el nombre del cliente: " + (i + 1) + ":");
            sc.nextLine();//limpiar
            String nombre = sc.nextLine();
            mapa4.put(cedula, nombre);
        }
        System.out.println(mapa4);
        System.out.println();
    }
}
