"""Tests for the :mod:`campy.datastructures.linkedlist` module."""
import linkedlist as LS

def test_empty_list():
	list1 = LS.LinkedList()
	assert list1.isEmpty()

def test_basic_operations():
	#test making a list and populating it
	list1 = LS.LinkedList()
	list1.add("tristen")
	assert list1[0].value == "tristen"

	for x in range(100):
		list1.add(x)

	#create new list for comparison
	list2 = LS.LinkedList()
	list2.add("Me")

	assert list1.equals(list2) == False

	#create third list for more comparison of equal lists
	list3 = LS.LinkedList()
	list3.add("Me")

	assert list2.equals(list3)

def test_advanced_operations():
	#test insertion and __getitem__
	list1 = LS.LinkedList()

	for x in range(10):
		list1.add(x)

	list1.insert(2, 1337)
	assert list1[2].value == 1337

	#test remove and __delitem__
	list1.remove(2)
	assert list1[2].value != 1337
	assert list1[2].value == 2

	#finally test the size function
	assert list1.size() == 10

if __name__ == '__main__':
	test_empty_list()
	test_basic_operations()
	test_advanced_operations()
