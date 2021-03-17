# +
import nbformat
import re

class assignment_rubric:
    def __init__(self, file):
        self.rubric_items = []
        self.question_points = {}
        self.subquestion_points = {}
        self.get_rubric_items(file)
        self.get_points()
        
    def get_rubric_items(self, file):
        nb = nbformat.read(file, as_version=nbformat.NO_CONVERT)
        nb.cells
        source = "\n".join([cell['source'] for cell in nb.cells if cell['cell_type'] == 'code' ])
        #print(source)
        pattern = r"### BEGIN GRADING(.*?)### END GRADING"
        rubric_strings = "".join(re.findall(re.compile(pattern, re.DOTALL),source))
        #print(rubric_strings)
        rubric_lines = [s for s in rubric_strings.splitlines() if s.strip() != '']

        self.rubric_items = []
        for l in rubric_lines:
            try:
                r = {}
                r['text'] = l.strip("# ").split(";")[0].rstrip()
                r['points'] = int(l.split(";")[1])
                self.rubric_items.append(r)
            except IndexError:
                print("Problem parsing this line:")
                print(l)
                raise IndexError
            
    def get_points(self):
        self.question_points = {}
        self.subquestion_points = {}
        for r in self.rubric_items:
            question = r['text'][0]
            subquestion = r['text'][0:2]
            if question in self.question_points.keys():
                self.question_points[question] += r['points']
            else:
                self.question_points[question] = r['points']
            if subquestion in self.subquestion_points.keys():
                self.subquestion_points[subquestion] += r['points']
            else:
                self.subquestion_points[subquestion] = r['points']
                
    def print_overview(self, print_rubric = False):
        total_points = 0
        for k1 in self.question_points.keys():
            print("Question %s: %d points" % (k1, self.question_points[k1]))
            total_points += self.question_points[k1]
            for k2 in [k for k in self.subquestion_points.keys() if k[0] == k1]:
                print("   - %s: %d points" % 
                      (k2, self.subquestion_points[k2]))
                if print_rubric:
                    for r in self.rubric_items:
                        if r['text'][0:2] == k2:
                            print("        *", r['text'], "(%d)" % r['points'])
            print()
        print("Total points:", total_points)
    
    def print_rubric(self):
        for r in self.rubric_items:
            print(r['text'])
            print(r['points'])
# -

# file = "Test notebook.ipynb"
# file = "../../course_material_2020_2021/Assignment 2/TN2513 Assignment 2.ipynb"
# a = assignment_rubric(file)
# a.print_rubric()
