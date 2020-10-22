package hw3_actual;

import java.util.List;
import java.util.function.Function;
import java.util.function.BiFunction;
import java.util.function.Predicate;
import java.util.Comparator;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;
import java.util.function.BiFunction;
import org.junit.Assert;
import org.junit.Test;
import java.util.Iterator;
import java.util.Set;

import static hw3_actual.fp.*;
import static org.junit.Assert.assertTrue;

import junit.framework.TestCase;
import java.util.Iterator;
import java.util.Set;

import static org.junit.Assert.assertTrue;

import java.util.Collection; // might want to delete this
import java.util.HashSet;

public class fpTest {
	
	/**
	 * 	(1) Use map to implement the following behavior (described in Python).  i.e given a List T create a List Integer of the hashes of the objects.
		names = ['Mary', 'Isla', 'Sam']
		for i in range(len(names)):
		names[i] = hash(names[i])
	 */
	@Test
	public void mapTest() {
        List<String> listArray = Arrays.asList("Maria", "Donatello", "Chicago", "Race car");
        assertTrue(listArray.size() == 4);
        assertTrue(listArray.get(0) == "Maria");
        List<Integer> listHash = map(listArray, (String e) -> e.hashCode());
        assertTrue(listHash.get(0).hashCode() == 74113750);
        assertTrue(listHash.get(1).hashCode() == -740971008);
        assertTrue(listHash.get(2).hashCode() == -1884315574);
        assertTrue(listHash.get(3).hashCode() == -1316315);
	}
	
	/**
	 * (2) Use foldleft to calculate the sum of a list of integers.
		i.e write a method: int sum(List Integer l)
	 */
	@Test
	public void foldLeftTest() {
		List<Integer> listInt = new ArrayList<>();
		listInt.add(12);
		listInt.add(17);
		listInt.add(14);
        BiFunction<Integer, Integer, Integer> sumFunction = (a, b) -> {
            return a+b;
        };
        int sum = foldLeft(0, listInt, sumFunction);
        assertTrue(sum==43);

	}
	
	/**
	 * 		
		(3) Use foldRight to concatenate a list of strings i.e write a method
		 String s (List Strringer l)
	 */
	@Test
	public void foldRightTest() {
		List<String> stringList = new ArrayList<>();
		stringList.add("Zenith");
		stringList.add("Sunshine");
		stringList.add("Fluffy");
		stringList.add("Michael");
        assertTrue(stringList.size() == 4);
        BiFunction<String, String, String> combined = (a, b) -> {
            return a + b;
        };
        String finalString = foldRight("", stringList, combined);
        assertTrue(finalString.equals("MichaelFluffySunshineZenith"));
	}
	
	/**
	 *  (4) consider an array of Persons. Use filter to 
		print the names of the Persons whose salary is
		greater than 100000
	 */
	@Test
	public void filterTest() {
		List<Person> listArray = new ArrayList<Person>();
		listArray.add(new Person(40, "Danny boi"));
		listArray.add(new Person(1200, "Justin Frias"));
        assertTrue(listArray.size()==2);
        List<Person> filteredAns = (List<Person>) filter(listArray, (person) -> person.getSalary() > 1000);
        assertTrue(filteredAns.size()==1);
	}
	
	/**
	 * (5) Use minVal to calculate the minimum of a List of 
		 Integers
	 */
	@Test
	public void minValMinTest() {
		assertTrue(1==0);
	}
	
	/**     (6) Use minVal to calculate the maximum of a List of 
		Integers
	 * 
	 */
	@Test
	public void minValMaxTest() {
		assertTrue(1==0);
	}
	/**
	 * 	(7)  Use minPos to calculate the position of the
		minimum in  a List of  Integers
	 */
	@Test
	public void minPosMinIntegerTest() {
		 List<Integer> listInteger = Arrays.asList(1,2,3,4,5,0,6);
	     int result = minPos(listInteger);
	     assertTrue(result == 5);
	}
	/**
	 *  (8)  Use minPos to calculate the position of the
		minimum in  a List of  String
	 */
	@Test
	public void minPosMinStringTest() {
        List<String> listString = Arrays.asList("apple","mariachi","zebra");
        int result = minPos(listString);
        assertTrue(result == 0);
	}
	
}
