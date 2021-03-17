# Notebook Grading Rubric

A small package to process a [nbgrader](https://nbgrader.readthedocs.io/en/stable/)-style "grading rubric specification" syntax that I made for specifying grading rubrics inside of jupyter notebooks for education.

By embedding the specification of the rubric directly inside the solution code, I find it easier to keep a clear overview of my manually graded criteria. 

The library then provides code for:

* Parsing these out of the source notebooks
* Calculating point totals for a given question and for the full assignment
* Printing the detail rubric criteria for a quick overview of your assessement
* Printing the totals in a markdown-friendly format for cutting and pasting into your assignment
* Automatically deploying these to an assignment in Vocareum using my python [Vocareum API](https://github.com/gsteele13/vocareum-api) interface

## Description of syntax

The basic idea is to add a delimited section of commenets inside the `### BEGIN SOLUTION` / `### END SOLUTION` delimeters of nbgrader. The grading rubric should be delimited by `### BEGIN GRADING` and `### END GRADING`, with mulitple commented lines in between in which the grading rubric is specified. Each grading rubric line should have the following format:

```
# {identifier} {Text}; {points}
```

`{identifier}` should contain two digits specifiying the question / subquestion, and then more digits specifying the rubric number for that question. For example, `1a1` would be the first rubric item for question 1a, `2c3` would be the third for question 2c. For now, I believe I suppport only a max of 9 questions, but this would be easy to change. The question and subquestion number are parsed out by the code for producing the question / subquestion point summary total. 

`{Text}` is a descriptive text that explains to the teaching assistents how to evaluate this grading critereon. In current version of the code, it should not contain any semicolons.

`{points}` is a numerical value indicating how many points are assigned to that grading criterion.

## Example

For example, an "instructor" code cell of your source notebook might look like this:

```
t = np.linspace(0,10,100)
### BEGIN SOLUTION
g = 9.81 # m/s^2
x = 0.5*g*t**2

### BEGIN GRADING
# 1a1 Student correctly implemented formula; 1
### END GRADING
### END SOLUTION
```

Because the grading criteria delimiters are embedded inside `### BEGIN SOLUTION` / `### END SOLUTION`, they are automatically removed from the student version of the notebook. 

For more a more detailed example and example of how to use it, see the files in the repository.
