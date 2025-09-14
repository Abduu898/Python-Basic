def arithmetic_arranger(problems, show_answers=False):
    first_line = []
    second_line = []
    dashes_line = []
    answers_line = []

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        parts = problem.split()
        operator = parts[1]

        if operator != '+' and operator != '-':
            return "Error: Operator must be '+' or '-'."

        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."

        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."

        num1 = parts[0]
        num2 = parts[2]
        width = max(len(num1), len(num2)) + 2

        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes_line.append('-' * width)

        if show_answers:
            if operator == '+':
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answers_line.append(answer.rjust(width))

    arranged = '    '.join(first_line) + '\n' + \
               '    '.join(second_line) + '\n' + \
               '    '.join(dashes_line)

    if show_answers:
        arranged += '\n' + '    '.join(answers_line)

    return arranged
