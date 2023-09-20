from rule_engine.statement_parser import parse_statement


def parse_rule(rule):
    statementList = rule.split("\n")
    statementList[:] = [x.strip() for x in statementList if x]

    operator_stack = []
    operand_stack = []
    for statement in statementList:
        if statement not in ['AND', 'OR', '(', ')']:
            operand_stack.append(parse_statement(statement))
        elif statement == 'OR' and len(operator_stack) > 0 and operator_stack[-1] == 'AND':
            right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
            operator = operator_stack.pop()
            operand_stack.append({
                "operator": operator,
                "right_operand": right_operand,
                "left_operand": left_operand
            })
            operator_stack.append(statement)
        elif statement == ')':
            while len(operator_stack) > 0 and operator_stack[-1] != '(':
                right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
                operator = operator_stack.pop()
                operand_stack.append({
                    "operator": operator,
                    "right_operand": right_operand,
                    "left_operand": left_operand
                })
            operator_stack.pop()
        else:
            operator_stack.append(statement)

    while len(operator_stack) > 0:
        right_operand, left_operand = operand_stack.pop(), operand_stack.pop()
        operator = operator_stack.pop()
        operand_stack.append({
            "operator": operator,
            "right_operand": right_operand,
            "left_operand": left_operand
        })

    return operand_stack.pop()
