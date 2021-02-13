Quick explanation of the RegEx used to check if a given string is a valid identifier.

```python
re.search(r"^(?=.{0,8}$)[A-Z][A-Z]*\d*$"
```

- ^$ | Mandates we match the entire string, not just subsets
- (?=.{0,8}$) | Lookahead expression that mandates length
- [A-Z][A-Z]*\d* | Mandates order and actual content 