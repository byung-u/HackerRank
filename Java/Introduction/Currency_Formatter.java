import java.io.*;
import java.util.*;
import java.text.*;

public class Currency_Formatter {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double payment = scanner.nextDouble();
        scanner.close();

        NumberFormat currencyFormat = NumberFormat.getCurrencyInstance(Locale.US);
        String us = currencyFormat.format(payment);
        currencyFormat = NumberFormat.getCurrencyInstance(new Locale("en", "IN"));
        String india = currencyFormat.format(payment);
        currencyFormat = NumberFormat.getCurrencyInstance(Locale.CHINA);
        String china = currencyFormat.format(payment);
        currencyFormat = NumberFormat.getCurrencyInstance(Locale.FRANCE);
        String france = currencyFormat.format(payment);


        System.out.println("US: " + us);
        System.out.println("India: " + india);
        System.out.println("China: " + china);
        System.out.println("France: " + france);
    }
}
