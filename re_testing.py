import re
#   python re_testing.py



s = "Isaac Newton, physicist"
reg = "(\w+) (\w+)"
m = re.match(r"(\w+) (\w+)","Isaac Newton,physicist")

print(m.groups())