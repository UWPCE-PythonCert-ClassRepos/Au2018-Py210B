# Lesson 3 (week 3) for PYTHON210B, Autumn 2018 (October 17, 2018)

## Topics

### Logistics

* Attendance check (TA)
* Lightning talks after the first break
* Office hours
  * Instructor: Tuesday 7:30-9pm online only through [Zoom](https://washington.zoom.us/my/python2018)
  * TA: Optional or TBA
* Due dates for week 3
  * Lesson 3 Exercises by 11:59pm, Tuesday, Oct. 23, 2018 (5 points each, Canvas submissions of your source files required, one single PR for all the week 3 submissions should include source files for all the exercises)
    * Slicing Lab: https://canvas.uw.edu/courses/1231462/modules/items/8758994
    * List Lab: https://canvas.uw.edu/courses/1231462/modules/items/8758995
    * String Formatting Lab: https://canvas.uw.edu/courses/1231462/modules/items/8758996
  * Lesson 3 Assignment by 11:59pm, Tuesday, Oct. 23, 2018 (15 points, Canvas submission of your source files required, one single PR for all the week 3 submissions should include source files for this assignment as well)
    * Mailroom, Part 1: https://canvas.uw.edu/courses/1231462/modules/items/8758997

### Git & Github exercises

* https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Git.html
* Remember the routine and apply to your coding activities
  * At the beginning of every work session: `git pull upstream master` and then `git push origin master`
  * Frequently commit your changes to your local repo
    * `git add <your_changed_file>` to add a single file to the current change set (called "staging"). This applies not only to new files, but also to existing files that are changed. `git add .` will stage all changed files under the current directory, so it could be useful, but we need to be careful not to include unwanted files.
    * `git commit -m "Your commit message"`. The commit message should be descriptive and also succinct.
  * At the end of every work session, push your new commits to your remote (`origin`) mostly for backup purpose
    * `git push origin master`
  * For assignment submission purpose, make only 1 github PR (for all the submissions on that week) nearing the due time
    * No command line for github PR creation. Use the web interface.
  * If you'd like to have your non-final code reviewed, feel free to send a PR, but add notes asking for an intermediate review and email us as a reminder.

### Miscellaneous

* VSCode run selection
  * Start a terminal and run `ipython`
  * Select a block of Python code in your editor
  * `Ctrl-Shift-p`, then enter `Run Selected Text In Active Terminal` (will pop up and allow you to pick)
  * Still have to press Enter in the ipython session on the terminal (that's why this is still not ideal)
  * Next time you enter `Ctrl-Shift-p`, you don't have to enter the command name, but should see it at the top and select it.
* Github PR merge conflict resolution
  * If your PR says there's a merge conflict with your PR, let us know and resolve the conflict.

### Boolean

* Truthiness: Need to remember the rules [What is False?](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Booleans.html#what-is-false)
* `and` and `or` short-circuiting: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Booleans.html#shortcutting
  * Some typos in the material [Booleans.html](https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Booleans.html): See [PR](https://github.com/UWPCE-PythonCert/PythonCertDevel/pull/169) for a fix
* Condition expressions: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Booleans.html#conditional-expressions

### Sequences

* Slicing: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#slicing
  * `sequence[first_to_include:first_to_exclude:increment]`
  * The indices-as-dividers analogy works as well, but not well for a negative increment
* Useful methods on sequences: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#miscellaneous
  * `min(seq)`, `max(seq)`, `seq.index(item)`, `seq.count(item)`, iterating over a sequence using `for`
* Lists vs. tuples (mutable, immutable)
  * Gotchas
    * https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#lists-are-mutable
    * https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#other-gotchas
    * https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#mutable-default-argument
  * Mutable sequence methods
    * `.append()` vs `.insert()` vs `.extend()`: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#growing-the-list
    * Shallow vs deep copy: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#shallow-copies
  * List performance (big-Oh): https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Sequences.html#list-performance

### Iteration

* `else` block in `for`: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Iteration.html#else
* `for` loops idioms: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Iteration.html#nifty-for-loop-tricks

### Strings

* `str(obj)`: E.g., `str(34) == "34"`
* String methods
  * `str.split(delim)` and `str.join(seq)`: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Strings.html#splitting-and-joining-strings
  * Building up a long string: Use `"".join(seq)` instead of `+=`
  * Ordinal: `ord(ch)`
  * String formatting: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Strings.html#string-formatting
    * You'll need to study various string formatting options: https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Strings.html#complex-formatting
  * f-strings
    * https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Strings.html#literal-string-interpolation
    * Shell-like string construction
