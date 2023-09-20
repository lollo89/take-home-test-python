# Cytora - python take home test

## How to run

```bash
python3 index.py
```

## How to interact

It is possible to customize the rule executed or the data on which the rule will be executed by opening the `ìndex.py` file and customizing the variables `RULE` and/or `EXAMPLE_1`.

There are also few examples of rules with different complexity commented in the same file.

## Assumptions

During development, I operated under the assumption that rules are defined as ONE statement/operator per line. Therefore, if one wishes to create a complex rule with two parentheses, it would be written as shown below.

```python
RULE = """
(
    revenue is above 1000000
    AND
    flood_risk is above 4
)
OR
(
    revenue is below 1500
    AND
    flood_risk is below or equals 5
    AND
    credit_rating is above 50
)
"""
```
