import ast

class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.functions = 0
        self.classes = 0
        self.conditionals = 0
        self.loops = 0
        self.assignments = 0

    def visit_FunctionDef(self, node):
        self.functions += 1
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        self.classes += 1
        self.generic_visit(node)

    def visit_If(self, node):
        self.conditionals += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.loops += 1
        self.generic_visit(node)

    def visit_While(self, node):
        self.loops += 1
        self.generic_visit(node)

    def visit_Assign(self, node):
        self.assignments += 1
        self.generic_visit(node)

    def report(self):
        return {
            "Functions": self.functions,
            "Classes": self.classes,
            "Conditionals (if)": self.conditionals,
            "Loops (for/while)": self.loops,
            "Assignments": self.assignments
        }

def analyze_code(source_code):
    tree = ast.parse(source_code)
    analyzer = CodeAnalyzer()
    analyzer.visit(tree)
    return analyzer.report()

if __name__ == "__main__":
    path = input("Enter path to Python file: ")
    with open(path, "r", encoding="utf-8") as f:
        code = f.read()
    results = analyze_code(code)
    print("Analysis Report:")
    for k, v in results.items():
        print(f"{k}: {v}")