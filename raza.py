# Python program: List, Tuple, and Set examples

# ---------- LIST ----------
# list ordered होती है और change की जा सकती है (mutable)
my_list = [10, 20, 30, 40]
print("List:", my_list)

# list में बदलाव
my_list.append(50)
print("List after append:", my_list)
my_list[1] = 25
print("List after changing index 1:", my_list)


# ---------- TUPLE ----------
# tuple ordered होता है लेकिन change नहीं किया जा सकता (immutable)
my_tuple = (10, 20, 30, 40)
print("\nTuple:", my_tuple)


# my_tuple[1] = 25


# ---------- SET ----------
# set unordered और unique values रखता है
my_set = {10, 20, 30, 40, 40, 20}
print("\nSet (duplicates auto remove):", my_set)

# set में add और remove कर सकते हैं
my_set.add(50)
print("Set after add:", my_set)
my_set.remove(20)
print("Set after remove 20:", my_set)
