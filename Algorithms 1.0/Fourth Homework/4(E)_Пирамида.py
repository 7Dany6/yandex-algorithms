def build_pyramid(blocks:list):
    pyramid_blocks = {}
    for width, height in blocks:
        if width not in pyramid_blocks or height > pyramid_blocks[width]:
            pyramid_blocks[width] = height
    return sum(pyramid_blocks.values())


number = int(input())
block = [tuple(map(int, input().split())) for _ in range(number)]
print(build_pyramid(block))
