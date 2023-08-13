class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.max_list_of_list1 = len(list_of_list)

    def __iter__(self):
        self.next_element = self.list_of_list[0]
        self.counter = 0
        self.elements_index = -1
        return self

    def __next__(self):
        self.elements_index += 1
        if self.elements_index >= len(self.next_element):
            self.counter += 1
            if self.counter >= self.max_list_of_list1:
                raise StopIteration
            # self.counter += 1
            self.next_element = self.list_of_list[self.counter]
            self.elements_index = 0

        return self.next_element[self.elements_index]

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
    