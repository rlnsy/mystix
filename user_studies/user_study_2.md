# User Study Round 1
## Findings



**Key feedback received:**
- Improve documentation


## User Study Provided

Hello and welcome to our user study!

In this exercise, we will provide you with a brief description of the language functionalities and an example showing you a little bit of how it works. Your job will then complete the study question as best as you see fit. Please make sure to note any of your assumptions so we can better understand your interpretation of the language. *NOTE* At the end of the document, you will find our suggested solution to the problem.

And that’s it! Once you are finished with the study, we ask you please provide your feedback on your experience working with the language, anything you found confusing or unclear, and any suggestions you have for improving the experience. We would also love to hear about one or more ways in which you would see yourself using this software in your own projects!


**Language Features:**
- Data can be sourced from a URL
- Users can choose between live or static data updates
- Variables can be set to keep track of any changes and be used in graph creation
- Ability to apply mathematical operations on the data, such as:
    - Sum, difference, multiplication, division, powers	
    - Logarithms, trigonometric ratios
    - Group by other columns
    - Filter outliers or values 
- Flexibility of graph parameters - axis ranges, graph colours, etc
- Generate multiple types of graphs such as scatterplot, line, and bar graphs


**Documentation:**

To read data from a source: {data_name} = live(optional) remote {source_url} 
- the live keyword lets the function monitor the data source to update the graph whenever the source data changes
Variable assignment: {type} {var_name} = {val} 
Mapping data to variable: map({data_name}) {data_attribute} to {type} {val} 

*Note: that comments are not actually supported in the language at this point, but are included in the example code for informational purposes.*


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

With data from the height measurements of a plant (recorded daily), plot the visualization of the height over time as a scatter plot called ‘My Little Plant’. Make a second graph called “More Leaves” that takes a static shot of the plant’s growth relative to the number of leaves it has and increases the number of leaves by double. The source URL (not a real link) is www.mylittleplant.tech.io/data. You can assume that the data source has the following attributes:
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


**Solution to Exercise:**

~~~
1  program:
2  // graph 1
3  source = remote("www.mylittleplant.tech.io/data")
4  map(source) “date” to number date
5  map(source) “plant_height” to number height
6  plot xy(date, height) titled “My Little Plant”
7  // graph 2
8  source_2 = remote("www.mylittleplant.tech.io/data")
9  map(source_2) “num_of_leaves” to number leaves
10 map(source_2) “plant_height” to number height
11 number doubled_leaves = leaves
12 observe(source_2) do doubled_leaves * 2
13 plot line_xy(height, doubled_leaves) titled “More Leaves”
14 start!
~~~