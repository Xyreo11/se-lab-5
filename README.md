# se-lab-5



### Issue Table

---

| Issue | Type | Line(s) | Description | Fix Approach |
|--------|------|----------|--------------|---------------|
| Missing module docstring | Style | 1 | No module-level docstring found | Add a descriptive module docstring at the top of the file |
| Unused import | Warning | 2 | `logging` imported but never used | Remove the unused import |
| Missing function docstrings | Style | 8, 14, 22, 25, 31, 36, 41, 48 | Functions lack descriptions | Add short docstrings explaining each function’s purpose |
| Non-snake_case function names | Style | 8, 14, 22, 25, 31, 36, 41 | Function names like `addItem`, `removeItem` don’t follow PEP8 | Rename functions to snake_case (e.g., `add_item`) |
| Mutable default argument | Bug | 8 | Default list `[]` used in parameter may be shared across calls | Change default to `None` and initialize inside the function |
| Bare `except` clause | Bug/Security | 19 | Catches all exceptions silently | Use specific exceptions (e.g., `except KeyError:`) or log errors |
| Try/Except/Pass detected | Security (Bandit B110) | 19 | Exception handling ignores errors entirely | Replace `pass` with proper handling or logging |
| Use of `eval()` | Security (Bandit B307) | 59 | `eval()` executes arbitrary code | Use `ast.literal_eval` or safer alternatives |
| Use of `open()` without encoding | Warning | 26, 32 | `open()` called without specifying encoding | Add `encoding='utf-8'` to `open()` calls |
| Global variable usage | Code Smell | 27 | Uses `global` statement | Refactor to pass data via parameters or class attributes |
| Missing blank lines | Formatting | 8, 14, 22, 25, 31, 36, 41, 48 | Function definitions missing required blank lines | Ensure 2 blank lines before top-level function definitions |
| Consider using `with` for file I/O | Best Practice | 26, 32 | Files not closed properly if exception occurs | Use `with open(...) as f:` for automatic resource cleanup |
| String formatting style | Improvement | 12 | Regular string formatting could use f-string | Replace with f-string for cleaner syntax |

---

### Reflections/Q&A

---

**1. Which issues were the easiest to fix, and which were the hardest? Why?**  
The easiest fixes were style issues like using f-strings and renaming functions. The hardest was handling the global variable and ensuring safe file operations without breaking the existing logic.

---

**2. Did the static analysis tools report any false positives? If so, describe one example.**  
Pylint’s warning about using the `global` keyword was a false positive — it was necessary to update shared data correctly in the program’s context.

---

**3. How would you integrate static analysis tools into your actual software development workflow? Consider continuous integration (CI) or local development practices.**  
I would use **pre-commit hooks** and **CI pipelines** (e.g., GitHub Actions) to automatically run `pylint`, `flake8`, and `bandit` on every commit or pull request, ensuring issues are caught early.

---

**4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?**  
The code became **cleaner, safer, and more maintainable**. Input checks and logging improved reliability, while removing `eval()` enhanced overall security.
