# User Study Round 1
## Findings
Our first user study consisted of had six participants, each with similar feedback. The user study we provided them did not have any official documantation and primarily consisted of a code example along with a list of some basic functionalities. This may have been a mistake as we wanted the user to infer how to proceed solely based off the example; however everyone said it was very confusing to complete the study without documentation. This was one of our biggest changes we would need to make moving forward.

Other feedback we were given was to encorporate syntax highlighting and change our literal "called" to "titled" for setting the title of graphs. Many were confused by the lack of highlighted function names and fixed literals. This may be due to the format in which we gave the participant the study, so we will be leaving this to a later feature to add.

Overall there was a unanimous response that the language would generally easy to comprehend once fully developed. The suggested modifications will be taken into account before our next user study. We will also be looking into potential error handling to improve the user’s debugging process.

**Key feedback received:**
- Highlight fixed literals
- *“Called” to “titled”*
- Declare multiple variables on same line
- Error handling
- *Unclear when data is being plotted and updated live or not*
- Chaining was unclear

## User Study Provided

**Language Functionalities:**
1. Options of actions that user can select from:
        - Notify in some form
        - Toast Message?
        - Email?
        - Text?
    - Change colour
    - Set between live or static data updating
    - Modify axis ranges
    - Apply math operations
    - Aggregation and analysis functions:
        - Sum, min, max, mean, median, mode	
        - Group by other column
        - Filter outliers or values 
    - Load data
2. Options of triggers that user can set to enact an action:
    - Define threshold value
    - Time limits/intervals
    - Define rate of change value

**Code Snippet Example:**

~~~
/* Implementation for loading case age and date as series, and displays an age/date scatterplot and a logarithmic graph of total cases over time. */

1 source = live remote "www.coviddata.com/stream" 
// a single record looks like this: { "case_age": 21, "case_date": 3 }
2 map source "case_date" to number date
3 number count = 0
4 on new data from source count++
5 plot xy date age called age_graph // default plot type: scatter
6 plot line xy(date, log(count)) called cases_log
~~~

**Example exercise**
Compute a moving average of case ages from the COVID data stream, and display it as a line graph over time, called “Average case age”.

~~~
/* TO DO -
Create a solution for the exercise based on your understanding of the above language. There is no one correct answer, and we would like to see how you have interpreted the language. */

// Answer Here:
~~~

Feedback: Please provide feedback on your experience using the new language and any thoughts on how we could improve it. Could you see yourself using this language in a real-world application? 

Answer Here: 


**Solution to exercise:**
~~~
1 source  = live remote "www.coviddata.com/stream" 
2 map source "case_date" to number date
3 map source "case_age" to number age
4 number count = 0
5 number total_age
6 number avg = 0
// option 1:
7 on new data from source count++, total_age += age, avg = total_age / count
// alternate option:
// on new data from source count++, total_age += age
// formula avg = total_age / count
8 plot line xy date avg called "Average case age"
~~~