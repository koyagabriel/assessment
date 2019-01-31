# Object Oriented Programming
### Expectation:
The Developer should have a very sound understanding of object relationships and be able to use this knowledge to design a complete system, taking into account the different possible users and interactions.

### Justification
For object-oriented programming, the design step is one of the most important phase in the process of developing software. For it is in the design step that we make the following decisions;
1. we decide how to divide the workings of our program into classes,
2. we decide how these classes will interact,
3. what data each will store, and 
4. what actions each will perform.

When designing a system, the rule of thumb I basically use in determining how to design my classes consist of the following:

**Responsibilities:** I divide the work into different actors, each with a different responsibility. I try to describe responsibilities using action verbs. These actors will form the classes for the program.

**Independence:** I define the work for each class to be as independent from other classes as possible. Each class has autonomy over some aspect of the program.

**Behaviors:** I define the behaviors for each class carefully and precisely, so that the consequences of each action performed by a class will be well un- derstood by other classes that interact with it. These behaviors are simply methods that this class defines.

The design process iterates through an action/actor cycle, where I first identify an action (that is, a responsibility), and then determine an actor
(that is, a component/class) that is best suited to perform that action. The design is complete when I have assigned all actions to actors. 

Some of the principles/concepts which I usually consider when design softwares in object-oriented programming are:

1. **Modularity:** Modularity refers to an organizing principle in which different components of a software system are divided into separate functional units. As a real-world analogy, a house or apartment can be viewed as consisting of several interacting units: electrical, heating and cooling, plumbing, and structural.
2. **Encapsulation:**  Encapsulation is a mechanism where you bind your data and code together as a single unit. It also means to hide your data in order to make it safe from any modification. Through encapsulation the methods and variables of a class are well hidden and safe.
3. **Abstraction:** It basically deals with hiding the details and showing the essential things to the user.
4. **Inheritance:** When one object acquires all the properties and behaviors of a parent object, it is known as inheritance. It provides code reusability.
5. **SOLID Principles:** https://github.com/koyagabriel/assessment/tree/master/D2%20Assessment/SOLID
