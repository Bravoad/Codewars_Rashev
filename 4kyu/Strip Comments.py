def strip_comments(text: str, comment_markers: list[str]) -> str:
    lines = text.split('\n')
    result = []

    for line in lines:
        min_index = len(line)
        for marker in comment_markers:
            index = line.find(marker)
            if index != -1 and index < min_index:
                min_index = index
        result.append(line[:min_index].rstrip())

    return '\n'.join(result)
