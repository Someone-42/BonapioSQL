import random

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

        assert items[0][1] > 0, "Items cannot have a frequency of 0 or negative"    # We take the first element, we know the first element is the smallest, 
                                                                                    #   so we test if it is over 0 (0 or negative can generate problems in the generation)

        frequencies = [i[1] for i in items] # gathering only the frequency
        freq_intervals = [sum(frequencies[:i]) for i in range(1, len(frequencies) + 1)] # Generating intervals for frequencies

        return (items, freq_intervals)

    def _debug(self):
        """ Prints out debugging information """
        to_str = lambda l : ", ".join([str(i) for i in l])
        print("-- Generator debug print --")
        print("Items :", to_str(self.__items))
        print("Frequencies :", to_str(self.__frequency_intervals))

    def next(self):
        """ Returns the next random item respecting the frequencies """
        r = random.randint(0, self.__frequency_intervals[-1])
        index = 0
        for i, v in enumerate(self.__frequency_intervals):
            if v > r:
                index = i
                break
        return self.__items[i][0] # Returning the item corresponding to the frequency

if __name__ == "__main__":
    # Testing
    items = [
        ("a", 1),
        ("b", 3),
        ("c", 42),
        ("d", 2),
        ("e", 87),
        ("f", 1),
        ("g", 1)
    ]

    g = Generator(items)
    g._debug()

    # Frequency testing
    
    items_total_freq = sum([i[1] for i in items]) # Sum of every frequency
    freq_count = {i[0]: 0 for i in items} # We copy the items into a dictionnary, and set their frequency to 0
    samples = 42000 # The amount of samples used to generate
    multiplier = items_total_freq / samples # The multiplier to range to the frequencies' range defined in the beginning

    for i in range(samples):
        freq_count[g.next()] += 1 # Generating sample amounts of items, and counting them using the dictionnary

    # Human readability
    print("Ran generation test with", samples, "samples :")
    for i in items:
        print(i[0], "supposed", i[1], "generated", round(freq_count[i[0]] * multiplier))
    