package edu.depaul.triangle;

import java.util.Scanner;

/**
 * A class to classify a set of side lengths as one of the 3 types
 * of triangle: equilateral, isosceles, or scalene.
 * If classification is not possible it emits an error message
 */
public class Triangle {
	
	/**
	 * Define as private so that it is not a valid
	 * choice.
	 */
	private Triangle() {}
	
	public Triangle(String[] args) {
		//
		// TODO: keep this simple.  Constructors should not do a lot of work
		//
	}

	// TODO: Add methods to validate input, and classify the triangle (if possible) here
	
	private static String[] getArgs(Scanner s) {
		System.out.println("press Enter by itself to quit");
		System.out.println("enter 3 integers separated by space.");
		String args = s.nextLine();
		return args.split(" ");
	}
	
	public static void main(String[] a) {

		try (Scanner scanner = new Scanner(System.in)) {
			String[] args = getArgs(scanner);

			// Loop until the user enters an empty line
			while(args[0].length() !=0) {
				//
				// TODO: create a new Triangle here and call it
				//
				args = getArgs(scanner);
			}
			System.out.println("Done");
		}
	}
}
