# implement an algo to find the kth to last element of a singly linked list
from linked_list import LinkedList,LinkedListNode


# runner technique (current & runner)
def kth_to_last(ll, k) -> LinkedListNode:
    current = runner = ll.head
    count = 0
    while runner:
        if count == k:
            runner = runner.next
            current = current.next
        else:
            count +=1
            runner = runner.next
    return current

test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert kth_to_last(ll, k).value == expected
        print("passed")


if __name__ == "__main__":
    test_kth_to_last()