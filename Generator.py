class Generator:
    __slots__=("__items", "__frequency_intervals")

    def __init__(self, items: list):
        """
        A class that can generate values according to a specified frequency
        @params items: A list of tuples(2) with the first element being the item, and the second being the frequency
        """
        # Setting private fields to prevent modifications from outside the class
        self.__items, self.__frequency_intervals = Generator.__get_items_and_frequencies(items)

    @staticmethod
    def __get_items_and_frequencies(items: list) -> tuple:
        """ Returns a sorted copy of the items, and a list with the frequency intervals """
        items = items[:]
        items.sort(key = lambda t : t[1]) # Sorting items by their frequency

        frequencies = [i[1] for i in items] # gathering only the frequency
        freq_intervals = [sum(frequencies[:i]) for i in range(1, len(frequencies) + 1)] # Generating intervals for frequencies

        return (items, freq_intervals)

    def _debug(self):
        """ Prints out debugging information """
        to_str = lambda l : ", ".join([str(i) for i in l])
        print("-- Generator debug print --")
        print("Items :", to_str(self.__items))
        print("Frequencies :", to_str(self.__frequency_intervals))

    def generate():
        #TODO: Return an item that was chosen randomly
        pass

if __name__ == "__main__":
    # Testing
    g = Generator([
        ("a", 1),
        ("b", 3),
        ("c", 42),
        ("d", 2),
        ("e", 87),
        ("f", 1),
        ("g", 1)
    ])
    g._debug()
