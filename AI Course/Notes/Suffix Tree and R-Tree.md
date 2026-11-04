# Suffix Tree and R-Tree

## Suffix Tree and R-Tree in C++

1. Suffix Tree (Simple Explanation)
What is a Suffix?
A suffix is a substring that starts at some position and goes to the end.
Example string:
- BANANA
Suffixes:
- BANANA
- ANANA
- NANA
- ANA
- NA
What is a Suffix Tree?
A Suffix Tree is a compressed trie (tree) that stores all suffixes of a string.
It helps in very fast string searching
For example:
- Finding substring
- Pattern matching
- Longest repeated substring
Time complexity:
- Search: o(m)
where m = length of pattern.
Idea of Suffix Tree
For string:
- BANANA$
$ means end of string.
Tree structure roughly looks like:
- (root)
- BANANA$
- ANANA$
- NANA$
- ANA$
- NA$
- A$
Instead of storing whole strings, it stores edges representing substrings.
Simple Suffix Tree Implementation in C+ +
This is a basic version (not the optimal Ukkonen algorithm) just for understanding.
- #include <iostream>
- #include <map>
- using namespace std;
- class Node {
- public:
- map<char, Node*> children;
- class SuffixTree {
- private:
- Node* root;
- public:
- SuffixTree(){
- root = new Node();
- void insertSuffix(string s) (
- Node* current = root;
- for(char c : s) {
- if(current->children.count(c) == 0)
- current->children[c] = new Node();
- current = current->children[c];
- void buildTree(string text) (
- for(int i = ; i < text.length(); i++) {
- insertSuffix(text.substr(i));
- bool search(string pattern) (
- Node* current = root;
- for(char c : pattern) {
- if(current->children.count(c) == 0)
- return false;
- current = current->children[c];
- return true;
- int main(){
- SuffixTree tree;
- string text = "banana";
- tree.buildTree(text);
- if(tree.search("ana"))
- cout << "Pattern Found\n";
- else
- C++
Output
- Pattern Found
2. R-Tree (Simple Explanation)
What is R-Tree?
An R-Tree is a tree data structure used for spatial data
It is mainly used in:
- Maps
- GIS systems
- Game engines
- Location search
It stores rectangles / regions instead of numbers.
Example
Imagine storing locations of buildings on a map.
Each object is stored using a bounding rectangle:
- Building A -> (x1,y1,x2,y2)
Example:
- A: (1,1,3,3)
B: (5,5,7,7)
- C: (2,6,4,8)
R-Tree groups nearby rectangles together.
Example structure:
- Root
- Node1 Node2
- RectARectBRectC RectD
Each node stores a Minimum Bounding Rectangle (MBR) covering its children.
Simple R-Tree Example in C+ +
This is a very simplified conceptual version.
- #include <iostream>
- #include <vector>
- using namespace std;
- struct Rectangle {
- int x1, y1, x2, y2;
- bool overlap(Rectangle a, Rectangle b)
- return !(a.x2 < b.x1 Il a.x1 > b.x2 I
- a.y2 < b.y1 ll a.y1 > b.y2);
- class RTree {
- vector<Rectangle> objects;
- public:
- void insert(Rectangle r) (
- objects.push_back(r);
- void search(Rectangle query) {
- for(auto r : objects) (
- if(overlap(r, query)){
- cout << "Found overlapping rectangle:"
- cout << "(" << r.x1 << "," << r.yl << "
- << r.x2 << "," << r.y2 <<")/n";
- int main()(
- RTree tree;
- tree.insert({1,1,3,3));
- tree.insert({5,5,7,7));
- tree.insert((2,6,4,8));
- Rectangle query = {2,2,6,6};
- C++
Output
- Found overlapping rectangle: (1,1,3,3)
- Found overlapping rectangle: (5,5,7,7)
- Found overlapping rectangle: (2,6,4,8)
Difference Between Suffix Tree and R-Tree
Feature Suffix Tree
Data Type Strings Spatial objects
Used for Map / GIS search
Structure Bounding rectangle tree
Example Find objects in region
One-Line Memory Trick
Suffix Tree
- Fast searching inside strings
R-Tree
- Fast searching inside maps/geometry
- Suffix Tree diagram step-by-step (BANANA example)
- Real R-Tree insertion algorithm
- Interview-style explanation (2-3 marks answer).

## Spatial Data, GIS and the R-Tree

1. What is Spatial Data?
Spatial data = data that represents a location or position in space.
It usually uses coordinates (x, y) on a map.
Example
Imagine a map like this:
- (0,10) (10,10)
- City A
- (0,0)- (10,0)
City A might be located at:
- (4,6)
So the location (4,6) is spatial data.
Examples of Spatial Data
Object Spatial Data
House (x,y) position
Building
Road
Country polygon
Restaurant map coordinates
Example:
- Restaurant → (7,3)
- School → (2,8)
- Park → (4,4)
All of these are spatial data because they represent positions on a map.
2. What is GIS?
GIS = Geographic Information System
It is software that stores, analyzes, and displays spatial data.
Examples:
- Google Maps
- Uber maps
- Weather maps
- City planning systems
Example Tasks GIS Does
- Find all hospitals within 5km
- Find restaurants near me
- Show buildings in this area
- Track traffic locations
To do this quickly, GlS needs special data structures like R-Tree
3. Why R-Tree is Needed
Imagine a map database with 1 million buildings.
Now someone asks:
- Find buildings inside this area
Example search area:
- (2,2) → (6,6)
If we check every building, it will be very slow
So we use R-Tree to organize objects by location.
4. Basic Idea of R-Tree
R-Tree groups nearby objects into rectangles.
Example objects:
- Building A → (1,1)-(2,2)
- Building B → (2,1)-(3,2)
- Building C → (7,7)-(8,8)
- Building D → (8,7)-(9,8)
Instead of storing them randomly, R-Tree groups them.
Step 1  Create Groups
- Group 1:
- A and B
- Group 2:
- C and D
Step 2  Create Bounding Rectangles
Group 1 rectangle:
- (1,1) → (3,2)
Group 2 rectangle:
- (7,7) → (9,8)
Step 3  Build Tree
- ROOT
- Rect(1,1-3,2) Rect(7,7-9,8)
Each rectangle is called:
MBR = Minimum Bounding Rectangle
5. How Search Works in R-Tree
Suppose we search this area:
- (0,0) → (4,4)
Step 1  Check root rectangles
- Rect(1,1-3,2) → overlaps
- Rect(7,7-9,8) → no overlap
So we ignore the second branch.
Step 2  Check objects inside first rectangle
- Check A
- Check B
Search becomes much faster.
6. Real Life Example
When you search:
- Restaurants near me
The system must check millions of locations.
R-Tree helps by only checking nearby map regions.
Used in:
- Google Maps
- Uber
- Pokémon GO
- GPS navigation
- GIS software
7. Very Simple Visualization
Without R-Tree:
- Check every object
vviti r-iiee.
- ROOT
- Region2
- Region1
Search only the correct region.
8. Easy One-Line Definition
R-Tree
- A tree data structure used to organize spatial objects (rectangles/locations) so that searching in maps becomes fast.
9. Memory Trick
- B-Tree → numbers
- Trie → words
- R-Tree→maps/locations
- A super simple R-Tree diagram (best for exams)
- Step-by-step R-Tree insertion example
- 5-line exam definition for Data Structures paper
- How R-Tree is asked in university exams.

