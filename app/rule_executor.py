def execute_rule(rule, data):
    match(rule["operator"]):
        case "gte" | "nlt":
            return data[rule["field"]] >= rule["value"]
        case "lte" | "ngt":
            return data[rule["field"]] <= rule["value"]
        case "e":
            return data[rule["field"]] == rule["value"]
        case "gt" | "nlte":
            return data[rule["field"]] > rule["value"]
        case "lt" | "ngte":
            return data[rule["field"]] < rule["value"]
    pass