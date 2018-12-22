import node
import random

LIST_SIZE = 10
MAX_ELEM_VALUE = 10
TEST_ITERATIONS = 2


def main():
    for i in range(0, TEST_ITERATIONS):
        head_node, answer_list = create_list()

        print(answer_list)

        for j in range(0, TEST_ITERATIONS):
            test_list(head_node, answer_list)

        print('\n')


def create_list():
    answer_list = []

    head_node = None
    previous_node = None
    for i in range(0, LIST_SIZE):
        new_node = node.Node(random.randint(-MAX_ELEM_VALUE, MAX_ELEM_VALUE))
        answer_list.append(new_node.value)

        if i == 0:
            head_node = new_node
        else:
            previous_node.next = new_node

        previous_node = new_node

    return head_node, answer_list


def test_list(head_node, answer_list):
    n = random.randint(0, LIST_SIZE - 1)

    print("n = ", n)

    nth_last_value = head_node.nth_last_node(n)
    nth_last_answer = answer_list[len(answer_list) - n - 1]

    if nth_last_answer != nth_last_value:
        print("Returned value: ", nth_last_value)
        print("Answer: ", nth_last_answer)
        print("Test Failed")
    else:
        print("TEST PASSED")


if __name__ == "__main__":
    main()
