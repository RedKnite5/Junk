def Map(num_buckets=256):
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def Map_hash(aMap, key):
	return hash(key) % len(aMap)

def Map_get_bucket(aMap, key):
	bucket_id = map_hash(aMap, key)
	return aMap[bucket_id]
	
def Map_get_slot(aMap, key, default=None):
	bucket = Map_get_bucket(aMap,key,)
	
	for i, kv in enumetate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	
	retrurn -1, key, default
	
def map_get(aMap, key, default=None):
	i, k, v = Map_get_slot(aMap, key, default=default)
	return v

def Map_set(aMap, key, value):
    bucket = Map_get_bucket(aMap, key)
    i, k, v = Map_get_slot(aMap, key)

    if v:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))

def Map_delete(aMap, key):
    bucket = Map_get_bucket(aMap, key)

    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def Map_list(aMap):
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v

jazz = Map()
Map_set(jazz, 'Miles Davis', 'Flamenco Sketches')
Map_set(jazz, 'Miles Davis', 'Kind Of Blue')
Map_set(jazz, 'Duke Ellington', 'Beginning To See The Light')
Map_set(jazz, 'Billy Strayhorn', 'Lush Life')

print "---- List Test ----"
Map_list(jazz)

print "---- Get Test ----"
print Map_get(jazz, 'Miles Davis')
print Map_get(jazz, 'Duke Ellington')
print Map_get(jazz, 'Billy Strayhorn')

print "---- Delete Test ----"
print "** Goodbye Miles"
Map_delete(jazz, "Miles Davis")
Map_list(jazz)

print "** Goodby Duke"
Map_delete(jazz, "Duke Ellington")
Map_list(jazz)

print "** Goodbye Billy"
Map_delete(jazz, "Billy Strayhorn")
Map_list(jazz)

print "** Goodbye Pork Pie Hat"
Map_delete(jazz, "Charles Mingus")
	