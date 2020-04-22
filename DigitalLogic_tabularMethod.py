#20191666 정주은
#don't care 포함 x

import collections

#1차이나는 값 찾는 함수
def findPartner(arr):
    arr = sorted(arr)
    lst = []
    max_len = 0
    #받은 값 이진수로 바꾸고, string으로 바꾸기
    for i in range(0, len(arr)):
        if(type(arr[i]) == int):
            lst.append(str(bin(arr[i]))[2:])
        else:
            lst = arr
        if(len(lst[i]) > max_len): max_len = len(lst[i])


    #각 PI의 크기 맞춰주기
    for i in range(len(lst)):
        fill = max_len - len(lst[i])
        if (fill != 0): lst[i] = "0"*fill +lst[i]

    ##print("lst: ",lst)

    #1차이 나는 값 찾기
    partner = [] #짝짓는 리스트
    difference = set() #중복 방지 위해 set함수 사용
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            diff = 0
            for k in range(max_len):
                if (lst[i][k] != lst[j][k]): diff += 1; #차이나는 개수 추가
            #1차이나는 값 리스트와 set함수에 담기
            if(diff == 1): partner.append([lst[i], lst[j]]); difference.add(lst[i]); difference.add(lst[j])

    ##print("differnece set: ", difference)
    difference = list(difference)

    #파트너 지으면서 포함되지않은 PI 찾기
    answer = collections.Counter(lst) - collections.Counter(difference)
    #set함수를 list로 바꾸기
    answer = list(answer)
    #파트너와 포함되지 않은 PI 합치기
    answer += partner

    ##print("partner: ",partner)

    #함수끼리 호출하는 것 -> 무한루프에 빠지지 않게 하기위한 조건설정
    if(len(partner)==0):
        ##print(arr)
        return arr

    ans = mergePartner(answer)
    return set(ans)

#findParnter에서 찾았던 짝들 정리하는 함수
def mergePartner(arr):
    temp_arr = []
    if(type(arr[0]) == str): max_len = len(arr[0])
    else: max_len = len(arr[0][0])
    ##print(max_len)

    #찾은 파트너에서 1차이나는 부분 '-'으로 치환하기
    for i in range(len(arr)):
        #findPartner함수에서 주는 리스트 안에 string 타입이 있다면 그냥 리스트에 추가.
        if(type(arr[i]) == str): temp_arr.append(arr[i]); continue
        #findPartner함수에서 주는 리스트 안에 list 타입이 있다면 1차이 나는 것이 있기때문에 처리해줌.
        for j in range(0, max_len):
            if (arr[i][0][j] != arr[i][1][j]):
                if(j==0):
                    temp_str = "-"+arr[i][0][j+1:]
                elif(j==max_len-1):
                    temp_str = arr[i][0][:max_len-1]+"-"
                else:
                    temp_str = arr[i][0][:j] + "-" +arr[i][0][j+1:]

                temp_arr.append(temp_str)
                break
    ##print("mergepartner: ",temp_arr)
    tm = findPartner(temp_arr)
    return tm

#결과 정리하는 함수
def result_func(arr):
    result = findPartner(arr)
    print("result EPI: ",result)
    result = list(result) #set함수를 list로 바꾸기
    max_len = len(result[0])

    #변수설정하기
    variables = []
    for i in range(max_len):
        variables.append('x{0}'.format(i+1))
    #변수보여주기
    print("variables: ",variables)

    #결과보여주기
    print("ANSWER: ", end='')
    for i in range(len(result)):
        for j in range(max_len):
            if(result[i][j] == '0'):
                print(variables[j]+"\'", end='')
            elif(result[i][j] =='1'):
                print(variables[j], end='')
        if(i != len(result)-1):
            print(end=" + ")
        else:
            print("\n\nEnd")


if __name__ == "__main__":
    F = [0, 2, 5, 6, 7, 8, 9, 13]
    result_func(F)
