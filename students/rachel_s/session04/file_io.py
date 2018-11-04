languages = set()

with open("students.txt") as f:
    for line in f.readlines():
        content = line.split(":")[1].strip().split()
        if line.split(":")[0] != "Name":
            for word in content:
                word = word.replace(',', '')
                if not word.istitle() and not word == 'nothing':
                    languages.add(word)

