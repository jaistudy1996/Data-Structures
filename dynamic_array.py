
import ctypes

class Dynamic_Array:
    def __init__(self):
        # initial length is zero
        self._length = 0
        # initial capacity is 1 as there are no elements
        self._actual_capacity = 1
        self._array = self._generate_array(self._actual_capacity)

    def __len__(self):
        return self._length

    def __getitem__(self, index):
        if(index >= self._length):
            raise IndexError
        else:
            return self._array[index]

    def append(self, item):
        if(self._length < self._actual_capacity):
            self._array[self._length] = item
            self._length += 1
        else:
            newArray = self._generate_array(2 * self._actual_capacity)
            for index in range(self._actual_capacity):
                newArray[index] = self._array[index]
            self._array = newArray
            self._actual_capacity *= 2
            self._array[self._length] = item
            self._length += 1

    def _generate_array(self, size):
        return (size * ctypes.py_object)()



def main():
    print("Dynamic Array Test")
    testArray = Dynamic_Array()
    print("Length should be 0: ", len(testArray))
    testArray.append(1)
    print("Length should be 1: ", len(testArray))
    testArray.append(2)
    print("Length should be 2: ", len(testArray))
    testArray.append(4)
    print("Length should be 3: ", len(testArray))
    print("1 ==", testArray[0], ", 2 ==", testArray[1], ", 4 ==", testArray[2])
    print(type(testArray))


if(__name__ == "__main__"):
    main()
