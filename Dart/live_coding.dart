void main() {
  // 1. Write a dart program that outputs your name,nationality and your hobby.
  String name = "Denzel";
  String nationality = "Kenyan";
  String hobby = "memes";
  // Printing them individually
  // print(name + nationality + hobby);
  print(name);
  print(nationality);
  print(hobby);
  // 2. Put the name,nationality and hobby above in variables and output in one line.
  print("I am $name, from $nationality, and I like watching $hobby");
  // 3. Perform string interpolation.
  String text = "Powerlearnproject";
  print("The name '$text' has ${text.length} characters");
  // 4. Show the index of a specific letter in a string
  String index_test = "Murife";
  // var index = index_test.indexOf("e");
  print("The letter 'e' is at position ${index_test.indexOf("e")}");
  // 5. Create a list of 5 capital cities in Africa
  List capital_cities = ["Nairobi", "Accra", "Lagos", "Cape Town", "Kampala", "Dar-el-salaam"];
  print("The capital cities are: $capital_cities");
  // 6. Add two capital cities to the list created.
  capital_cities.add("Kakuma");
  capital_cities.add("Mogadishu");
  print("After independence, the cities are: $capital_cities");
  // Adding multiple values
  capital_cities.addAll(["Daadab", "Eritrea"]);
  print("Too many now, haha: $capital_cities");
  // 5. Create a map
  Map schools = {
    "Univeristy" : "KAFU",
    "High school" : "Kamiti",
    "Primary school" : "Green Angels Academy"
  };
  print("The schools I have attended are: $schools");
  // Adding another element
  schools["Sunday school"] = "Sanctuary of Love";
  print("Now completed: $schools");
  schools.addAll({
    "Driving school" : "Petanns",
    "Therapy" : "Tao",
    "Online sessions" : ["Coursera", "PLP", "eMobilis", "Microsoft", "Google"],
  });
  print("More schools: $schools");
  print("The online sessions, I've done: ${schools['Online sessions'][2]}");
}
