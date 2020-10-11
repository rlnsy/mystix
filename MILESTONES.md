## Milestone 4 Update (10-09-2020)
### Status of Implementation
As of today, we have implemented several code components of our language
system, including
1. An AST data structure
2. Stubs for most main functions
3. A system for variables and memory.
3. Utilities and test cases for many core modules.

In addition, we have a rigorous automated testing system in place for our code-base
and are on track to completely define our system spec using tests by the start of next
week.

### Plans for Last User Study
We have several participants lined up, some of which did not complete the first
 user study, to help us with the final study. We plan on completing our final study
  at the end of next week, once all of our system is implemented and mostly free
  of bugs. For the final study, however, we plan on making the following improvements:
  
  1. We will attend a live call with the participant to examine how they interact
   with the language and provide guidance where necessary.
  2. We will develop some more complex use cases and problems to solve with our
   language.
   3. We will present code examples with some level of syntax highlighting in order
   to make things slightly easier to discern for the user.
   
### Remaining Timeline
(See Roadmap below) We plan on specifying full tests of the system by the start of
 next week and be halfway done the implementation. By the end of the week we will
  be done with our MVP implementation in order to perform the user-study. We
   will prioritize dynamic functionality, quality, and overall usability of the
    language over additional features.

## Milestone 3 Update (10-02-2020)
### First Language Grammar Mockup
The following EBNF describes our initial language grammar as used for
our first user study. This design leaves many things to be desired but is
included for consistency and to accurately formalize the syntax given to our
first user-study participants.
```
PROGRAM ::= LINE*
LINE ::= LINE_CONTENT “\n”
LINE_CONTENT ::= COMMENT | STATEMENT
COMMENT ::= //[^\\n]+|/*.*/*
STATEMENT ::= ASSIGNMENT | MAP | RULE | PLOT COMMENT*
ASSIGNMENT ::= SOURCE_ASSIGNMENT | NUMBER_ASSIGNMENT
SOURCE_ASSIGNMENT ::= SOURCE_NAME = SOURCE_TYPE SOURCE_URL
SOURCE_NAME ::= [a-z]+
SOURCE_TYPE ::= live remote
SOURCE_URL ::= “.+”
NUMBER_ASSIGNMENT ::= number NUMBER_NAME = NUMBER
NUMBER_NAME ::= [a-z]+
NUMBER ::= [0-9]+
MAP ::= map SOURCE_NAME FIELD_NAME to MAP_REF
MAP_REF ::= number NUMBER_NAME
FIELD_NAME = “.+”
RULE ::= on new data from SOURCE_NAME NUMBER_OPS
NUMBER_OPS ::= ε | NUMBER_OP “,” NUMBER_OPS
NUMBER_OP ::= NUMBER_NAME++
PLOT ::= plot PLOT_TYPE VAL VAL called PLOT_NAME
PLOT_TYPE ::= xy | line xy
VAL ::= NUMBER | FUNC(NUMBER)
PLOT_NAME ::= [a-z]+
FUNC ::= log
```
Example program:
```
/* Implementation for loading case age and date as series, and displays 
    an age/date scatterplot and a logarithmic graph of total cases 
    over time. 
*/
1 source = live remote "www.coviddata.com/stream" 
// a single record looks like this: { "case_age": 21, "case_date": 3 }
2 map source "case_date" to number date
3 number count = 0
4 on new data from source count++
5 plot xy date age called age_graph // default plot type: scatter
6 plot line xy date log(count) called cases_log
```

### First User Study
1. Summary and notes:
Our first user study had six participants with similar views. Many were confused by the lack of highlighted function names and fixed literals; however, overall it was unanimous that the easy language like syntax would be easy to use and follow once fully developed. Changes suggested by participants included improving readability by adding highlighting, changing the “called” functionality to “titled”, and error handling. These modifications will be taken into account for the final design of the language to satisfy the design principle regarding code consistency for new users to easily understand how to use the language. We will also be looking into potential error handling to improve the user’s potential debugging process.
2. Key feedback received:
    - **Highlight fixed literals**
    - “Called” to “titled”
    - Declare multiple variables on same line
    - Error handling
    - **Unclear when data is being plotted and updated live or not**
    - Chaining was unclear
    
### Improved Language Design:
We made several changes to generalize the grammar and allow for more features in
 our language:
 
 1. Added clear start and end tokens to help users frame the structure of the
  program.
 2. Added new terminology to make it more evident when things are dynamic vs static.
 3. Added an array of new keywords corresponding to different types of data objects
  etc.
 4. Elaborated the structure of math and variable syntax.
 5. Removed comments since they seem hard to parse and are not that useful.
 
 Things we might add going forward:
 
 1. Stricter checking for strings at parsing.
 2. A more visually pleasing syntax for modelling control flow.
 3. Custom functions/routines that can be applied
 4. More static type declarations.
 5. Add a more elegant, non-comment way to insert documentation into the program.
 
 The latest version of our grammar can be found [here](grammar.txt).

## Milestone 2 Update (09-25-2020)
### Summary of Progress So Far:
As of today, we have completed both milestone 1 and 2. The user study has been created
 and is currently underway. The team will be meeting early next week to finalize
  the language grammar, which has been discussed at a high-level at this point
  ; more depth and details are yet to come. The assigned “Project Manager” will
   ensure the team stays on schedule (See "Responsibilities").

### Project Roadmap
A schedule for key targets our group will reach

| Date | Description |
| :--- | :---------- |
| Sat, Sep. 26, 2020 | A concrete list of features, visualization types etc. |
Mon, Sep. 28, 2020 | Concrete language design for user-study 1
Tue, Sep. 29, 2020 | Working prototypes of each feature
Wed, Sep. 30, 2020 | User-study 1
Thurs, Oct. 1, 2020 | Modified language design following user-study 1
Fri, Oct. 2, 2020 | Milestone 3
| Mon, Oct. 5, 2020 | Coded specification of shared data-structures e.g. Tokenized, AST and module specification. |
| Thurs, Oct. 8, 2020 | Unit and Integration tests for each module
Fri, Oct. 9, 2020 | Milestone 4
Wed, Oct. 14, 2020 | Implementation complete; all tests passing
Fri, Oct. 16, 2020 | Final User-study
Sun, Oct. 18, 2020 | Project Video
Mon, Oct. 19, 2020 | Final Deliverable

### Responsibilities
Here we describe the high-level roles each team member will have throughout the
 project
 
| Role | Group Member | Responsibilities |
| ---- | ------------ | :--------------- |
|Project Manager | Rowan | Review and submit assignments, manage deadlines |
|Dev Lead | Brandon | Review and approve code changes, manage source code repository, coordinate integration, determine tools, practices, architecture |
|QA Lead | Adrian | Design and review tests, ensure that code changes do not break existing functionality, enforce code consistency and style |
|Design Lead | Jack | Review and approve changes to language design (i.e. EBNF), communicate with research lead to ensure features are correctly implemented and changes are made in an organized way |
|Research Lead | Sofia | Coordinate user studies and determine new requirements/changes that should be added to design and implementation, prototype features to use for user-studies and to ensure feasibility |
 
 In addition to the above, we plan to assign smaller tasks during the implementation phase, particularly relating to the development of core modules such as
 - Tokenizer
 - Parser
 - Evaluator
 - Validator
 
 Other tasks will include the integration of modules, testing of modules, and
  fixing of reported bugs. The above tasks will be assigned at a later date when the precise requirements and work schedules of our individual members are better understood.

## Milestone 1 Update (09-18-2020)
### Use Case
An individual working on a research report or informative website who wants to display and work with static or live data

### Description
The data visualization DSL will allow a user to display their data in different customizable graphs and visualizations. Data taken from external sources will be mapped to a database, where the data can then be plotted on to a variety of graphs. Once graphs are determined, they may be updated in real time,  specified intervals, or remain static. Math operations and visual aspects such as colour schemes and layout may be applied as well, for added customization.

### Time Management
A significant portion of the work would revolve allowing graphs to be updated dynamically. The remainder of the project would be spent completing smaller user stories which would allow the DSL to become increasingly customizable to the user.

### Notes from TA Discussion
We presented an original idea to our TA which was quite ambitious and not well defined in the core-functionality. He thought this would be an interesting project, but mentioned we should be weary of scope creep. To avoid this, we decided to narrow down to a few core features (see roadmap and code example below)

### Additional Features
Stretch goals would include implementing an alert feature which would send out an alert or a notification once a certain data point/level is reached (ex. A desired stock price is reached and the user is notified).

### Tools to be used
Python, numpy, PyQtGraph/dc.js, HTTP client and/or filesystem library

### Tentative Roadmap
- MVP:
	1. Design
		- basic syntax/grammar. Features:
			1. set up a remote data source (i.e. url)
			2. Plot a basic scatter plot using live data from stream
			3. Create variables that store updated values
			4. Functions (e.g. log) to modify series
		- Map example programs to expected output and implement prototypes of these in Python/ core libraries
		- Perform first user study to get feedback on language features
		- Design program architecture
	2. (Optional) Prototyping:
		- Create working data streamer
		- Create working tokenizer/parser
		- Create example visualizations programmatically
	3. Implementation
		1. Delegate responsibility for program modules e.g. tokenizer, parser, evaluator, graph builder, data streamer
		2. Specify program behavior through tests for each module
		3. Implement core MVP features
- Stretch Goals:
	- Native alerts (app or browser) upon events
 	- Extensive plot design
	- Plot inference based on input data
	- Advanced schema definition

### Example
```c
// Program: Fetches COVID-19 data from an external source and generates dynamic
// visualizations as a browser-based

// opens a live data stream from a remote url (change live to fixed for a fixed dataset):
source  = live remote “www.coviddata.com/stream” 
refresh source every 60 minutes // default setting is 5 min
// whenever we receive a new record, map these column values to program variables
map source “case_age” to number age 
map source “case_date” to number date
// creates graph with data on x-axis and age on y-axis:
plot xy date age called age_graph
// creates histogram with age in bins of 10 years (0-10,11-20,...):
plot histogram age with range 10 called age_hist
variable count = 0 // create a numerical variable called count
on new data from source count++ // updates count whenever data is received
// a log graph of total cases, will update when count is updated:
plot xy date log(count) called cases_log
// specify layout - default: stacked:
display (age_graph left of age_hist) on top of cases_log
// colours bins in hues of blue - default grays
format age_histogram.bins blue color scheme
```
