# euler19.py

import arrow

count = 0

start = arrow.get("1901-01-01", "YYYY-MM-DD")
end = arrow.get("2000-12-31", "YYYY-MM-DD")
for i in arrow.Arrow.range("day", start, end):
	if i.weekday() == 6 and i.day == 1:
		count += 1
print(count)
