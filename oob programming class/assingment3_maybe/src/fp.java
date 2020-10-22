package hw3_actual;

import java.util.List;
import java.util.function.Function;
import java.util.function.BiFunction;
import java.util.function.Predicate;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;

public class fp {
	
	
/** 
 * 
 * @param <U> - generic parameter U
 * @param <V> - generic parameter V
 * @param l - iterable of generic type U
 * @param f - generic function f that takes generic parameter U and V
 * @return a linked list of type V
 */
static <U,V> List<V> map(Iterable<U> l, Function<U,V> f) {
	List<V> res = new LinkedList<V>();
	for (U a: l) {
		res.add(f.apply(a));
	}
	return res;
}

/**
 * 
 * @param <U> - generic parameter U
 * @param <V> - generic parameter V
 * @param e - variable e of type V
 * @param l - iterable variable l of type U
 * @param f - generic function f that takes 3 generic paramters (V,U,V)
 * @return - returns iterable 
 * from left to right, apply some function
 */
static <U,V> V foldLeft(V e, Iterable<U>l, BiFunction<V,U,V> f){
	for(U var: l){
		e = f.apply(e, var);
	}
	return e;
}


/**
 * 
 * @param <U> - generic parameter U
 * @param <V> - generic parameter V
 * @param e - variable e of type V
 * @param l - iterable variable l of type U
 * @param f - generic function f that takes 3 generic paramters (V,U,V)
 * @return returns iterable 
 * from right to left, apply some function
 */

static <U,V> V foldRight(V e, Iterable<U>l, BiFunction<U,V,V> f){
	for(U var: l){
		e = f.apply(var, e);
	}
	return e;
}

/**
 * 
 * @param <U>- generic parameter U
 * @param l - a iterable variable of type U
 * @param p - a predicate variable of type U
 * @return a linked list of type u 
 */

static <U> Iterable<U> filter(Iterable<U> l, Predicate<U> p){
	List<U> res = new LinkedList<U>();
	for (U a: l) {
		if (p.test(a)) {
			res.add(a);
		}
	}
	return res;
}
/**
 * 
 * @param <U>- generic parameter U
 * @param l - a iterable variable of type U
 * @param c - a comparator variable c of type U
 * @return
 */
static <U> U minVal(Iterable<U> l, Comparator<U> c){
	// write using fold.  No other loops permitted. 
	return null;
}

static <U extends Comparable<U>> int minPos(Iterable<U> l){
	// write using fold.  No other loops permitted. 
//	return foldLeft(0,l, 
//	        new BiFunction<Integer, U,Integer>(){
//	               int currIndex=0;
//	               U currMin = l.iterator().next();
//	               public Integer apply(Integer x, U a) {
//	               currIndex++;
//	               if (a.compareTo(currMin) < 0) {
//	                currMin =a;
//	                return currIndex;
//	               }  
//	               else return x;
//	               }});
	BiFunction<Integer, U, Integer> minPosBiFunc = (x, y)->{
		ArrayList<U> genArray = new ArrayList<>();
		l.forEach(genArray::add);
		if (genArray.get(x).compareTo(y) > 0){
			return genArray.indexOf(y);
		} 
		else if(genArray.get(x).compareTo(y) < 0){
			return x;
		} 
		else {
			return x;
		}
	};
	int result = foldLeft(0, l, minPosBiFunc);
	return result;
}

	public static void main(String[] args) {
		// (1) Use map to implement the following behavior (described in Python).  i.e given a List<T> create a List<Integer> of the hashes of the objects.
		// names = ['Mary', 'Isla', 'Sam']
		// for i in range(len(names)):
		       // names[i] = hash(names[i])
		
		// (2) Use foldleft to calculate the sum of a list of integers.
		// i.e write a method: int sum(List<Integer> l)
		
		// (3) Use foldRight to concatenate a list of strings i.e write a method
		// String s (List<String> l)
		
		// (4) consider an array of Persons. Use filter to 
		// print the names of the Persons whose salary is
		// greater than 100000
		
		// (5) Use minVal to calculate the minimum of a List of 
		//       Integers
		
        // (6) Use minVal to calculate the maximum of a List of 
		//       Integers
		
		// (7)  Use minPos to calculate the position of the
		// minimum in  a List of  Integers

		// (8)  Use minPos to calculate the position of the
		// minimum in  a List of  String

	}

}

class Person{
	final int salary;
	final String name;
	
	Person(int salary, String name){
		this.salary = salary;
		this.name = name;
	}
	
	int getSalary() { return salary; }
	String name() { return name;}
	
}