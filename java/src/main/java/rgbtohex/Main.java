package main.java.rgbtohex;

class RgbToHex {

    private static final char[] hexaDictionary = new char[16];

    static String hexRepresentation(int c) {
        char[] hexString = new char[2];

        for (int i = 1; i >= 0; i--) {
            int valueToHex = c % 16;
            c = c / 16;
            hexString[i] = hexaDictionary[valueToHex];
        }

        return new String(hexString);
    }

    static int checkValue(int a) {
        a = Math.min(255, a);
        a = Math.max(0, a);
        return a;
    }

    public static String rgb(int r, int g, int b) {
        int[] rgbValues = {r, g, b};

        for (int i = 0; i < 16; i++) {
            hexaDictionary[i] = Character.toUpperCase(Character.forDigit(i, 16));
        }

        StringBuilder hex = new StringBuilder(new String());
        for (int value : rgbValues) {
            value = checkValue(value);
            hex.append(hexRepresentation(value));
        }
        return hex.toString();
    }
}

public class Main {
    public static void main(String[] args) {
        System.out.println(RgbToHex.rgb(1, 2, 3));
        System.out.println(RgbToHex.rgb(-1, 2222, 35));
    }
}
