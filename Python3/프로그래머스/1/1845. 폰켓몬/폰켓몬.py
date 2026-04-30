# 종류 개수를 파악하기 위해서
# collections.Counter를 쓸 필요 없이
# set()만 사용하면 된다.
def solution(nums):
    max_nums = len(nums)/2
    types = len(set(nums))
    if types < max_nums:
        return types
    else:
        return max_nums