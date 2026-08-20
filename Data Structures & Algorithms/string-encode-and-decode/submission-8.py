class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for st in strs:
            st_len = len(st)
            len_st_len = len(str(st_len))
            encoded_str += f"#{len_st_len}{st_len}{st}"

        return encoded_str

    def decode(self, s: str) -> List[str]:
        result_st = []

        st_to_build = ""
        length_to_append = 0
        current_idx = 0
        should_append = False
        while current_idx < len(s):
            if should_append == False:
                if s[current_idx] == "#":
                    digits_len = int(s[current_idx + 1])
                    len_of_str = int(s[(current_idx + 2):current_idx + 2 + digits_len])
                    length_to_append = len_of_str
                    current_idx += (2 + digits_len)
                    if current_idx >= len(s):
                        result_st.append("")
                    should_append = True
            else:
                if length_to_append > 0:
                    st_to_build += s[current_idx:current_idx + length_to_append]
                current_idx += length_to_append
                result_st.append(st_to_build)
                st_to_build = ""
                should_append = False

        return result_st
