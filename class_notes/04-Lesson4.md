# Lesson 4 (week 4) for PYTHON210B, Autumn 2018 (October 24, 2018)

## Topics

### Logistics

* Attendance check (TA)
* Lightning talks after the first break
* Office hours
  * Instructor: Tuesday 7:30-9pm online only through [Zoom](https://washington.zoom.us/my/python2018)
    * May have to change this to appointment slots?
  * TA: Optional or TBA
* Instructor out of town on 11/7/2018
  * Class will be held using [Zoom](https://washington.zoom.us/my/python2018)
  * In person classroom attendance is still possible/encouraged. TA will be present for anyone who'll attend in person.
* Due dates for week 4
  * Lesson 4 Activities by 11:59pm, Friday, Oct. 26, 2018 (No points, no submissions)
    * Dict, set labs, file processing lab: https://canvas.uw.edu/courses/1231462/modules/items/8759002
  * Lesson 4 Assignments by 11:59pm, Tuesday, Oct. 23, 2018 (15 points each, Canvas submission of your source files required, one single PR for all the week 4 submissions should include source files for this assignment as well)
    * Mailroom, Part 2: https://canvas.uw.edu/courses/1231462/modules/items/8759003
    * Kata Fourteen: Tom Swift Under Milk Wood: https://canvas.uw.edu/courses/1231462/modules/items/8759004

### Git & Github exercises

* If you still have hard time working with git & GitHub, please let us know and help!
* Just repeating the same stuff for convenience:
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

### Dictionaries and Sets

* https://uwpce-pythoncert.github.io/PythonCertDevel/modules/DictsAndSets.html
* Just a lot of syntax/idioms to remember...
* `d[k]` throws if `k not in d`
  * `d.get(k)` never throws. Returns `None` if `k not in d`. Can specify the desired default: `d.get(k, default)`
* Auto initialization of a dict item value
  * Common code pattern
    ``` Python
    if ch not in counts_dict:
        counts_dict[ch] = 0
    counts_dict[ch] += 1
    ```
    Or
    ``` Python
    if word not in book_index_dict:
        book_index_dict[word] = []
    book_index_dict[word].append(page)
    ```
  * Can use `d.setdefault()` for the second case:
    ``` Python
    book_index_dict.setdefault(ch, []).append(page)
    ```
  * Better use `collections.defaultdict`: See [this](https://docs.python.org/3.7/library/collections.html#defaultdict-objects) for more details
    ``` Python
    from collections import defaultdict
    counts_dict = defaultdict(int)
    counts_dict[ch] += 1

    book_index_dict = defaultdict(list)
    book_index_dict[word].append(page)
    ```
  * For `counts_dict`, we can even use `collections.Counter`: See [this](https://docs.python.org/3.7/library/collections.html#counter-objects) for more details
    ``` Python
    >>> from collections import Counter
    >>> cnt = Counter()
    >>> for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    ...     cnt[word] += 1
    >>> cnt
    Counter({'blue': 3, 'red': 2, 'green': 1})
    >>> # Instead of the above, do this:
    ... cnt2 = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
    >>> cnt2
    Counter({'blue': 3, 'red': 2, 'green': 1})
    >>>
    ```
* Sets: Probably used later
  * See examples like [this](https://realpython.com/python-sets/)
  * Remember the set operations: union, intersection, set difference, ...
    * Set theory in mathematics
* Do practice dict/set with the [lab](https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/dict_lab.html), though no submission's required/accepted.

### File Reading and Writing

* https://uwpce-pythoncert.github.io/PythonCertDevel/modules/Files.html
* Not many gotchas, just another lot of syntax/idioms to learn and remember
  * Use `with`!
* Do practice file handling with the [lab](https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/file_lab.html), though no submission's required/accepted.
