import java.util.HashSet;
import java.util.Set;

public class conjuntos {
    public static void main(String[] args) throws Exception {
        Set<Integer> conjuntoEnteros = new HashSet<Integer>();
        //por asignacion
        conjuntoEnteros.add(5);
        conjuntoEnteros.add(5);
        conjuntoEnteros.add(2);
        conjuntoEnteros.add(1);
        //recorrer el conjunto
        for (Integer i: conjuntoEnteros) {
            System.out.println(i);
        }


    }
}
