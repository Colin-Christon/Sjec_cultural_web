import re

link = re.compile(r'href="(.*?)"')
srcLink = re.compile(r'src="(.*?)"')

with open("rnd.html", "r") as reader:
    s = ""
    with open("fixed.html", "w+") as writer:
        for line in reader.readlines():
            newLine = link.sub(r"href='https://sjec.ac.in/\1'", line)
            newLine = srcLink.sub(r"src='https://sjec.ac.in/\1'", newLine)
            s += newLine + "\n"
        writer.write(s)