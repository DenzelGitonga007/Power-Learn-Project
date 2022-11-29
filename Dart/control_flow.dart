// 1. Create a program that takes in the age of a person. If the age is greater than or equal to 21,
//  print (“You are at least 21 years, drinks allowed”). Otherwise, print “You’re not 18 yet, go home!”
// The function to check the age
import 'dart:io';

void ageLimit(int age) {
  if (age >= 21) {
    print("You are at least 21 years, drinks allowed");
  } else {
    print("You're not 18 yet, go home!");
  }
}
// 2. Look at the following grading system of the PLP School of Technology:

// Create a program that takes in a learner’s score and outputs the grade.
int score = int.parse(stdin.readLineSync()!);
// The function to assign grade
grade(int score) {
  if (score >= 90) {
    return "A";
  } else if (score >= 80 && score >= 89) {
    return "B";
  } else if (score >= 70 && score > 79) {
    return "C";
  } else if (score >= 60 && score > 69) {
    return "D";
  } else if (score >= 50 && score > 59) {
    return "E";
  } else if (score < 50) {
    return "F";
  }
}

// The main function
void main() {
  // Call the functions
  ageLimit(20);
  print("Please enter your score: ");
  print(grade(score));
}
