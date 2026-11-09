package main.java.morsecode;

public class MorseCodeDecoder {
    public static String decode(String morseCode) {
        morseCode = morseCode.trim();
        String[] morseWords = morseCode.split("   ");
        String[] words = new String[morseWords.length];

        for (int i = 0; i < morseWords.length; i++) {
            String[] morseCharacters = morseWords[i].split(" ");
            StringBuilder sb = new StringBuilder();
            for (String character : morseCharacters) {
                sb.append(MorseCode.get(character));
            }

            words[i] = sb.toString();
        }

        return String.join(" ", words);
    }
}