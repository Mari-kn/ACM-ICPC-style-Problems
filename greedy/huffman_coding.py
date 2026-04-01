# Huffman Coding
# Build an optimal prefix-free binary code based on character frequencies.
# Uses a min-heap to repeatedly merge the two lowest-frequency nodes.
# Time Complexity: O(n log n) | Space Complexity: O(n)
#
# Input format:
#   Line 1: number of test cases t
#   For each test case:
#     Line 1: n (number of characters)
#     Next n lines: character frequency
# Output: Huffman codes for each character, and encoded/decoded demo

import sys
import heapq
input = sys.stdin.readline


class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(chars, freqs):
    heap = [HuffmanNode(c, f) for c, f in zip(chars, freqs)]
    heapq.heapify(heap)

    if len(heap) == 1:
        # Edge case: single character
        root = HuffmanNode(None, heap[0].freq)
        root.left = heap[0]
        return root

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(root):
    codes = {}

    def dfs(node, code):
        if node.char is not None:
            codes[node.char] = code if code else "0"
            return
        if node.left:
            dfs(node.left, code + "0")
        if node.right:
            dfs(node.right, code + "1")

    dfs(root, "")
    return codes


def encode(text, codes):
    return "".join(codes[ch] for ch in text)


def decode(bits, root):
    result = []
    node = root
    for bit in bits:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            result.append(node.char)
            node = root
    return "".join(result)


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        chars = []
        freqs = []
        for _ in range(n):
            parts = input().split()
            chars.append(parts[0])
            freqs.append(int(parts[1]))

        root = build_huffman_tree(chars, freqs)
        codes = build_codes(root)

        # Sort by code length then character for clean output
        for ch in sorted(codes, key=lambda c: (len(codes[c]), c)):
            print(f"  '{ch}': {codes[ch]}")

        total_bits = sum(freqs[i] * len(codes[chars[i]]) for i in range(n))
        total_chars = sum(freqs)
        print(f"total_bits: {total_bits}, avg_bits: {total_bits / total_chars:.2f}")


if __name__ == "__main__":
    main()
