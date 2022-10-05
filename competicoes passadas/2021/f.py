
from pprint import pprint

n, m = map(int, input().split())

edges = { i : [] for i in range(1,n+1)}

for i in range(m):
    u, v = map(int, input().split())
    
    edges[u].append(v)
    edges[v].append(u)


ana = {n}
bob = set()
# ana_adj = edges[n]
bob_adj = [n-1]

while len(bob_adj)>0:
    last = bob_adj.pop()
    bob.add(last)
    for e in edges[last]:
        if not(e in ana.union(bob)):
            bob_adj.append(e)
        
      
res = (ana.union(bob)).symmetric_difference(range(1, n+1))
ana.update(res)

solucao = "".join(['A' if i in ana else 'B' for i in range(1,n+1)])
print(solucao)


    



