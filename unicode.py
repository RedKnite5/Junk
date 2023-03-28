import io

with io.open("unicode.txt", "w+", encoding="utf8") as file:
  for i in range(32, 127):
    file.write(chr(i))
  for i in range(161, 130_000):
    try:
      file.write(chr(i))
    except UnicodeEncodeError:
      pass
