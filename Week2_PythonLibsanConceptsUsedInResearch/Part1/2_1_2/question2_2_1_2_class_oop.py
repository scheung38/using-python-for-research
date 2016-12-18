# Consider the following code:


class NewList(list):
    def remove_max(self):
        self.remove(max(self))

    def append_sum(self):
        self.append(sum(self))


x = NewList([1, 2, 3])
while max(x) < 10:
    x.remove_max()
    x.append_sum()
print(x)

# What will this print?

