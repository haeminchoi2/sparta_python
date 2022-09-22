n = int(input())

def star(l):
    if l == 3: # l이 3일때, 패턴을 넣어준다. why? 최소단위가 3이기때문
        return ['***',
                '* *',
                '***']

    arr = star(l//3) # 예를 들어 l이 27일때, 재귀적으로 star(9) -> star(3) 호출
    stars = []

    for i in arr: # 3의 패턴을, 9의 패턴을 3번 반복해준다
        stars.append(i * 3)

    for i in arr: # 3의 패턴을, 9의 패턴을 3번 반복하지만, 중앙의 내용은 공백으로 처리해준다.
        stars.append(i + ' ' * (l//3) + i)

    for i in arr: # 3의 패턴을, 9의 패턴을 3회 반복해준다.
        stars.append(i*3)

    return stars # append된 리스트를 반환해준다.

print('\n'.join(star(n)))