import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


// javac xxx.java
// java xxx

public class Datatypes {

    public static void main(String []argh)
    {
        Scanner sc = new Scanner(System.in);
        int t=sc.nextInt();

        for(int i=0;i<t;i++)
        {

            try
            {
                long x=sc.nextLong();
                System.out.println(x+" can be fitted in:");
                if(x<=Long.MAX_VALUE) { // -9223372036854775808,9223372036854775807 
                    if(x>=Byte.MIN_VALUE && x<=Byte.MAX_VALUE) { // -128, 127
                        System.out.println("* byte");
                    }
                    if(x>=Short.MIN_VALUE && x<=Short.MAX_VALUE) { // -32768, 32767
                        System.out.println("* short");
                    }
                    if(x>=Integer.MIN_VALUE && x<=Integer.MAX_VALUE) { // -2147483648, 2147483647
                        System.out.println("* int");
                    }
                    if(x>=Long.MIN_VALUE && x<=Long.MAX_VALUE) { // -9223372036854775808,9223372036854775807 
                        System.out.println("* long");
                    }
                }
            }
            catch(Exception e)
            {
                System.out.println(sc.next()+" can't be fitted anywhere.");
            }

        }
    }
}
