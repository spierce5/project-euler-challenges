package driver;
import java.util.*;
import java.io.File;
import java.io.FileReader; 
import java.io.IOException; 
import java.math.BigInteger;


public class driver {

	public static void main(String[] args) {
		String fileName = "Library/data.txt";
		StringBuilder series = new StringBuilder();
		Scanner sc = null;
		
		try {
			sc = new Scanner(new File(fileName));
			while (sc.hasNextLine()) {
				String line = sc.nextLine();
				series.append(line);			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		int n = 13; 			//Choose number of terms for product
		BigInteger largestProduct = new BigInteger("0"); 
		int[] terms;
		terms = new int[n];
		
		
		for(int i=0; i < series.length()-n+1; i++) {
			BigInteger product = new BigInteger("1");
			int[] temp;
			temp = new int[n];
			
			for(int j=0; j<n; j++) {
				temp[j] = Character.getNumericValue(series.charAt(i+j));
			}
		
			for(int k: temp) {
				product = product.multiply(BigInteger.valueOf(k));
			}
			
			if(product.compareTo(largestProduct)>0) {
				largestProduct = product;
				terms = temp;
			}
		}
		for(int i=0; i<n; i++) {
			System.out.print(terms[i]);
			if(i<n-1) {
				System.out.print(" * ");
			}
		}
		System.out.print(" = " + largestProduct);
	}

}
