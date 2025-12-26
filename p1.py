def res(s:str):
    n = len(s)
    curr = ""
    result = 0
    count = 0
    if len(s)>0:
        for char in s:
            if curr=="":
                curr = char
                count = 1
            else:
                if curr == char:
                    count+=1
                else:
                    if count%2==0:
                       result+=count
                    count = 1
                    curr = char
    print(result)

res("aaabbaccccdds")