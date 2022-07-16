public class Computadores {
    public static final Integer PESO_BASE = 5;
    public static final char CONSUMO_W = 'F';
    public static final Double PRECIO_BASE = 100.0;
    public Double precioBase;
    public Integer peso;
    public char consumoW;

    public Computadores() {
        this.precioBase = PRECIO_BASE;
        this.consumoW = CONSUMO_W;
        this.peso = PESO_BASE;
    }

    public Computadores(Double precioBase, Integer peso) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = CONSUMO_W;
    }

    public Computadores(Double precioBase, Integer peso, char consumoW) {
        this.precioBase = precioBase;
        this.peso = peso;
        this.consumoW = consumoW;
    }

    // Metodos
    public Double calcularPrecio() {
        Double adicion = 0.0;
        // codigo
        switch (consumoW) {
            case 'A':
                adicion += 100;
                break;
            case 'B':
                adicion += 80;
                break;
            case 'C':
                adicion += 60;
                break;
            case 'D':
                adicion += 50;
                break;
            case 'E':
                adicion += 30;
                break;
            case 'F':
                adicion += 10;
                break;

        }
        if (peso >= 0 & peso<19) {
            adicion +=10;
        }else if (peso >= 20 & peso<49){
            adicion +=50;
        }else if (peso >= 50 & peso<79){
            adicion+=80;
        }else if (peso >= 80){
            adicion+=100;
        }
        return precioBase+adicion;
    }

    public Double getPrecioBase() {
        return precioBase;
    }

    public Integer getPeso() {
        return peso;
    }

    public char getConsumoW() {
        return consumoW;
    }
}
