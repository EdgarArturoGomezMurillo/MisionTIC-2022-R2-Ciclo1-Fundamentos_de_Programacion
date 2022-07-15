import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Colecciones {
    public static void main(String[] args) throws Exception {
        //colecciones 
        //listas
        Scanner sc = new Scanner(System.in);    
        List <Integer> listaEnteros = new ArrayList<>();
        //Adicionar por asignacion
        listaEnteros.add(8);
        System.out.println(listaEnteros.get(0));
        System.out.println("de forma dinamica");
        System.out.print("Digite la cantidad de numeros que desea añadir a la lista: ");
        int numeroLista = sc.nextInt();
        for (int i = 0; i < numeroLista; i++){
            System.out.print("Digite el numero "+ (i + 1) +":");
            int numero = sc.nextInt();
            listaEnteros.add(numero);
        }
        System.out.println("");
        
        System.out.println("Mostrar lista de forma convencional");
        for (int i = 0; i < listaEnteros.size(); i++){
            System.out.println(listaEnteros.get(i));
        }
        System.out.println("otra forma foreach");
        for (Integer i : listaEnteros){
            System.out.println(i);
        }
        System.out.println("tamaño de la lista : "+listaEnteros.size());
        System.out.println("Digite el numero a buscar: ");
        int numeroB = sc.nextInt();
        if (listaEnteros.contains(numeroB)){
            System.out.println("El objeto "+numeroB+" Si se encuentra en la lista");
        }
        else{
            System.out.println("El objeto "+numeroB+" No se encuentra en la lista");
        }
        //eliminar un objeto de la lista
        System.out.println("Digite el numero de la lista a eliminar");
        int nEliminar = sc.nextInt();
        listaEnteros.remove (nEliminar);
        System.out.println("Nueva lista sin el numero");
        for (int i = 0; i < listaEnteros.size(); i++){
            System.out.println(listaEnteros.get(i));
        }
    }//end main
}
