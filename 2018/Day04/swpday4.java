import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Scanner;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Collections;

public class swpday4 {

public static void main(String[] argv){

	try {
		swpday4 obj = new swpday4();
		obj.run();
	} catch (Exception e) {
		e.printStackTrace();
	}
}

void run() {	
	ArrayList<String> inputStrs = null;

	try {
		inputStrs = this.getInputStrs();
	} catch (Exception e) {
		System.out.println(e.getMessage());
	}

//	Collections.sort(inputStrs);

	for (String str : inputStrs) {
//		System.out.println(str);
	}

	int partA = this.partA(inputStrs);
	int partB = this.partB(inputStrs);

	System.out.println(String.format("part A answer: %d", partA));

	System.out.println(String.format("part B answer: %d", partB));
}

/*
Takes an ArrayList<String> of formatted guard
watch IDs and sleeping times.
Finds the guard which sleeps most,
and returns their ID number multiplied by the
minute (0-59) they are most frequently asleep.
*/
int partA(ArrayList<String> inputStrs){
	HashMap<Integer, Guard> guardMap = this.getGuardMap(inputStrs);
	int maxAsleepTime = -1;
	int maxGuardID = -1;

	for (Guard g : guardMap.values()) {
		int asleepTime = g.getAsleepTime();
		if (g.getAsleepTime() > maxAsleepTime) {
			maxAsleepTime = g.getAsleepTime();
			maxGuardID = g.getID();
		}
	}
	
	int bestMinute = guardMap.get(maxGuardID).getBestMinute();

	int result = maxGuardID * bestMinute;

	return result;
}

int partB(ArrayList<String> inputStrs){
	HashMap<Integer,Guard> guardMap = this.getGuardMap(inputStrs);
	int highestCount = -1;
	int maxGuardID = -1;

	for (Map.Entry<Integer,Guard> entry : guardMap.entrySet()) {
		int count = entry.getValue().getHighestCount();
		if (count > highestCount) {
			highestCount = count;
			maxGuardID = entry.getKey();
			}
	}

	int result = maxGuardID * guardMap.get(maxGuardID).getHighestMinute();
	return result;
}

/*
A Guard Object represents a Guard, and can return
the total number of minutes spent asleep, 
and which minute the guard is most frequently asleep.
*/
class Guard {
	int ID;
	HashMap<Integer, Integer> minutesMap;
	
	Guard(int ID) {
		this.ID = ID;
		this.minutesMap = new HashMap<Integer, Integer>();
	}

	int getID() {
		int id = this.ID;
		return id;
	}

	void setCount(int minute) {
		if (this.minutesMap.containsKey(minute)) {
			int oldCount = this.minutesMap.get(minute);
			this.minutesMap.put(minute, oldCount + 1);
		} else {
			this.minutesMap.put(minute, 1);
		}
	}

	int getAsleepTime() {
		int total = 0;
		for (int time : this.minutesMap.values()) {
			total += time;
		}
		return total;
	}

	int getHighestCount() {
		int highestCount;
		if (this.minutesMap.values().size() > 0){
			highestCount =  Collections.max(this.minutesMap.values());
		} else {
			highestCount = 0;
		}
		return highestCount;	
	}

	int getHighestMinute() {
		int highestMinute = -1;
		int maxCount = -1;
		if (this.minutesMap.values().size() > 0) {
			for (Map.Entry<Integer,Integer> entry : this.minutesMap.entrySet()) {
				if (entry.getValue() > maxCount) {
					maxCount = entry.getValue();
					highestMinute = entry.getKey();
				}
			}
		} else {
			highestMinute = -1;
		}
		return highestMinute; 
	}

	int getBestMinute() {
		int bestMinuteCount = -1;
		int bestMinute = -1;

		// only 60 minutes
		for (int i = 0; i < 60; i++) {
			if (this.minutesMap.containsKey(i)) {
				if (this.minutesMap.get(i) > bestMinuteCount) {
	bestMinute = i;
	bestMinuteCount = this.minutesMap.get(i);
				}
			}
		}

		return bestMinute;
	}

}

/*
Given a list of input strings,
returns a HashMap<int, Guard>.
*/
HashMap<Integer, Guard> getGuardMap(ArrayList<String> inputStrs) {
	HashMap<Integer, Guard> guardMap = new HashMap<Integer, Guard>();

	int id = -1;
	int sleptAt = -1;

	Collections.sort(inputStrs);

	for (String s : inputStrs){
		String[] sArray = s.split("]");
		String date = sArray[0].trim();
		String[] dateArray = date.split(" ");
		String[] hoursAndMinutes = dateArray[1].split(":");
		int minute = Integer.parseInt(hoursAndMinutes[1]);
		String record = sArray[1].trim();
		if (record.substring(0,1).equals("G")) {
			String[] textArray = record.split(" ");
			id = Integer.parseInt(textArray[1].substring(1));
			if (!guardMap.containsKey(id)) {
				Guard newGuard = new Guard(id);
				guardMap.put(id, newGuard);
			}
		} else if (record.substring(0,1).equals("f")) {
			sleptAt = minute;
		} else if (record.substring(0,1).equals("w")) {
			for (int i = sleptAt; i < minute; i++) {
				guardMap.get(id).setCount(i);
			}
		}
	}

	return guardMap;
}

/*
Using the default input file location for this
project, returns an ArrayList<String> 
containing a String for each line in
the input file.
*/
ArrayList<String> getInputStrs(){
	ArrayList<String> inputStrList = new ArrayList<String>();
	String inputStr;
	BufferedReader br = null;

	try {
		br = new BufferedReader(new FileReader("./swpinput.txt"));
	} catch (IOException e) {
		System.out.println(e.getMessage());
	}

	try {
		while ((inputStr = br.readLine()) != null) {
			inputStrList.add(inputStr);	
		}
	} catch (IOException e) {
		System.out.println(e.getMessage());
	}

	return inputStrList; 
}
}
