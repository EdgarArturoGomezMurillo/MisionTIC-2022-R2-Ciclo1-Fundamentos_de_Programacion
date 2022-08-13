/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package ejercicio34;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import javax.swing.JOptionPane;

/**
 *
 * @author artur
 */
public class Ejercicio34 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        // Archivo.ddr
        final String RUTA = "D:\\vhiculos.ddr";
        String matricula = JOptionPane.showInputDialog("Introduzca la matricula");
        String marca = JOptionPane.showInputDialog("Introduzca la marca");
        String tamaño_deposito = JOptionPane.showInputDialog("Introduzca el tamaño del deposito");
        double tamañoDeposito = Double.parseDouble(tamaño_deposito);
        String modelo = JOptionPane.showInputDialog("Introduzca el modelo");
        try ( DataOutputStream dos = new DataOutputStream(new FileOutputStream(RUTA, true));  DataInputStream dis = new DataInputStream(new FileInputStream(RUTA))) {
            introduceDatos(dos, matricula, marca, tamañoDeposito, modelo);
            muestraDatos(dis);
        } catch (EOFException e) {
        } catch (IOException e) {
            JOptionPane.showMessageDialog(null, e.getMessage());
        }
    }//end main

    public static void introduceDatos(DataOutputStream dos, String matricula, String marca, double tamañoDeposito, String modelo) throws IOException {
        dos.writeUTF(matricula);
        dos.writeUTF(marca);
        dos.writeDouble(tamañoDeposito);
        dos.writeUTF(modelo);
    }

    public static void muestraDatos(DataInputStream dis) throws IOException {
        while (true) {
            JOptionPane.showMessageDialog(null, "El vehiculo tiene una matricula " + dis.readUTF() + " su marca es " + dis.readUTF() + " el tamaño del deposito es de " + dis.readUTF() + " litros y su modelo es " + dis.readUTF());

        }
    }
}
