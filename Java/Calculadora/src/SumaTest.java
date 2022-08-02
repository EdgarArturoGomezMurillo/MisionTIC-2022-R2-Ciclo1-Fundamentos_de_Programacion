import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class SumaTest {
    @Test
    void testSumar() {
        System.out.println("sumar");
        int numero1 = 2;
        int numero2 = 1;
        Suma instance = new Suma();
        int expResult = 3;
        int result = instance.sumar(numero1, numero2);
        assertEquals(expResult, result);
    }
}
