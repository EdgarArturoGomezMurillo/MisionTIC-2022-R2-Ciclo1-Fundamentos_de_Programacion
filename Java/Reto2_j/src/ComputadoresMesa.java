public class ComputadoresMesa extends Computadores{
    private final static Integer ALMACENAMIENTO_BASE = 50;
    private Integer almacenamiento;
    public ComputadoresMesa() {
        this(PRECIO_BASE, PESO_BASE, CONSUMO_W, ALMACENAMIENTO_BASE);
    }
    
    public ComputadoresMesa(Double precioBase, Integer peso) {
        super(precioBase, peso);
        this.almacenamiento = ALMACENAMIENTO_BASE;
    }

    public ComputadoresMesa(Double precioBase, Integer peso, char consumoW, Integer almacenamiento) {
        super(precioBase, peso, consumoW);
        this.almacenamiento = almacenamiento;
    }
    //Metodos
    public Double calcularPrecio() {
        // Código return adicion;
        Double adicion = super.calcularPrecio();
        if (almacenamiento > 100){
            adicion+=50;
        }
        return adicion;
    }
    public Integer getCarga() {
        return almacenamiento;
    }
    
}
