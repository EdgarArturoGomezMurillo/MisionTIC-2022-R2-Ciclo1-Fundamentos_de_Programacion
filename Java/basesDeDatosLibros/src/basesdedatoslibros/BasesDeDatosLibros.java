/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package basesdedatoslibros;

import java.sql.*;
import java.util.Scanner;

/**
 *
 * @author artur
 */
public class BasesDeDatosLibros {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Conexion cc = new Conexion();
        Connection cn = cc.conectar();
    }
    Scanner sc = new Scanner(System.in);
    boolean continuar = true;

    
        do{
            System.out.println("Elija la opción a realizar sobre la BD");
        System.out.println("""
                           1. Guardar
                           2. Buscar
                           3. Listar Libros
                           4. Actualizar unidades
                           5. Consultar unidades
                           6. Vender Libro
                           7. Salir
                           """);
        System.out.print("Digite la opción");
        int opcion = sc.nextInt();
        switch (opcion) {
            case 1:
                System.out.println("********Guardar Libro*******");
                break;

            case 2:
                System.out.println("********Buscar Libro*******");
                break;
            case 3:
                System.out.println("********Listar Libros*******");
                break;
            case 4:
                System.out.println("********Actualizar unidades del libro*******");
                break;
            case 5:
                System.out.println("********Consultar unidades de libro*******");
                break;
            case 6:
                System.out.println("********Vender Libro*******");
                break;
            case 7:
                System.out.println("Gracias por utilizar nuestro sistema");
                continuar = false;
                break;
            default:
                System.out.println("No es una opción válida");

        }

    } while (continuar);
    
}
