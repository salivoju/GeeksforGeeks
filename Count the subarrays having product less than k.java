import java.util.*;
import java.lang.*;
import java.io.*;

class GFG {
	public static void main (String[] args) {
		//code
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-- >0){
		    long n=sc.nextLong();
		    long pro=sc.nextLong();
		    long a[]=new long[(int)n];
		    for(int i=0;i<n;i++)  a[i]=sc.nextLong();
		    int count=0;
    long p = 1; 
    int res = 0; 
    for (int start = 0, end = 0; end < n; end++) { 
        //p *= a.get(end);
        p=p*a[end];
        while (start < end && p >= pro)  
            //p /= a.get(start++); 
            p/=a[start++];
          
       
        if (p < pro) { 
            int len = end - start + 1; 
            res += len; 
        } 
    } 
		    System.out.println(res);
		}
	}
}
