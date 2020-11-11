# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        DIFF = ord('a') - 1
        int_list = []
        ans = ''
        first, second, sign = 0, 0, 0
        for idx_ch in range(len(s) - 2):
            first = s[idx_ch]
            second = s[idx_ch + 1]
            sign = s[idx_ch + 2]
            print(f'{first} {second} {sign}')
            if sign == '#':
                print(f'>> {int(first + second)}')
                int_list.append(int(first + second))
            else:
                if first != '#' and second != '#':
                    int_list.append(int(first))
        print(f'>>>> {int_list}')
        
        if s[len(s) - 1] != '#' and s[len(s) - 2] != '#': int_list.append(int(s[len(s) - 2]))
        if s[len(s) - 1] != '#': int_list.append(int(s[len(s) - 1]))
    
        for digit in int_list:
            print(digit)
            ans += chr(digit + DIFF)
        
        return ans

        

cl = Solution()

print('cl.freqAlphabets("10#11#12"): ', cl.freqAlphabets("10#11#12"))
print('cl.freqAlphabets("1326#"): ', cl.freqAlphabets("1326#"))
print('cl.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"): ', cl.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))

# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 