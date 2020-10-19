## Features
- Data can be sourced from a URL
- Variables can be set to keep track of any changes and be used in graph creation
- Ability to apply mathematical operations on the data, such as:
  -  Aggregation and analysis functions using:
     - Sum, difference, multiplication, division, powers	
     - Logarithms, trigonometric ratios
- Generate multiple types of graphs such as scatterplot and line graphs



## Basic Definitions

### Variable
Any alphanumeric string and underscores(_) can be the name of a variable. Use variables to store data, calculations, counters, and so on. 

### Type
The type of the variable. One of:
- number
- category
- binary

### Value
Data that can be either:
- Numbers
- String
- Booleans

### Strings
```
"{YOUR_STRING}"
```
A string is text surrounded by quotations. 


### Axis
```
{VARIABLE | MATH_FUNCTION}
```
Either a variable or a math function.

### Math Functions
#### Simple Functions
```
{VARIABLE} {+=|-=|*=|/=|^=} {VALUE}
```
Updates the variable by performing the operator with the specified value.

#### Fast Functions
```
{VARIABLE}{++|--}
```
Increments or decrements the variable by 1.

#### Built-in Functions
```
{log|sin|cos|exp}({VARIABLE})
```
Performs the specified operation on the variable.

## Commands

### Load Data
```
{VARIABLE} = remote({URL})
```
Loads data from the specified URL. Only API endpoints thhat return an array called "data" are supported.

### Mapping
```
map({VARIABLE}) {DATA_ATTRIBUTE} to {TYPE} {VAR}
```

### Variable Assignment
```
{TYPE} {VARIABLE} = {VALUE}
```
Assigns a variable of the specified type the specified value.

### Trigger
```
observe({VARIABLE}) do {[MATH_FUNCTIONS, ...]}
```
Watches a variable and executes the specified function when the variable changes or updates. 

### Plotter 
```
plot {scatter_xy|line_xy}({AXIS}, {AXIS}) titled {STRING}
```
Plots either a scatterplot or line graph with the specified axes and title. 

## Program Structure

```
program:
{COMMAND}
...
{COMMAND}
start!
```
The basic structure of the program is to to start with `program:` then a new command on each line, ending with `start!`


### Quickstart
For example, let's load some data (sorry, it's not a real link) to get data related to the growth of a cute puppy, named Buster. We will plot Buster's weight over the course of a range of days with a scatter plot. To start, we need to start the program with 'program:', we need to load a data source. 
```
program:
test_source = remote("www.myawesomedogmeasurements.com/data")
```
From the data (we named it test_source), let's focus on the attributes that we care about, and map them to newly defined variables.

```
map(test_source) "buster_weight" to number weight
map(test_source) "day" to number day
```
Next we will plot the scatter plot of the data (named "My awesome pup") using the new variables that we defined, then end the program with 'start!'.
```
plot scatter_xy(date, weight) titled "My Awesome Pup"
start!
```

Putting it all together, we have:
```
program:
test_source = remote("www.myawesomedogmeasurements.com/data")
map(test_source) "buster_weight" to number weight
map(test_source) "day" to number day
plot scatter_xy(date, weight) titled "My Awesome Pup"
start!
```

