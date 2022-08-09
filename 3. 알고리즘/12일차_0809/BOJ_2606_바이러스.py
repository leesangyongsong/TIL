N = int(input())

M = int(input())
network = [[] for _ in range(N+1)]
for i in range(M) :
    u, v = map(int, input().split())
    network[u].append(v)
    network[v].append(u)
visit = [0] * (N+1) # 방문한 컴퓨터를 표시
def dfs(u) : # 
    visit[u] = 1 # 
    for i in network[u] :
        if visit[i] == 0 :
            dfs(i)
dfs(1)

print(sum(visit)-1)