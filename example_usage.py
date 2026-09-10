from client import CapnProtoArena

def main():
    print("=== Testing Cap'n Proto Word-Aligned Arena ===")
    arena = CapnProtoArena()
    ptr = arena.allocate_object(data_words=2, pointer_words=0)
    arena.set_data(ptr, 0, 99999)
    val = arena.get_data(ptr, 0)
    print("Direct word read:", val)

    assert val == 99999
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
