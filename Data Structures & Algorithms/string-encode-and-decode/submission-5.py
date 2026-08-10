from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_res = ""

        for s in strs:
            encoded_res += f"{len(s)}#{s}"
        return encoded_res

    def decode(self, s: str) -> List[str]:
        decoded_res = []
        decoded_str = ""
        len_str = ""
        skip_length = 0
        reading_len = True

        for ch in s:
            if reading_len:
                if ch == "#":
                    skip_length = int(len_str)
                    len_str = ""
                    reading_len = False

                    if skip_length == 0:
                        decoded_res.append("")
                        reading_len = True
                else:
                    len_str += ch
            else:
                decoded_str += ch
                skip_length -= 1
                if skip_length == 0:
                    decoded_res.append(decoded_str)
                    decoded_str = ""
                    reading_len = True

        return decoded_res

