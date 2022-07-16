public class Mapa <K,V>{
    private K k;
    private V v;
    public Mapa() {
    }
    public Mapa(K k, V v) {
        this.k = k;
        this.v = v;
    }
    public K getK() {
        return k;
    }
    public void setK(K k) {
        this.k = k;
    }
    public V getV() {
        return v;
    }
    public void setV(V v) {
        this.v = v;
    }
    @Override
    public String toString() {
        return "Mapa [k=" + k + ", v=" + v + "]";
    }
    
    
    
}
