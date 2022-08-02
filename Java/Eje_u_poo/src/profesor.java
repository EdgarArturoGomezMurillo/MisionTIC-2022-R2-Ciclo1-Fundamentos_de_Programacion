public class profesor extends persona {
    private String categoria;

    public profesor() {
    }

    public profesor(String categoria) {
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
        return "--------- Datos del profesor "+  super.getNombre() +" ---------" + "\nNombre : " + super.getNombre() + "\nApellido : "
        + super.getApellido() + "\nCategoria : " + categoria;
    }
    
}
