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

## Functions

### Load Data
```
{VARIABLE} = {live|static} remote {URL}
```
Loads data either statically or live (streaming) from the specified URL.

### Mapping
```
map {VARIABLE} {DATA COLUMN NAME} to {TYPE} {VAR}
```
