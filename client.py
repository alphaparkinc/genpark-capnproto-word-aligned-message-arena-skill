class CapnProtoArena:
    """
    Cap'n Proto 64-Bit Word-Aligned Arena Allocator.
    Eliminates decoding overhead through in-memory wire formatting.
    """
    def __init__(self):
        self.words = []

    def allocate_object(self, data_words, pointer_words):
        start_idx = len(self.words)
        tag = (data_words << 48) | (pointer_words << 32)
        self.words.append(tag)
        self.words.extend([0] * (data_words + pointer_words))
        return start_idx

    def set_data(self, obj_ptr, data_idx, val):
        self.words[obj_ptr + 1 + data_idx] = val

    def get_data(self, obj_ptr, data_idx):
        return self.words[obj_ptr + 1 + data_idx]
