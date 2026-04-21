def solution(participant, completion):
    hash = dict()
    for name in participant:
        hash[name] = hash.get(name, 0) + 1
    # #디버깅 코드
    # print("[Participant]")
    # for name, count in hash.items():
    #     print(f"이름:{name}\t횟수:{count}")
    
    for name in completion:
        hash[name] -= 1
    # #디버깅 코드
    # print("\n[Completion]")
    # for name, count in hash.items():
    #     print(f"이름:{name}\t횟수:{count}")
        
    for key in hash:
        if hash[key]>0:
            answer=key
    return answer

"""
N<100,000 #NlogN
participant(참여한 선수들의 리스트, size N)
completion(완주한 선수들의 리스트, size N-1)
"""