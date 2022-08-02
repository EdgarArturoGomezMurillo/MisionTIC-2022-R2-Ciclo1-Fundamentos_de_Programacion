public class director extends persona {
    private String categoria;

    public director() {
    }

    public director(String categoria) {
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
        return "--------- Datos del director "+  super.getNombre() +" ---------" + "\nNombre : " + super.getNombre() + "\nApellido : "
                + super.getApellido() + "\nCategoria : " + categoria;
    }

}
