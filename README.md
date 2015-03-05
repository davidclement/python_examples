# python_examples
short programs/scripts that illustrate python concepts, syntax, etc

## getattr/farm.py
shows a way to use a naming convention for functions, then build up strings that are the names of these functions based on input, then get find actual function if it exists programmatically using `getattr()`.  In this case the generic `grow()` function is called, `grow('apples')`, and then it looks for a `_grow_apples()` function and calls it if it exists
