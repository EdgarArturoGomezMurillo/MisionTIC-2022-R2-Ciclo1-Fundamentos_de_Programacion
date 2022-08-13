/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelo.DAO;
import basesdedatoslibros. *;
import java.sql.*;
/**
 *
 * @author artur
 */
public class GuardarLibro {
    public void guardar (int isbn, String titulo, int año){
        
    Conexion cc = new Conexion();
    Connection cn = cc.conectar();}
    PreparedStatement ps = cn.prepareStatement("INSERT INTO libro VALUES (?,?,?)");
    
}
