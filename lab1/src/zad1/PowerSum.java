package zad1;

public class PowerSum {
	public int n;
	public int PowerSum(int n){
		int x, i, sum;
		for (x = 1, i = 0, sum = 0; i<n; x++, i++) {
			if (i == n - 1) {
				sum = sum + x*x;
			}
			else {
				sum = sum + x*x;
			}
		}
	}
	return sum;
}