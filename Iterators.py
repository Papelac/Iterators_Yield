
class FlatIterator:

    def __init__(self, list_of_list):
        self.start = 0
        self.end = len(list_of_list)-1
        self.list_of_list = list_of_list
        self.flat_list = []

    def _get_flat_list_(self):
        while (self.start <= self.end):
            for elem in self.list_of_list[self.start]:
                self.flat_list.append(elem)
            self.start += 1
 
    def __iter__(self):
        self._get_flat_list_()
        self.start = -1
        self.end = len(self.flat_list)
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.end:
            raise StopIteration
        
        item = self.flat_list[self.start]
        return item


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