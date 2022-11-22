// Trying out datatypes in dart
// 1. Numbers
void main() {
int num = 7;
double num_2 = 5;
// Getting the variable type
// ....
print("$num is of type interger");
print("$num_2 is a double");

// 2. Strings
String name = "Denzel";
print("I am $name");

// 3. Lists
List cars = ["Benz", "BMW", "Dodge", "GTR"];
print("Check out my cars list meeehn!: $cars");
// Manipulating the list
cars.add("Jeep");
print("Oh, I bought another one, see the list now: $cars");
// 4. Maps -- these are the dictionaries in Python
Map fullname = {
  "firstname" : "Denzel",
  "middlename" : "Murathi",
  "surname" : "Gitonga"
};
print("My fullname is: $fullname");
// Accessing just the name
print("But most people use:");
print(fullname["firstname"]);
}
