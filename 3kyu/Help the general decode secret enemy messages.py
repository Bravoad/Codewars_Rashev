from functools import lru_cache

@lru_cache(None)
def build_tables(max_len: int):
    alph = [chr(i) for i in range(32, 127)]
    tables = []
    for pos in range(max_len):
        d = {}
        for ch in alph:
            enc = encode("_" * pos + ch)
            d[enc[pos]] = ch
        tables.append(d)
    return tables


def decode(p_what: str) -> str:
    tables = build_tables(len(p_what))
    out = []
    for i, ch in enumerate(p_what):
        if ch == "-":
            out.append("-")
        else:
            out.append(tables[i][ch])
    return "".join(out)
