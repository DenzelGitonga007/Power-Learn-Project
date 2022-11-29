// Getting user input
// First import the dart Input/Output module
import 'dart:io';

void main() {
  // 1. For a general data type
  print("Type anything");
  var general_text = stdin.readLineSync();
  // Reading the text entered
  print("You entered $general_text");
  // 2. For a string
  print("What is your name");
  // Reading the name entered
  String? name = stdin.readLineSync();
  print("Hello $name");
  // 3. For an interger
  print("How old are you? In numbers only: ");
  int? age = int.parse(stdin.readLineSync()!);
  // The "?" and "!" are for null entry
  print("Congratulations, you are $age years old");
}
