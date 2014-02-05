import java.io.*;

public class Main {

public static void main (String[] args) {
    try {
        File file = new File(args[0]);
        BufferedReader in = new BufferedReader(new FileReader(file));
        String line;
        
        while ((line = in.readLine()) != null) {
            String[] linesOfFileArray = line.split("\\s");
            replaceFNWithRNEachLine(linesOfFileArray);
        }
    } catch (IOException e) {
        System.out.println("File Read Error: " + e.getMessage());
    }               
}

private static void replaceFNWithRNEachLine(String[] linesArray) {
    if (linesArray.length > 0) {
       for (int k = 0; k < linesArray.length; k++) {
        String[] splitLineArray = linesArray[k].split(";");
        String stringModifiee = splitLineArray[0];
        String[] valuesOfFNandRNArray = splitLineArray[1].split(",");
        stringModifiee = replaceFNWithPlaceholder(valuesOfFNandRNArray, stringModifiee);
        stringModifiee = replacePlaceholderWithRN(valuesOfFNandRNArray, stringModifiee);      
        System.out.println(stringModifiee);
       }
    }
}

private static String replaceFNWithPlaceholder(String[] valuesOfFNandRNArray, String stringModifiee) {
    for (int i = 0; i < (valuesOfFNandRNArray.length) / 2; i++){
        int regexIndex = 2 * i;
        String regex = valuesOfFNandRNArray[regexIndex];
        stringModifiee = stringModifiee.replaceAll(regex, createRegexPlaceholder(i));
    }
    return stringModifiee;
}

private static String replacePlaceholderWithRN(String[] valuesOfFNandRNArray, String stringModifiee) {
	for (int j = 0; j < (valuesOfFNandRNArray.length) / 2; j++){
        int replIndex = 2 * j + 1;
        String repl = valuesOfFNandRNArray[replIndex];
       	stringModifiee = stringModifiee.replaceAll(createRegexPlaceholder(j), repl);        
    }
    return stringModifiee;
}

private static String createRegexPlaceholder(int l) {
	String regexPlaceholder = "i" + Integer.toString(l) + "i";
	regexPlaceholder = regexPlaceholder.replaceAll(Integer.toString(0),"zero");
	regexPlaceholder = regexPlaceholder.replaceAll(Integer.toString(1),"one");
	return regexPlaceholder;
}

}
