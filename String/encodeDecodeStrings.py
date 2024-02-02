from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return ''.join(str(len(s)) + '/' + s for s in strs)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            slash = s.find('/', i)
            length = int(s[i:slash])
            i = slash + length + 1  # Corrected the assignment
            decoded.append(s[slash+1:i])
        return decoded


# Example usage
codec = Codec()
original_strings = ["apple", "banana", "cherry"]
encoded_string = codec.encode(original_strings)
decoded_strings = codec.decode(encoded_string)

print(f"Original Strings: {original_strings}")
print(f"Encoded String: {encoded_string}")
print(f"Decoded Strings: {decoded_strings}")
