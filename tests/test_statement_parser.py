import unittest

from rule_engine.statement_parser import parse_statement, extract_sign


class TestStatementParser(unittest.TestCase):
    def test_greater_condition(self):
        rule = 'credit_rating is above 50'
        result = parse_statement(rule)

        self.assertEqual('credit_rating', result['field'])
        self.assertEqual(50, result['value'])
        self.assertEqual('gt', result['operator'])

    def test_extract_sign(self):
        self.assertEqual("gt", extract_sign(["is", "above"]))
        self.assertEqual("lt", extract_sign(["is", "below"]))
        self.assertEqual("gte", extract_sign(["is", "above", "or", "equals"]))
        self.assertEqual("lte", extract_sign(["is", "below", "or", "equals"]))
        self.assertEqual("ngt", extract_sign(["not", "is", "above"]))
        self.assertEqual("ngt", extract_sign(["is", "not", "above"]))
        self.assertEqual("nlte", extract_sign(
            ["is", "not", "below", "or", "equals"]))


if __name__ == '__main__':
    unittest.main()
