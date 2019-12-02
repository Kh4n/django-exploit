import importlib
from pprint import pprint
import ast

def get_imports_from_file(file_name):
    with open(file_name, "r") as source:
        tree = ast.parse(source.read())

    analyzer = Analyzer()
    analyzer.visit(tree)
    imports = analyzer.report()

    ret = []
    for i in imports:
        print(i)
        try:
            a = importlib.util.find_spec(i)
            if a.origin:
                ret.append(a.origin)
        except Exception as e:
            print(e)
    return ret


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.import_list = []

    def visit_Import(self, node):
        for alias in node.names:
            # print("import", alias.name)
            self.import_list.append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            # print("from", node.module, "import", alias.name)
            if alias.name == '*':
                self.import_list.append(node.module)
            else:
                self.import_list.append(node.module + '.' + alias.name)
        self.generic_visit(node)

    def generic_visit(self, node):
        # print(type(node).__name__)
        # print(node._fields)
        return super().generic_visit(node)

    def report(self):
        return self.import_list


if __name__ == "__main__":
    print(get_imports_from_file("backdoor.py"))
    print(get_imports_from_file("defaults.py"))