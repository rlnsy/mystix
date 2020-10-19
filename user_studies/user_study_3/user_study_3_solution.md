**Solution to Exercise:**

~~~
1  program:
2  // graph 1
3  source = remote("http://localhost:8000")
4  map(source) “date” to number date
5  map(source) “plant_height” to number height
6  plot xy(date, height) titled “My Little Plant”
7  // graph 2
8  source_2 = remote("http://localhost:8000")
9  map(source_2) “num_of_leaves” to number leaves
10 map(source_2) “plant_height” to number height
11 number doubled_leaves = leaves
12 observe(source_2) do doubled_leaves * 2
13 plot line_xy(height, doubled_leaves) titled “More Leaves”
14 start!
~~~
