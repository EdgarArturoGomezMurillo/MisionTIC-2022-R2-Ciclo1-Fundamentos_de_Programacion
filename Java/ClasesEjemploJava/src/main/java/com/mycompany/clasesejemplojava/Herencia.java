/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.clasesejemplojava;

import java.util.Date;
import java.util.Scanner;

/**
 *
 * @author artur
 */
public class Herencia {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // dinamica --> cliente
        System.out.println("-------------Seccion de clientes-------------");
        System.out.println("");
        System.out.print("Porfavor digite la cantidad de clientes que desea ingresar al sistema : ");
        int nClientes = sc.nextInt();
        sc.nextLine();// resetear el buffer
        // instancia de clase -- Array...
        Cliente[] cliente = new Cliente[nClientes];
        for (int i = 0; i < cliente.length; i++) {
            System.out.println("Digite el nombre del cliente " + (i + 1) + ":");
            String nombre = sc.nextLine();
            System.out.println("El cliente " + nombre + " es un cliente VIP (true o  false) : ");
            boolean Vip = sc.nextBoolean();
            cliente[i] = new Cliente(new Date(), Vip);
            cliente[i].setNombre(nombre);
            sc.nextLine();
        }
        // mostrar clientes
        for (int i = 0; i < cliente.length; i++) {
            System.out.println(cliente[i].toString());
        }
        System.out.println("-------------Seccion de empleados-------------");
        System.out.println("");
        System.out.print("Cuantos empleados desea ingresar: ");
        int nEmpleados = sc.nextInt();
        sc.nextLine();//limpiar buffer
        Empleado [] empleado = new Empleado[nEmpleados];
        for (int i = 0; i < nEmpleados; i++) {
            System.out.println("Digite el nombre del empleado " +(i+1) +":");
            String nombreE = sc.nextLine();
            System.out.println("Digite el genero  del empleado(f/m/o) "+(i+1)+":");
            char genero = sc.next().charAt(0);
            System.out.println("Digite la edad del empleado "+ (i+1) +":");
            int edad = sc.nextInt();
            sc.nextLine();//limpiar buffer
            System.out.println("Digite la direccion del empleado "+(i+1)+":");
            String direccion = sc.nextLine();
            System.out.println("Digite el sueldo  del empleado "+(i+1)+":");
            double sueldo = sc.nextDouble();
            //guardamos en la instancia de clase
            empleado[i]= new Empleado (sueldo);
            empleado[i].setNombre(nombreE);
            empleado[i].setGenero(genero);
            empleado[i].setEdad(edad);
            empleado[i].setDireccion(direccion);
            sc.nextLine();//limpiar el buffer
        }
        for (int i = 0; i < empleado.length; i++) {
            System.out.println(empleado[i].toString());
        }
    }// end main
}
