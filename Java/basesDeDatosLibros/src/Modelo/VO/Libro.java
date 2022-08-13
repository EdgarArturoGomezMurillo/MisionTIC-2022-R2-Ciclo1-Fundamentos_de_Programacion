/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Modelo.VO;

/**
 *
 * @author artur
 */
public class Libro {

    //value object
    private int isbn;
    private String titulo;
    private String año;

    public Libro() {
    }

    public Libro(int isbn, String titulo, String año) {
        this.isbn = isbn;
        this.titulo = titulo;
        this.año = año;
    }

    public int getIsbn() {
        return isbn;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAño() {
        return año;
    }

    public void setIsbn(int isbn) {
        this.isbn = isbn;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAño(String año) {
        this.año = año;
    }

}
