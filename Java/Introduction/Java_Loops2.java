import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


// javac xxx.java
// java xxx.class

public class Java_Loops2 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();

            int res = a + b;
            for(int j=1;j<n;j++){
                System.out.print(res + " ");
                res = res + (b * ((int)Math.pow(2, j)));
            }
            System.out.println(res);
        }
        in.close();
    }
}
