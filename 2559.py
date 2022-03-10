## 시간 제한

N, K = map(int, input().split())
temp_lst = list(map(int, input().split()))

sum_tmp = sum(temp_lst[:K])
tmp_kdays =[sum_tmp]

# for문 내에서 복잡한 연산 최대한 없애기 (sum을 밖에서 한번만)
for i in range(N-K):
    # 맨앞 지우고 맨뒤 +1 index를 더하기
    sum_tmp = sum_tmp - temp_lst[i] + temp_lst[i+K]
    tmp_kdays.append(sum_tmp)

print(max(tmp_kdays))