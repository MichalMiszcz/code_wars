package main.java.stopspinningmywords;

class SpinWords {
    public String spinWords(String sentence) {
        String[] words = sentence.split(" ");

        StringBuilder finalSentence = new StringBuilder();
        int i = 0;
        for (String word : words) {
            if (i > 0) {
                finalSentence.append(" ");
            }

            if (word.length() >= 5) {
                StringBuilder newWord = new StringBuilder();
                for (char character : word.toCharArray()) {
                    newWord.insert(0, character);
                }
                finalSentence.append(newWord);
            }
            else {
                finalSentence.append(word);
            }

            i++;
        }

        return finalSentence.toString();
    }
}

public class Main {
    static void main(String[] args) {
        String reversed = new SpinWords().spinWords("Welcome home");
        System.out.println(reversed);
    }
}