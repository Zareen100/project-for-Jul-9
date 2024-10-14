# Class to represent a mathematical expression
class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error in expression: {e}"

# Class to print the result
class ResultPrinter:
    def __init__(self, solver):
        self.solver = solver

    def print_result(self):
        result = self.solver.solve()
        print(f"The result of the expression '{self.solver.expression}' is: {result}")

# Main function to run the program
def main():
    # Taking a mathematical expression as input
    expression = input("Enter a mathematical expression to solve: ")

    # Creating objects of the classes
    solver = ExpressionSolver(expression)
    printer = ResultPrinter(solver)

    # Solving and printing the result
    printer.print_result()

# Run the program
if __name__ == "__main__":
    main()
