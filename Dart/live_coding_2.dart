// 1. Write down a function to print out the value of adding 2 numbers.
void main() {
  int sumNum() {
    int num_1 = 10;
    int num_2 = 20;
    // int sum = num_1 + num_2;
    return num_1 + num_2;
  }

  // Call the function
  print(sumNum());

  // 2. Write down a function that prints out your name.
  String fullName(String name) {
    print("Hello $name");
    return name;
  }

  print(fullName("Denzel"));
  // 3. A function to calculate circumference of a circle.
  double circumference(double r) {
    // Declare the constant pie
    const pie = 3.14;
    return 2 * pie * r;
  }

  print(circumference(7));
  // 4. A function to print out a greeting in any language.
  
}
