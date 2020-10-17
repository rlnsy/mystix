## Features
- Data can be sourced from a URL
- Users can choose between live or static data updates
- Variables can be set to keep track of any changes and be used in graph creation
- Ability to apply mathematical operations on the data, such as:
  -  Aggregation and analysis functions using:
     - Sum, difference, multiplication, division, powers	
     - Logarithms, trigonometric ratios
     - Group by other columns
- Filter outliers or values 
- Flexibility of graph parameters - axis ranges, graph colours, etc
- Generate multiple types of graphs such as scatterplot, line, and bar graphs



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
{log|sin|cos|exp} {VARIABLE}
```
Performs the specified operation on the variable.

## Functions

### Load Data
```
{VARIABLE} = {live|static} remote {URL}
```
Loads data either statically or live (streaming) from the specified URL.

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
plot {xy|line_xy}({AXIS}, {AXIS}) titled {STRING}
```
Plots either a scatterplot or line graph with the specified axes and title. 

## TODO:
- Quick Start Guide
- Example Code
