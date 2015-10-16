import sys
from itertools import chain, combinations

def total(arr):
	add = 0
	for i in range(len(arr)):
		add += int(arr[i])
	return add

def dRoot(arr):
	add = total(arr)
	while len(str(add)) != 1:
		add = total(list(str(add)))
	return add

def powerset(arr):
    return chain.from_iterable(combinations(arr, r) for r in range(len(arr)+1))

def allCombos(arr, door):
	pset = list(powerset(arr))
	combos = []
	for item in pset[1:]:
		dig = dRoot(item)
		if dig == door and len(item) >= 3 and len(item) <= 5:
			combos.append(item)
	return combos

def cannotBeSaved(arr, door):
	dead = []
	combos = allCombos(arr, door)
	temp = []
	for item in combos:
		for sub in item:
			temp.append(sub)
	for item in arr:
		if not(item in temp):
			dead.append(item)
	return dead

def maybeSaved(arr, door):
	maybe = []
	dead = cannotBeSaved(arr, door)
	combos = allCombos(arr, door)
	for item in arr:
		for sub in combos:
			if not(item in sub) and item not in maybe and item not in dead:
				maybe.append(item)
	return maybe

def live(arr, door):
	live = list(arr) #list copy
	combos = allCombos(arr, door)
	if len(combos) == 0:
		return []
	for item in arr:
		for sub in combos:
			if not(item in sub) and item in live:
				live.remove(item)
	return live

def doorsCanBeEntered(arr):
	doors = range(1,10)
	pset = list(powerset(arr))
	openable = []
	for sub in doors:
		for item in pset[1:]:
			dig = dRoot(item)
			if dig == sub and len(item) >= 3 and len(item) <= 5 and not(dig in openable) :
				openable.append(dig)
	return openable

print "Door to check? "
door = int(sys.stdin.readline())
print "All possible combinations of people that can enter: "
print allCombos(sys.argv[1:], door)
print "People that will not enter: "
print cannotBeSaved(sys.argv[1:], door)
print "People that can conditionally enter: "
print maybeSaved(sys.argv[1:], door)
print "People that will unconditionally enter: "
print live(sys.argv[1:], door)
print "All doors that can be opened: "
print doorsCanBeEntered(sys.argv[1:])
