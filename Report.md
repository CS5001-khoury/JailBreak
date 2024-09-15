# Report

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended youthe python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)


1. Correct the following loop.
   ```python
   value = None
   while value == "quit":
       value = input("Enter a value or quit: ")
       print(value)
   ```
    ```python
    ## put your corrected code below this line

    ```

2. The above code uses a None value to initialize the input variable. This works because python can let a variable be multiple types, but in some languages, you would have to match the type. Assuming you had to match the type (str), what would be a good default input value, that could never cause the loop to not run at least once? Provide reasoning for your logic as there are multiple correct answers. With that said, there is one that is more 'standard' than the rest, so feel free to openly discuss options that come to mind (you do not have to come up with the standard answer, but try to!). 
   

3. Write a small loop that will keep repeating until someone 
   enters a number greater than 0, and less than 5. It has to be
   whole numbers (hint: look up .isnumeric() from the team activity).

   ```python
   ## put your code here
   ```

4. Draw a flow diagram for your solution to #3

5. Looking back at homework #2, we actually had a type of 'loop' in the provided code (look near the main function). First copy the bit of code that causes the loop.
    ```python
    # code here
    ```
    Now: what would be some of the pros and cons of looping in such a way (think about 'frames' you see in the python visualizer)?

6. Thinking about edge cases, it is very common to get an off-by-one (OB1) error with loops. 
   Create two test cases (just as examples/inputs) for the following code. They 
   should both be 'correct' cases, but one of them should uncover the error in the code.

   ```python
    def count_backwards(value: int) -> None:
        """ Counts from value to 0, printing even values until 10 (including 10), and 
        then odd values."""
       counter = value
       while counter >= 0:
          if counter > 10:
            if counter % 2 == 0:
                print(counter)
          else:
            if counter % 2 == 1:
                print(counter)
          counter -= 1
   ```
   * Example test one:
   * Example test two:

 7. When thinking of these edge cases and OB1 errors, it is common to say one should test
    every condition plus-minus 1. In your opinion, is this beneficial? Why or why not?


## Deeper Thinking

Reflection is a powerful tool that has been **repeatedly** documented to help computer scientists learn languages, concepts, and improve their problem solving skills. There is even research that shows CS majors who spend time reflecting often do better at technical interviews, and long term studies show those reflective students also tend to get higher paying jobs over time. It is also a great way to help you learn how to learn.

Take a moment to reflect on the design of jailbreak.py (just the one file). Was it
a design you would have come up with given the problem? Did breaking concepts up into
functions help as compared to one loop? Also take a moment to reflect on your development process in general. What are topics you need to work on? What are some topics you really enjoy?  You should write a paragraph reflection using *PROSE* (don't bullet point). We often return reflections that are bullet points, and there is a reason you should use prose as it forces you to consolidate and solidify your thoughts. 
