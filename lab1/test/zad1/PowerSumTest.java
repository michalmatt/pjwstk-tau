package zad1;

import static org.junit.Assert.*;

import org.junit.*;

public class PowerSumTest {
	private PowerSum ps;
	
	@Before
	public void setUp(){
		ps = new PowerSum();
		System.out.println("Before");
	}
	
	@After
	public void tearDown(){
		ps = null;
		System.out.println("After");
	}
	
	@Test
	public void testPowerSumCalculations() {
		int result = ps.PowerSum(3);
		assertEquals(14,result);
		System.out.println("Test1: Calculations");
	}
	
}
