# Assignment 2: Stack & Queue
Task Description: Complete the following tasks. 

***Also, write sample test cases to validate your implementation for each task.

## Task-1: 

Implement a stack data structure from scratch. You can’t use built-in Stack APIs. You can use the built-in Array or List or your custom-built LinkedList.  The Stack class must have the following functions. Write sample test cases to validate your implementation.

```java
class Stack { 

  push(element); // pushes element in the stack. 

  pop(); //removes the latest element from the stack and returns it. 

  peek(); //returns the latest element from the stack without removing it 

  size(); //returns the size of the stack. 

}
```

## Task-2: 
Given a string str that represents an arithmetic expression, evaluate the arithmetic expression.  The arithmetic expression can only include any arithmetic operators (i.e., +, -, /, *) and numeric operands, i.e., any positive or negative integer from  (-2^31) to (2^31-1).  There may be one or more white spaces between an operand and an operator. You should ignore the white spaces while scanning. For an invalid expression, i.e., any operand other than numeric values, invalid operator, or division by 0, either return NaN or throw an exception. You have to use the stack you implemented in Task-1 of the assignment. Write sample test cases to validate your implementation.

 

Input: str = "10 + 20 * 2"

Output: 50

Input: str = “foo / 30 + 7”

Output: NaN

## Task-3: 
Implement a Queue data structure from scratch. You cannot use built-in Queue APIs. You can use the built-in Array or List or your custom-built LinkedList.  The Queue class must have the following functions. Write sample test cases to validate your implementation.

```java
class Queue {

  enqueue(element); // enqueue element in the queue.

  dequeue();  // remove and return the earliest element from the queue. 

  poll(); //returns the earliest element without removing it. 

  size();  // returns the size of the queue.  

}
```

## Task-4: 
Implement a Stack using only two instances of your implemented Queue class (Task-3).  Write sample test cases to validate your implementation.

```java
class StackWithTwoQs{

  Queue queueOne; // your implemented Queue class

  Queue queueTwo; // your implemented Queue class

  // all stack methods 

  push(x); //pushes x in the stack. 

  pop();  //removes the latest element from the stack and returns it. 

  peek(); //returns the latest element from the stack without removing it 

  size(); //returns the size of the stack.

}
```

 

