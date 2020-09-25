## Milestone 2 Update (09-24-2020)
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
|Dev Lead | Brandon | Review and approve code changes, manage source code repository, coordinate integration, determine tools, practices, architecture
 |
|QA Lead | Adrian | Design and review tests, ensure that code changes do not break existing functionality, enforce code consistency and style
 |
|Design Lead | Jack | Review and approve changes to language design (i.e. EBNF), communicate with research lead to ensure features are correctly implemented and changes are made in an organized way
 |
|Research Lead | Sofia | Coordinate user studies and determine new requirements/changes that should be added to design and implementation, prototype features to use for user-studies and to ensure feasibility
 |
 
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
