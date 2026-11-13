package main.java.splitstirngs;

import java.util.Arrays;

class StringSplit {
    public static String[] solution(String s) {
        int arrayLength = (int) Math.ceil(s.length() / 2.0);
        String[] splited = new String[arrayLength];
        StringBuilder toCharString = new StringBuilder();
        int i = 0;
        for (char c : s.toCharArray()) {
            toCharString.append(c);
            i++;
            if (i % 2 == 0) {
                splited[i/2 - 1] = toCharString.toString();
                toCharString.setLength(0);
            }
        }

        if (!toCharString.isEmpty()) {
            toCharString.append("_");
            splited[arrayLength - 1] = toCharString.toString();
        }

        return splited;
    }
}

public class Main {
    static void main(String[] args) {
        System.out.println(Arrays.toString(StringSplit.solution("abcde")));
    }
}
