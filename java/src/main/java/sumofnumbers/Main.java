package main.java.sumofnumbers;

class Sum
{
    public int GetSum(int a, int b)
    {
        if (a == b) {
            return a;
        }

        int sumOfNumbers = 0;
        int bigger = Math.max(a, b);
        int smaller = Math.min(a, b);

        int number = smaller;
        while (number <= bigger) {
            sumOfNumbers += number;
            number += 1;
        }

        return sumOfNumbers;
    }
}

public class Main {
    public static void main(String[] args) {
        Sum sum = new Sum();
        System.out.println(sum.GetSum(1, 2));
        System.out.println(sum.GetSum(1, 0));
        System.out.println(sum.GetSum(-1, 2));
        System.out.println(sum.GetSum(-1, -1));
    }
}
