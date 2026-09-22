class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = dict()
        for st in strs:
            counter = self.MyCounter(st)
            if counter in resDict:
                resDict[counter].append(st)
            else:
                resDict[counter] = [st]
        lista = []
        for val in resDict.values():
            lista.append(val)

        return lista


        
    
    def MyCounter(self, string: str) -> dict:
        dictA = dict()
        string = sorted(string)
        for l in string:
            if l in dictA:
                dictA[l] += 1
            else:
                dictA[l] = 1
        return str(dictA)
        
