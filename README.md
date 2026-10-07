# PLP Python Week 7 - Shopping List Manager

## File Descriptions
* `list_warmup.py`: Demonstrates basic list operations including index access, `.append()`, `.remove()`, and measuring length with `len()`.
* `shopping_list.py`: An interactive program allowing users to add, remove, show, and finish managing a shopping list safely.
* `list_report.py`: Displays a numbered list of items, counts names longer than 4 characters, and finds the longest item name using custom loop logic.

## Reflection Question
### Why is it safer to check `in` before calling `.remove()`?
It is safer to check membership with `in` before calling `.remove()` because attempting to remove an element that does not exist in a list raises a `ValueError` in Python, which would cause the program to crash. Verifying that the item exists first ensures smooth program execution and allows for user-friendly error messages without breaking runtime.
