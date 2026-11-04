# Percepts in Robots Explained

## Percepts in Robots

Percepts ka matlab hota hai wo information ya signals jo robot apne environment se receive karta hai.  
Simple words mein:  
- Percepts = jo robot “mehsoos” ya “dekh” ya “sun” kar samajhta hai.

#### Easy Example

Socho ek robot room mein khara hai.  
- Agar robot ke sensors ko pata chale ke room dark hai → yeh ek percept hai. Agar robot ko signal mile ke samne wall hai → yeh bhi percept hai.  
- Agar robot sun le ke koi awaaz aa rahi hai → yeh bhi percept hai.

#### Real Life Example (Vacuum Robot)

Ek robot vacuum cleaner:  
- Sensor batata hai: samne sofa hai → percept  
- Sensor batata hai: floor ganda hai → percept  
- Sensor batata hai: battery low hai → percept  
Phir robot in percepts ke basis par action leta hai:  
- Sofa hai → direction change  
- Floor ganda hai → cleaning start  
- Battery low hai → charging station par chala jata hai

#### Simple Formula

Sensors → Percepts → Decision → Action

#### Short Definition (Exam Style)

Percepts wo information hoti hai jo robot apne sensors ke zariye environment se receive karta hai, aur usi ke basis par robot apna action decide karta hai.  
diagrams ke saath bhi samjha sakta hoon.  
Percepts are the information or signals a robot receives from its environment.  
In very simple words:  
- Percepts = what the robot senses or notices.

#### Easy Example

Imagine a robot standing in a room.  
- If its sensor detects that the room is dark → this is a percept.  
- If it senses a wall in front → this is also a percept.  
- If it hears a sound → that is another percept.

#### Real-Life Example (Robot Vacuum)

A robot vacuum cleaner:  
- Sensor detects a sofa ahead → percept  
- Sensor detects dirty floor → percept  
- Sensor detects low battery → percept  
Based on these percepts, the robot takes actions:  
- Sofa ahead → change direction  
- Dirty floor → start cleaning  
- Low battery → go to charging station

#### Simple Flow

Sensors → Percepts → Decision → Action

#### Short Definition (Exam Style)

Percepts are the information a robot receives from its sensors about its  
environment, which it uses to decide what action to take. action, or give a simple diagram.
