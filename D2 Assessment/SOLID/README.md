## SOLID - Principles that Apply

- [Intro to `SOLID`](http://www.wikiwand.com/en/SOLID_(object-oriented_design))
    - `S`: Single Responsibility Principle.
        - ```The first principle of the SOLID stack is the Single Responsibility Principle. Following Martin's definition, the principle says: A class should have only one reason to change. The attribution of single responsibility leads to misunderstanding this principle. In fact it is often mistakenly taken to mean that a class should only do one thing. The definition of the principle, however, states that the only reason for which a class or object should be changed is because it has changed its responsibility. So, it is not true that an object can only do one thing, rather it can do more things that belong to the same responsibilities. In other words, the actions assigned to an object must be consistent with the unique responsibility that was given. If there are two different reasons why an object or class must be changed, then we have to separate the two responsibilities into as many objects or classes.```
            - [link](http://www.oodesign.com/single-responsibility-principle.html)
    - `O`: Open/Close Principle.
        - ```The second SOLID principle concerns the extensibility of components and is called the Open/Closed Principle. Its focus is on avoiding changes when we need to extend a component's feature. The principle states: Software entities like classes, modules and functions should be open for extension but closed for modifications.```
            - [link](http://joelabrahamsson.com/a-simple-example-of-the-openclosed-principle/)
    - `L`: Liskov Substitution Principle.
        - ```The third SOLID principle, the Liskov Substitute Principle, is somehow an extension of the Open/Closed Principle. In fact, it concerns the possibility of extending a component through inheritance and imposes a constraint that ensures interoperability of objects within an inheritance hierarchy. The principle says: Subtypes must be substitutable for their base types.```
            - [link](http://www.objectmentor.com/resources/articles/lsp.pdf)
            - [Stack Overflow](http://stackoverflow.com/questions/56860/what-is-the-liskov-substitution-principle)
            - [Circle-Ellipse Problem](https://en.wikipedia.org/wiki/Circle-ellipse_problem)
        - ```Moral of the story: model your classes based on behaviours not on properties; model your data based on properties and not on behaviours. If it behaves like a duck, it's certainly a bird.```
        - ```This strongly suggests that inheritance should never be used when the sub-class restricts the freedom implicit in the base class, but should only be used when the sub-class adds extra detail to the concept represented by the base class as in 'Monkey' is-an 'Animal'.```
    - `I`: Interface Segregation Principle
        - ```When designing the interface of an object, we should limit to define what is strictly necessary, avoiding carrying around stuff that is not used. This is, in a nutshell, the Interface Segregation Principle, whose official version says: Clients should not be forced to depend on methods they do not use.```
            - [link](http://www.oodesign.com/interface-segregation-principle.html)
            - [Wiki](https://en.wikipedia.org/wiki/Interface_segregation_principle)
    - `D`: Dependency Inversion Principle
        - ```The last SOLID principle concerns the dependence among the components of an application and states that: 1. High-level modules should not depend on low-level modules. Both should depend on abstractions. 2. Abstractions should not depend upon details. Details should depend on abstractions. ```
        - [link](http://www.oodesign.com/dependency-inversion-principle.html)
        - [Code Tutorials](http://code.tutsplus.com/tutorials/solid-part-4-the-dependency-inversion-principle--net-36872)
        - **Program to an interface, not an implementation.**

### Advantages of SOLID Principles
- Cleaner code.
- Code smells are kept away.
- Codebase that is maintainable and expandable.

## Running the Code

All the submodules are managed in the same way, which means you can run the code using the same syntax. For example, if you want to see the result of the sample code for Open/Close principle, just run:

```
python -m python_code.bad.open_close   # See the result of bad implementation
python -m python_code.good.open_close  # See the result of good implementation
```

Or, you can run `python -m python_code --list` or `python -m python_code -l` to see all the available submodules.
