# Developer Tools

### xargs
Builds and execute command lines from standard input. It converts input from standard input into arguments to a command.

```
>>> echo {1..9} | xargs -n1 echo "Hello"

Hello 1
Hello 2
Hello 3
Hello 4
Hello 5
Hello 6
Hello 7
Hello 8
Hello 9
```

### expr
expr is a command line Unix utility which evaluates an expression and outputs the corresponding value. It can be likened to ``eval`` in python.

```
>>> expr 1 + 2

3
```


### AWK
AWK is an interpreted programming language. It is very powerful and specially designed for text processing. 

Example: lets onsider a text file marks.txt to be processed with the following content
```
1) Amit     Physics   80
2) Rahul    Maths     90
3) Shyam    Biology   87
4) Kedar    English   85
5) Hari     History   89
```

This command prints the third column which contains the subject name and the fourth column which contains the marks obtained in a particular subject.
```
>>>  awk '{print $3 "\t" $4}' marks.txt
```

**output**
```
Physics   80
Maths     90
Biology   87
English   85
History   89
```


### sed
sed is a stream editor. A stream editor is used to perform basic text transformations on an input stream (a file or input from a pipeline).

For example, to replace all occurrences of ‘hello’ to ‘world’ in the file input.txt:

```
>>> sed 's/hello/world/' input.txt > output.txt
```