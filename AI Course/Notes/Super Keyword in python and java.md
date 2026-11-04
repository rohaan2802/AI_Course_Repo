# Super Keyword in python and java

## The super Keyword in Python and Java

- What is super?
The super keyword is used in inheritance.
+ It allows a child class to access:
- The parent class constructor
- The parent class methods
- super in Python
In Python, super() is used to call methods or constructors from the parent class.
- Example 1: Calling Parent Constructor
- class Parent:
- def _init_(self， name):
- self.name = name
- print("Parent constructor called")
- class Child(Parent):
- def _init_(self, name, age):
- super()._init_(name) # Calling Parent constructor self.age = age
- print("child constructor called")
- ryuun
- c = Child("Ali"， 20)
P output:
- Explanation:
- super()._init_(name) calls the Parent class constructor Without super() , the parent constructor won't run automatically.
- Example 2: Calling Parent Method
- class Parent:
- def show(self):
- print("This is parent method")
- class Child(Parent):
- def show(self):
- super().show() # Calling parent method
- print("This is child method")
- Python
P output:
- Code
- <1)
- super in Java
In Java, super is used to:
- Call parent class constructor → super()
- Access parent class method -→ super.methodName()
- Access parent class variable -→ super.variableName
- Example 1: Calling Parent Constructor
- class Parent {
- Parent(String name) {
- System.out.println("Parent constructor called");
- class Child extends Parent (
- Child(String name, int age) (
- super(name); // Must be first line
- System.out.println("child constructor called");
- public class Main {
- public static void main(String[] args) {
- Child c = new Child("Ali", 20);
- Java
- Output:
- Code
- In Java, super() must be the first line in the child constructor.
- Example 2: Calling Parent Method
- class Parent {
- void show() {
- System.out.println("This is parent method");
- class Child extends Parent (
- void show(){
- super.show(); // Call parent method
- System.out.println("This is child method");
- public class Main
- public static void main(String[] args) {
- Child c = new Child();
- c. show();
- Java
- Key Differences: Python vs Java
Feature
Syntax super() super
Constructor call super()._init_() super()
Must be first line? Yes
Access variable super().var
- Simple Summary
- super means: "Go to my parent class"
- It is used in inheritance.
- It helps avoid rewriting code.
- It allows access to parent methods and constructors.
- super in multi-level inheritance
- super vs this
- Real-life example for better understanding

## Accessing Private Parent Members With super

Excellent question  This is where many students get confused.
Short answer:
No, you cannot access private constructor, method, or variable of a parent class using super
(in both Python and Java, but for different reasons).
- In Java
Java has strict access modifiers: private , protected , public , default.
1. Private Variable
- class Parent {
- private int x = 10;
- class Child extends Parent (
- void show() {
- Svstem nlit nrintln(slinen y): FRROR
- Java
- Error: x has private access in Parent
- private members are only accessible inside the same class.
Even super cannot access them.
2. Private Method
- class Parent {
- private void show() {
- System.out.println("Parent method");
- class Child extends Parent {
- void display(){
- super.show(); //
- Java
- Not allowed.
Private methods are not inherited.
3. Private Constructor
- class Parent {
- private Parent() {
- System.out.println("Parent constructor");
- class Child extends Parent (
- Child(）{
- super();
- Java
- Cannot access private constructor.
If parent constructor is private → child class cannot extend it normally
- When Can Java Child Access Parent Members?
Modifier
public
protected
default (same package)
private
- In Python
Python is different.
It does NOT have strict private like Java.
It has:
- _var → protected (by convention)
- _var → name-mangled (pseudo-private)
- Example with Double Underscore
- class Parent:
- def _init_(self):
- self._x = 10
- This will not work.
Why?
Because Python changes _x to:
- Code
This is called name mangling.
- Can we still access it?
(but not recommended):
- class Child(Parent):
But this is breaking encapsulation.
- Private Method in Python
- class Parent:
- def _show(self):
- print("Parent method")
- class Child(Parent):
- def display(self):
- super()._show()
Same reason: name mangling.
- Final Comparison
Feature Java Python
Strict private? Yes
Can child access private variable using
super ?
Can bypass? A Yes (using _className_var )
Privateconstructoraccessible?
- Simple Final Answer
- super CANNOT access private members in Java.
+ In Python, it also cannot directly access double-underscore members because of name mangling.
So in both languages:
Private means not accessible from child class - even with super .
- Why Java private methods are not inherited
- Why Python uses name mangling instead of true private
- Real-world use of private constructor (Singleton pattern)

## Using super()._Parent__x

Very sharp question
- Can we use super()._Parent_x ?
- Short Answer:
technically you can, but it is not recommended.
- Why This Works
In Python, when you write:
Python changes (mangles) the name internally to:
- Code
So it is not truly private  it is just renamed.
- Example Using super()._Parent_x
- class Parent:
- def _init_(self):
- self._x = 10
- class Child(Parent):
- def show(self):
- print(super()._Parent__x)
- c.show()
- Output:
- Code
- this works.
- But Why Is It Not Recommended?
Because:
1. _x is meant to be private
2. Accessing _Parent_x breaks encapsulation
3. If class name changes, it breaks
4. It makes code harder to maintain
So even though Python allows it, it's considered bad practice.
- Better Approach
- Protected (single underscore)
- class Parent:
- def _init_(self):
- self._x = 10#protected(convention)
- class Child(Parent):
- def show(self):
- print(super()._x)
- This is clean and acceptable.
- Important Concept
Python's _variable is:
- NOT truly private
- Just name-mangled to avoid accidental access
Python ="we trust you" private
- Final Answer
you can use:
But you should avoid doing it in real projects.
- Difference between _var and _var
- How name mangling works internally
- Why super() is rarely needed for variables in Python
- Is this conversation helpful so far?

