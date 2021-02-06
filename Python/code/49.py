class Solution:
    def groupAnagrams(self, strs):
        mode_key = []
        mode_list = []
        for is_str in strs:
            temp_dic = {}
            for c in is_str:
                if c in temp_dic.keys():
                    temp_dic[c] += 1
                else:
                    temp_dic[c] = 1
            find = False
            print(temp_dic)
            for i in range(len(mode_key)):
                if len(mode_key[i]) == len(temp_dic):
                    find = True
                    for key,value in mode_key[i].items():
                        print("key:{},value:{}".format(key,value))
                        if (key in temp_dic.keys()) and temp_dic[key] == value:
                            find = True
                        else:
                            find = False
                            break
                    if find == True:
                        mode_list[i].append(is_str)
                        break
            if find == False or len(mode_key)==0:
                mode_key.append(temp_dic)
                mode_list.append([is_str])
        return mode_list


if __name__ == '__main__':
	mysolution = Solution()
	strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
	strs2 = ["ddddddddddg","dgggggggggg"]
	strs3 = ["",""]
	print(mysolution.groupAnagrams(strs))