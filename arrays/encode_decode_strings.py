from typing import List

class Solution:
    # BFM   
    def encode(self, strs: List[str]) -> str:
        encoded_str: str = ""

        for word in strs:
            encoded_str += word + "ram"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list: List[str] = s.split("ram")
        return decoded_list[:len(decoded_list) - 1]