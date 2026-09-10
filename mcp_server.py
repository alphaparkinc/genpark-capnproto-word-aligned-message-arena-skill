import sys
import json
from client import CapnProtoArena

def main():
    arena = CapnProtoArena()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "allocate":
            p = arena.allocate_object(params.get("data_words", 1), params.get("pointer_words", 0))
            res = {"ptr": p}
        elif method == "set":
            arena.set_data(params.get("ptr"), params.get("idx"), params.get("val"))
            res = {"status": "ok"}
        elif method == "get":
            res = {"val": arena.get_data(params.get("ptr"), params.get("idx"))}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
