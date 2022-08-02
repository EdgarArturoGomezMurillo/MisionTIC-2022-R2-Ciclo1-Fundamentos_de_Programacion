public class decano extends persona{
    private String categoria;

    public decano() {
    }
    
    public decano(String categoria) {
        this.categoria = categoria;
    }

    public String getCategoria() {
        return categoria;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    @Override
    public String toString() {
        return "--------- Datos del decano ---------" + "\nNombre : " + super.getNombre() + "\nApellido : "
        + super.getApellido() + "\nCategoria : " + categoria;
    }

    

    
}
