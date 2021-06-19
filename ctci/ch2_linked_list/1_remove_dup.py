# remove duplicates from an unsorted linked list

import time
from linked_list import LinkedList

# use temporary buffer
def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    # ll.tail = previous
    return ll

# 1 -> 1 -> 2 -> 3 -> 3
# 1 -> 2 -> 3
# bf: O(n^2)
# do it without temporary buffer (my sol)
def remove_dups_mysol(ll):
    if len(ll) ==1:
        return ll

    for node in ll:
        chs = node # chaser
        run = node.next # runner
        while run:
            if run.value == node.value:
                # delete run node
                chs.next = run.next
                run = run.next
            else:
                chs = run
                run = run.next
    # q: what's this line for?
    # ll.tail = previous
    return ll

    
# do it without temporary buffer (sol)
def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner:
            if runner.next and runner.next.value == current.value:
                runner.next = runner.next.next # better way to delete nodes
            else:
                runner = runner.next # step forward
        current = current.next
    return ll
                


testable_functions = (remove_dups, remove_dups_followup)
test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


def example():
    ll = LinkedList.generate(10, 0, 9)
    print(ll)
    remove_dups(ll)
    print(ll)
    print()

    ll = LinkedList.generate(10, 0, 9)
    print(ll)
    remove_dups_followup(ll)
    print(ll)


if __name__ == "__main__":
    example()
