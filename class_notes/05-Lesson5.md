# Lesson 5 (week 5) for PYTHON210B, Autumn 2018 (October 31, 2018)

## Topics

### Logistics

* Attendance check (TA)
* Lightning talks after the first break
* Office hours
  * Instructor: Tuesday 7:30-9pm online only through [Zoom](https://washington.zoom.us/my/python2018)
  * TA: Optional or TBA
* Instructor out of town on 11/7/2018
  * Class will be held using [Zoom](https://washington.zoom.us/my/python2018)
  * In person classroom attendance is still possible/encouraged. TA will be present for anyone who'll attend in person.
    * **Poll:** Who will attend in person?
* Time to do some checkpointing on overall grades
  * Note that 80% or higher weighted total percentage score is required to pass this course, in addition to 80% or higher attendance.
  * We'll need to think about how to handle retried/improved submissions.
* Due dates for week 5
  * Lesson 5 Exercises by 11:59pm, Tuesday, Nov. 6, 2018 (5 points, Canvas submission of your source files required, one single PR for all the week 4 submissions should include source files for this assignment as well)
    * Exceptions and modules exercises: https://canvas.uw.edu/courses/1231462/modules/items/8759008
  * Lesson 5 Assignments by 11:59pm, Tuesday, Oct. 23, 2018 (15 points each, Canvas submission of your source files required, one single PR for all the week 4 submissions should include source files for this assignment as well)
    * Mailroom, Part 3: https://canvas.uw.edu/courses/1231462/modules/items/8759009
  * No-submission/grade labs that are not mentioned:
    * [Exception lab](https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/exceptions_lab.html)
    * [Comprehension lab](https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/comprehensions_lab.html)

### Modules and Packages

* https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Modules.html
* Do `git pull upstream master` and browse source files in the `examples/modules_and_packages` directory
* Understand diferences between:
  * A module and a package
  * `import abc` and `from abc import xyz`
  * `from abc import *` strongly discouraged
  * `__init__.py` for package initialization
    * Python 2 requires `__init__.py` even if it's empty. Python 3 doesn't.
    * Can import children modules from within `__init__.py`.
* In PYTHON210, we may not need to create our own modules/packages.
  * Our source code size is not that big -- Mostly nicely fitting in a single source file (for each exercise/assignment).
  * Still encouraged to modularize any software project using modules/packages
  * See how standard library modules/packages are referenced
    * In VSCode, right-click on any imported module/package and click `Go to Definition`. On the opened module/package source file tab, right-click on the tab and click `Reveal in Explorer`.
      * Try doing this on `import random` and see where `random.py` is.
      * Note that this doesn't work on `import math` -- on any **built-in** modules
      * Try doing this on `import os` and note that it's not a package, but a module (though we use something like `import os.path`).
        * See the Python's flexible namespace-manipulation capability

### Documentation

* Let's use [Docstrings](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Documentation.html#docstrings) as much as possible from now on!

### Exceptions

* `try: ... except: ... else: ... finally: ...`
  * `else` is unique in Python
* Exception handling mechanism:
  * A statement may raise ("throw" in most other programming languages) an exception when it's executed.
  * If the statement is inside a `try` block, its `except` blocks are searched for the raised exception type.
  * If a matching `except` block is found, then the statements in the `except` block will be executed.
    * The subsequent statements in the `try` block (after the statement where the exception was raised) will NOT be executed! -- It's an unexpected disruption of normal execution.
  * Statements in `else` block will be executed if no statement in the `try` block raised any exception.
    * Useful in minimizing the scope of the `try: ... except: ...` block (which is considered a good practice)
  * Statements in `finally` block will be executed regardless of whether any exception was raised or not.
    * Intended to do any necessary clean-up that should happend regardless (e.g., closing open file/database/network connections), which is very important
  * Any of `except`, `else`, and `finally` are optional.
    * But of course you'd want at least one of these 3 to make your `try: ...` block meaningful.
  * If a raised exception is not handled (caught) by an `except` block, the exception is propagated.
    * The execution of the current call stack frame (either the function where the `try: ...` block is located--let's call this `callee`--or the top-level REPL loop) will be interrupted.
    * The funciton `callee` will return immediately to the function that called `callee` (let's call this function `caller`).
      * Note that the `finally` block statements are still executed, right before `callee` returns to `caller`.
    * The `caller` might have `try: ...` block that might handle the exception.
      * In that case, that exception is handled there.
      * If not, the exception keeps propagating along the call stack, until it's handled, or there's no more call stack frame (at which time your program crashes).
* [Use exceptions for input validation](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Exceptions.html#example-from-mailroom-exercise), rather than your own `if` tests.
  * EAFP: Easier to Ask Forgiveness than Permission
* Don't try to handle all possible exceptions yourself!
  * Sometimes you have to let the caller of your functions handle them.
  * What's important now is to clearly specify the contract: Which (if any, or no) exceptions are handled.
* A lot of real-world experiences/practices needed to master exceptions

### Comprehensions

* Many of you have already started to use this!
* Simple/concise/succinct syntactic reduction of very commonly occurring `for` loops with lists/dicts/sets.
* See [`lightning.py`](../examples/lightning.py) and [`Comprehensions.html`](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Comprehensions.html) for examples
* Functional programming constructs: map and filter
* Know the difference between a generator and a list
  * `range(10)` vs `list(range(10))`
  * Get/use a generator if you will immediately iterate over the result using `for`
  * To get a list from a generator object `gen`, use `list(gen)`.
    * `[gen]` won't work!
