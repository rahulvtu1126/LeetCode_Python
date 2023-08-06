class Solution:
    def romanToInt(self, s):
        import re
        roman_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        roman_dict_pattern={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        match_pattern=[]
        for i in roman_dict_pattern.keys():
            if s.find(i) >= 0:
                match_pattern.append(roman_dict_pattern.get(i))
                s=s.replace(i, '')             
        s_List=list(s)
        unique_ele=[]
        for i in s_List:
            if i not in unique_ele:
                unique_ele.append(i)
        sum_list=[]
        for i in unique_ele:
            sum_list.append(roman_dict.get(i) * s_List.count(i))
        return(sum(sum_list) + sum(match_pattern))

s=Solution()
# nums="III"
# s.romanToInt(nums)
# nums="LVIII"
# s.romanToInt(nums)
# nums="MCMXCIV"
# s.romanToInt(nums)
        