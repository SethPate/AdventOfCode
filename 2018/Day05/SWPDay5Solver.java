import java.io.FileReader;
import java.io.BufferedReader;

class SWPDay5Solver {

public static void main(String[] args) {
  SWPDay5Solver solution = new SWPDay5Solver();
  solution.run();
}

/*
Calls and prints the answers to partA and partB.
*/
void run() {
  String polymer = parseInput("swpinput.txt");
//  polymer = "dabAcCaCBAcCcaDA";
  int partA = partA(polymer);
  System.out.println(String.format("part A is %d", partA));
  int partB = partB(polymer);
  System.out.println(String.format("part B is %d", partB));
}

/*
Takes a file location String,
and returns a String containing the file contents.
*/
String parseInput(String inputLocation) {
  String polymer = null;

  try {
    BufferedReader br = new BufferedReader(new FileReader(inputLocation));
    polymer = br.readLine();
  } catch (Exception e) {
    e.printStackTrace();
  }

  return polymer;
}

/*
Returns the length of a polymer after all
reactions have taken place.
*/
int partA(String polymer) {
  return react(polymer).length();
}

/*
Given a polymer,
Returns the length of the shortest polymer
that could be reacted if a single
type of character were removed from the polymer.
*/
int partB(String polymer) {
  int minLength = polymer.length();

  for (char c = 65; c < 91; c++) {
    Character C = new Character(c);
    String upper = C.toString();
    String lower = C.toString().toLowerCase();
    String polymerWithoutC = polymer.replace(upper,"");
    polymerWithoutC = polymerWithoutC.replace(lower,"");
    polymerWithoutC = react(polymerWithoutC);
    int lengthWithoutC = polymerWithoutC.length();
    if (lengthWithoutC < minLength) {
      minLength = lengthWithoutC;
    }
  }

  return minLength;
}

/*
Reacts and removes letters from a polymer
until the polymer is stable.
*/
String react(String polymer) {	
  String newPolymer = polymer; 

  int preLength = newPolymer.length();
    int postLength = -1;

  while (preLength != postLength) {
    preLength = newPolymer.length();
    newPolymer = reactHelper(newPolymer);
    postLength = newPolymer.length(); 
  }

  return newPolymer;
}

/*
Given a polymer,
removes the first reactive pair,
returns the resulting polymer.
*/
String reactHelper(String polymer) {
  String newPolymer = polymer;

  for (int i = 0; i < polymer.length() - 1; i++) {
    char j = polymer.charAt(i);
    char k = polymer.charAt(i + 1);
    if (Character.toLowerCase(j) == Character.toLowerCase(k)) {
      if (j != k) {
        // create new polymer without j,k
        String pre = polymer.substring(0,i);
	String post = polymer.substring(i + 2);
	newPolymer = pre.concat(post);
	return newPolymer;
      }
    }
  }
  return newPolymer;
}

}
