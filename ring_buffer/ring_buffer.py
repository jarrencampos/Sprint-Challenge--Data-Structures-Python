class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.structure = []
        self.structure_index = 0

    def append(self, item):
        if len(self.structure) < self.capacity:
            self.structure.append(item)

        else:
            if self.structure_index < self.capacity:
                self.structure.pop(self.structure_index)
                self.structure.insert(self.structure_index, item)
                self.structure_index += 1
            else: 
                self.structure_index = 0
                self.structure.pop(self.structure_index)
                self.structure.insert(self.structure_index, item)
                self.structure_index += 1

    def get(self):
        return self.structure