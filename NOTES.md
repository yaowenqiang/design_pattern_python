# SOLID

Design Pattern Classification

+ Creational
  + Object creation
+ Structural
  + Object composition
+ Behavioral
  + Object communication and responsibility

## Single Responsibility Principle

A class should have one, and only one, reason to change.

## Open/Closed Principle

Software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification.

## Liskov Substitution Principle

Objects in a program should be replaceable with instances of their subtypes without altering the correctness of that program.

## Interface Segregation Principle

Clients should not be forced to depend on interfaces they do not use.

## Dependency Inversion Principle

High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces). Abstractions should not depend on details. Details should depend on abstractions.


## Python interface

PEP 3119

+ abc module
+ @abstractmethod
+ @abstractproperty
+ @abstractclassmethod
+ @abstractstaticmethod

The Abstract Factory Pattern

+ Classification: Creational
+ Close cousin of Factory pattern
+ Factory creates one product
+ Abstract Factory creates families of related products
+ Enforce dependencies between classes
+ Defers creation of objects to concrete subclasses

The Builder Pattern

+ Classification: Creational
+ Separate construction and representation
+ Allows for flexible object creation
+ Useful for complex objects with many parameters

The Factory Method Pattern

+ Classification: Creational
+ Factory Method is a method that returns an instance of a class
+ Factory Method is used to create an object
+ Factory Method is used to encapsulate the creation logic
+ Factory Method is used to create objects of different types
+ Factory Method is used to create objects of the same type

The Prototype Pattern

+ Classification: Creational
