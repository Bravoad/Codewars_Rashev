def snail(snail_map: list) -> list:
    final_array = []
    while snail_map:
        final_array += snail_map.pop(0)
        if snail_map and snail_map[0]:
            for row in snail_map:
                final_array.append(row.pop())
        if snail_map:
            final_array += snail_map.pop()[::-1]
        if snail_map and snail_map[0]:
            for row in snail_map[::-1]:
                final_array.append(row.pop(0))
    return final_array


array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]
print(snail(array))
