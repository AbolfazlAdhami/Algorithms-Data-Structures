class MemoryManager:
    def __init__(self, memory):
        self.memory = memory
        self.blocks = [{'start': 0, 'size': len(memory), 'free': True}]

    def allocate(self, size):
        for block in self.blocks:
            if block['free'] and block['size'] >= size:
                index = block['start']
                block['free'] = False
                if block['size'] > size:
                    self.blocks.insert(self.blocks.index(block)+1, {
                        'start': block['start']+size,
                        'size': block['size']-size,
                        'free': False
                    })
                block['size'] = size
                return index
        raise Exception("Allocate does not have a memory overhead")

    def release(self, pointer):
        block_index = next((i for i, b in enumerate(
            self.blocks) if b['start'] == pointer and not b['free']), -1)
        if block_index == -1:
            raise Exception("Invalid release")
        self.blocks[block_index]['free'] = True

        if block_index > 0 and self.blocks[block_index-1]['free']:
            self.blocks[block_index -
                        1]['size'] += self.blocks[block_index]['size']
            del self.blocks[block_index]
            block_index -= 1
        if block_index < len(self.blocks) - 1 and self.blocks[block_index+1]['free']:
            self.blocks[block_index]['size'] += self.blocks[block_index+1]['size']
            del self.blocks[block_index+1]

    def read(self, pointer):
        block = next(
            (b for b in self.blocks if not b['free'] and pointer >= b['start'] and pointer < b['start']+b['size']), None)
        if not block:
            raise Exception("Invalid write")
        return self.memory[pointer]

    def write(self, pointer, value):
        block = next((b for b in self.blocks if not b['free'] and pointer >=
                     b['start'] and pointer < b['start']+b['size']), None)
        if not block:
            raise Exception("Invalid write")
        self.memory[pointer] = value


memory = [None] * 10
manager = MemoryManager(memory)
print(manager.blocks)
ptr1 = manager.allocate(3)
print(ptr1)
manager.write(ptr1, 42)
print(manager.blocks)
print(manager.read(ptr1))  # 42
manager.release(ptr1)
print(manager.blocks)
