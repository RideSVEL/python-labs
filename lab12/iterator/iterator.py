class CarAssembler:
    def __iter__(self):
        return self

    def __init__(self, spisok):
        self.spisok = spisok
        self.limit = len(spisok)
        self.counter = -1

    def __next__(self):
        if self.counter + 1 < self.limit:
            self.counter += 1
            return self.spisok[self.counter]
        else:
            raise StopIteration
