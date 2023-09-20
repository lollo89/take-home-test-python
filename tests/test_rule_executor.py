import unittest

from rule_engine.rule_executor import execute_rule


class TestRuleExecutor(unittest.TestCase):
    def test_execute_gr_rule_true(self):
        rule = {
            "value": 50,
            "operator": "gt",
            "field": "score"
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 51
        }

        self.assertTrue(execute_rule(rule, data))

    def test_execute_gr_rule_false(self):
        rule = {
            "value": 50,
            "operator": "gt",
            "field": "score"
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 50
        }

        self.assertFalse(execute_rule(rule, data))

    def test_execute_gre_rule_true(self):
        rule = {
            "value": 50,
            "operator": "gt",
            "field": "score"
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 50
        }

        self.assertFalse(execute_rule(rule, data))

    def test_execute_gre_rule_false(self):
        rule = {
            "value": 50,
            "operator": "gt",
            "field": "score"
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 49
        }

        self.assertFalse(execute_rule(rule, data))

    def test_execute_and_rule_true(self):
        rule = {
            "operator": "AND",
            "left_operand": {
                "value": 70,
                "operator": "gt",
                "field": "credit_rating"
            },
            "right_operand": {
                "value": 40,
                "operator": "gt",
                "field": "score"
            }
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 50
        }

        self.assertTrue(execute_rule(rule, data))

    def test_execute_and_rule_false(self):
        rule = {
            "operator": "AND",
            "left_operand": {
                "value": 75,
                "operator": "gt",
                "field": "credit_rating"
            },
            "right_operand": {
                "value": 40,
                "operator": "gt",
                "field": "score"
            }
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 50
        }

        self.assertFalse(execute_rule(rule, data))

    def test_execute_or_rule_true(self):
        rule = {
            "operator": "OR",
            "left_operand": {
                "value": 80,
                "operator": "gt",
                "field": "credit_rating"
            },
            "right_operand": {
                "value": 50,
                "operator": "gte",
                "field": "score"
            }
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 50
        }

        self.assertTrue(execute_rule(rule, data))

    def test_execute_or_rule_false(self):
        rule = {
            "operator": "OR",
            "left_operand": {
                "value": 80,
                "operator": "gt",
                "field": "credit_rating"
            },
            "right_operand": {
                "value": 50,
                "operator": "gt",
                "field": "score"
            }
        }

        data = {
            "credit_rating": 75,
            "flood_risk": 5,
            "revenue": 1000,
            "score": 50
        }

        self.assertFalse(execute_rule(rule, data))
