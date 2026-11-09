package main.java.jadencasingstrings;

import java.util.StringJoiner;

class JadenCase {

    public String toJadenCase(String phrase) {
        if (phrase == null || phrase.isEmpty()) {
            return null;
        }

        String[] words = phrase.split(" ");

        StringJoiner finalSentence = new StringJoiner(" ");
        for (String word : words) {
            StringBuilder capitalizedWord = new StringBuilder();
            String firstLetter = Character.toString(word.charAt(0)).toUpperCase();
            capitalizedWord.append(firstLetter);
            capitalizedWord.append(word.substring(1));
            finalSentence.add(capitalizedWord.toString());
        }

        return finalSentence.toString();
    }

}

public class Main {
    static void main(String[] args) {
        JadenCase jc = new JadenCase();
        System.out.println(jc.toJadenCase("most trees are blue"));
        System.out.println(jc.toJadenCase(""));
        System.out.println(jc.toJadenCase(null));
    }
}
