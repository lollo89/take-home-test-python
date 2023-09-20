def parse_statement(statement): 
    statement_elements = statement.split(" ")
    elements_number = len(statement_elements)

    if len(statement_elements) >= 3:
        return {
            "field": statement_elements[0],
            "operator": extract_sign(statement_elements[1:elements_number-1]),
            "value": float(statement_elements[-1])
        }

def extract_sign(condition):
    match (condition[0]):
        case "is":
            return "" + extract_sign(condition[1::])
        case "not":
            return "n" + extract_sign(condition[1::])
        case _:
            return extract_operator(condition)

def extract_operator(condition): 
    length = len(condition)
    match(condition[0]):
        case "above" | "greater":
            return "gt" + extract_operator(condition[1::]) if length > 1 else "gt"
        case "below" | "less":
            return "lt" + extract_operator(condition[1::]) if length > 1 else "lt"
        case "equals":
            return "e"  + extract_operator(condition[1::]) if length > 1 else "e"
        case _:
            return extract_operator(condition[1::]) if length > 1 else ""

