package main.java.stop_spinning_my_words;

class SpinWords {
    public String spinWords(String sentence) {
        String[] words = sentence.split(" ");

        String final_sentence = "";
        int i = 0;
        for (String word : words) {
            if (i > 0) {
                final_sentence += " ";
            }

            if (word.length() >= 5) {
                StringBuilder new_word = new StringBuilder();
                for (char character : word.toCharArray()) {
                    new_word.insert(0, character);
                }
                final_sentence += new_word;
            }
            else {
                final_sentence += word;
            }

            i++;
        }

        return final_sentence;
    }
}

public class Main {
    static void main(String[] args) {
        String reversed = new SpinWords().spinWords("Welcome home");
        System.out.println(reversed);
    }
}