'''
만약 두 딱지의 별의 개수가 다르다면, 별이 많은 쪽의 딱지가 이긴다.
별의 개수가 같고 동그라미의 개수가 다르다면, 동그라미가 많은 쪽의 딱지가 이긴다.
별, 동그라미의 개수가 각각 같고 네모의 개수가 다르다면, 네모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모의 개수가 각각 같고 세모의 개수가 다르다면, 세모가 많은 쪽의 딱지가 이긴다.
별, 동그라미, 네모, 세모의 개수가 각각 모두 같다면 무승부이다.
'''

T = int(input())
for t in range(T):
    A = list(input().split())
    B = list(input().split())
    # 맨 앞 숫자 없애기
    A.pop(0)
    B.pop(0)
    
    # 카드 그림 파악
    card_dict = {'A': [0, 0, 0, 0], 'B': [0, 0, 0, 0]}
    # [별, 동그라미, 네모, 세모] 개수 리스트 딕셔너리 value 값으로 저장
    for i in range(4):
       card_dict['A'][3-i] = A.count(str(i+1))
       card_dict['B'][3-i] = B.count(str(i+1))

    # 무승부
    if card_dict['A'] == card_dict['B']:
        print('D')
    # 승부가 날때, 별, 동그라미, 네모, 세모 순으로 우열 가리기
    else: 
        for j in range(4):
            if card_dict['A'][j] > card_dict['B'][j]:
                print('A')
                break
            elif card_dict['A'][j] < card_dict['B'][j]:
                print('B')
                break
            else:
                pass


