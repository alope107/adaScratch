some_dict = {"k1": 5, "k2": 99}
some_list = ["k1", "k2"]

#O(1)
("k1", 5) in some_dict.items()

#O(n) n = len(some_list)
"k1" in some_list