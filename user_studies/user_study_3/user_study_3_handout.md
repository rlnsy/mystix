# Mystix User-Study

Hello and welcome to our user study!

In this exercise, we will provide you with a brief description of the language
 functionalities and an example showing you a little bit of how it works. Your job
  will then complete the study question as best as you see fit. Please make sure to
   note any of your assumptions so we can better understand your interpretation of
    the language. *NOTE*: Attached, you will find our suggested solution to the
     problem.

And that’s it! Once you are finished with the study, we ask you please provide your feedback on your experience working with the language, anything you found confusing or unclear, and any suggestions you have for improving the experience. We would also love to hear about one or more ways in which you would see yourself using this software in your own projects!


**Language Features and Documentation:**

Please read the attached [docs](documentation.md).

*Note: that comments are not actually supported in the language at this point, but are included in the example code for informational purposes.*

**Setup:**
1. If you haven't already, install the package:
```
pip3 install mystix
```
or upgrade to the latests version:
```
pip3 install mystix --upgrade
```
2. Verify version
```
python3 -m mystix -v
```
make sure you have the latest version (0.1.3)
3. Write a program. For example:
```
vim example.mstx
```
4. Run the program:
```
python3 -m mystix example.mstx
```
5. (Optional) Simulate a compatible data stream:
```
python3 -m mystix -s
```
This runs a custom Flask server on your machine at `localhost:8000` that interacts nicely with our data-loading backend.


**Code Snippet Example:**

~~~
/* Implementation for loading case age and date as series, and displays an age/date scatterplot where age is divided by 4 and a logarithmic graph of total cases over time. */
1 program:
2 source = remote("www.coviddata.com/stream") 
// a single record looks like this: { "case_age": 21, "case_date": 3 }
3 map(source) "case_date" to number date
4 number count = 0
5 number younger_age = age
6 observe(source) do count++, younger_age /= 4
7 plot xy(date, younger_age) titled age_graph //default plot type: scatter
8 plot line_xy(date, log(count)) titled cases_log
9 start!
~~~

**Example Exercise:**

With data from the height measurements of a plant (recorded daily), plot the
 visualization of the height over time as a scatter plot called ‘My Little Plant
 ’. Make a second graph called “More Leaves” that takes a static shot of the plant
 ’s growth relative to the number of leaves it has and increases the number of
  leaves by double. The source URL is http://localhost:8000 (the server you ran
   previously). You can assume that each record from the data
   source
   has the following attributes:
- date
- plant_height
- plant_leaves

~~~
/* TODO:
Create a solution for the exercise based on your understanding of the above language. There is no one correct answer, and we would like to see how you have interpreted the language. */

// Answer Here:

// Solution on the next page
~~~

Feedback: 
Please provide feedback on your experience using the new language and any thoughts on how we could improve it. Could you see yourself using this language in a real-world application?
