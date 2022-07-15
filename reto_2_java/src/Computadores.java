public class Computadores {
   private int PESO_BASE;
   private char CONSUMO_W_BASE;
   private double PRECIO_BASE;
   private Integer peso;
   private char consumoW;
   private Double precioBase;
    
    // Variables base
    // Variables
    // Constructores public Computadores(){
    // Constructor
    public Computadores() {
    }
    public Computadores(Double precioBase, Integer peso) {
    }
    public Computadores(Double precioBase, Integer peso, char consumoW) {
    this.precioBase = precioBase;
    this.peso = peso;
    this.consumoW = consumoW;
    }
    // Metodos
    public Double calcularPrecio() {
    Double adicion = 0.0;
    // Código
    }
    public Integer getPeso() {
        return peso;
    }
    public void setPeso(Integer peso) {
        this.peso = peso;
    }
    public char getConsumoW() {
        return consumoW;
    }
    public void setConsumoW(char consumoW) {
        this.consumoW = consumoW;
    }
    public Double getPrecioBase() {
        return precioBase;
    }
    public void setPrecioBase(Double precioBase) {
        this.precioBase = precioBase;
    }
    
}