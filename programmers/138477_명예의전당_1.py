def solution(k, score):
    answer = []
    podium = []
    for s in score:
        if len(podium) < k:
            podium.append(s)
            podium = sorted(podium, reverse=True)
            answer.append(podium[-1])
        elif len(podium) >= k:
            if podium[-1] >= s:
                pass
            elif podium[-1] < s:
                podium = podium[:k-1]
                podium.append(s)
                podium = sorted(podium,reverse=True)
            answer.append(podium[-1])
    return answer