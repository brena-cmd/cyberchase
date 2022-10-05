
w, h = map(int, input().split())

n = int(input())

pairs = {}

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    is_in_edge_pair_1 = ((x1==0 or x1==w) or (y1==0 and y1==h))
    is_in_edge_pair_2 = ((x2==0 or x2==w) or (y2==0 and y2==h))

    if is_in_edge_pair_1 and is_in_edge_pair_2:
        pairs[(x1,y1)]=(x2,y2)
        pairs[(x2,y2)]=(x1,y1)

# topo topo 
# [0][j1] [0][j2]
# dir dir 
# [i1][n-1] [i2][n-1]
# 
# esq esq
# [i1][0] [i2][0]
# baixo baixo 
# [n-1][j1] [n-1][j2]
# = pode dois nós dentro do intervalo


# topo baixo = os dois J' precisam ser maiores ou menores que o J do par corrente
# [0][j1] [n-1][j2]

# topo dir 
# [0][j1] [i][n-1]
# baixo dir 
# [n-1][j1] [i][n-1]


# | topo esq 
# [0][j1] [i][0]



# | baixo esq = 
# [n-1][j1] [i][0]
# 	se J do primeiro for maior, o J do segundo tem que ser maior também
# 	se I do primeiro for maior, o J do segundo tem que ser maior também

# esq dir = os dois I' precisam ser maiores ou menores que o I do par corrente
#[0][j1] [i2][n-1]
positions = {
    'same_horizontal_border':[],
    'same_vertical_border':[],
    'top_dir':[],
    'top_esq':[],
    'baix_dir':[],
    'baix_esq':[],
    'opposites_horizontal':[],
    'opposites_vertical':[]
}

class Rules:
    @staticmethod
    def check_same_horizontal_border(p1,p2,q1,q2):
        if q1[1]>p1[1] and q2[1]<p2[1] and q1[0]==p1[0]==p2[0]==q2[0]:
            return True

        p1,p2,q1,q2 = q1,q2,p1,p2  

        if q1[1]>p1[1] and q2[1]<p2[1] and q1[0]==p1[0]==p2[0]==q2[0]:
            return True
        
        return False


    @staticmethod
    def check_same_vertical_border(p1,p2,q1,q2):
        if q1[0]>p1[0] and q2[0]<p2[0] and q1[1]==p1[1]==p2[1]==q2[1]:
            return True

        p1,p2,q1,q2 = q1,q2,p1,p2  

        if q1[0]>p1[0] and q2[0]<p2[0] and q1[1]==p1[1]==p2[1]==q2[1]:
            return True
        
        return False

    @staticmethod
    def check_top_dir_border(p1,p2,q1,q2,retoric=True):
        if (q1[1]>p1[1] and q2[0]<p2[0]) or (q1[1]<p1[1] and q2[0]>p2[0]):
            return True
        if retoric: 
            Rules.check_top_dir_border(q1,q2,p1,p2, False) 
        
        return False

    @staticmethod
    def check_top_esq_border(p1,p2,q1,q2,retoric=True):
        if (q1[1]<p1[1] and q2[0]<p2[0]) or (q1[1]>p1[1] and q2[0]>p2[0]):
            return True
        if retoric: 
            Rules.check_top_esq_border(q1,q2,p1,p2, False) 
        
        return False

    @staticmethod
    def check_baixo_dir_border(p1,p2,q1,q2, retoric=True):
        if (q1[1]>p1[1] and q2[0]>p2[0]) or (q1[1]<p1[1] and q2[0]<p2[0]):
            return True
        if retoric: 
            Rules.check_baixo_dir_border(q1,q2,p1,p2, False) 
        
        return False
    @staticmethod
    def check_baixo_esq_border(p1,p2,q1,q2,retoric=True):
        if (q1[1]<p1[1] and q2[0]>p2[0]) or (q1[1]>p1[1] and q2[0]<p2[0]):
            return True
        if retoric: 
            Rules.check_baixo_esq_border(q1,q2,p1,p2, False) 
        
        return False

    @staticmethod
    def check_opposites_horizontal(p1,p2,q1,q2):
        if (q1[1]<p1[1] and q2[1]<p2[1]) or (q1[1]>p1[1] and q2[1]>p2[1]):
            return True

    @staticmethod
    def check_opposites_vertical(p1,p2,q1,q2):
        if (q1[0]<p1[0] and q2[0]<p2[0]) or (q1[0]>p1[0] and q2[0]>p2[0]):
            return True


for n1, n2 in pairs.items():
    for position, points in positions.items():

    if n1[0]==n2[0]:
        positions['same_horizontal_border'].append((n1,n2)) 
    elif n1[1]==n2[1]:
        positions['same_vertical_border'].append((n1,n2)) 
    
    elif n1[0]!=n2[0]:
            positions['opposites_vertical'].append((n1,n2))
    elif n1[1]!=n2[1]:
        positions['opposites_horizontal'].append((n1,n2))
    
    elif n1[0]==0:
        if n2[1]==w:
            positions['top_dir'].append((n1,n2)) 
        else:
            positions['top_esq'].append((n1,n2)) 
    elif n1[0]==h:
        if n2[1]==w:
            positions['baix_dir'].append((n1,n2)) 
        else:
            positions['baix_esq'].append((n1,n2)) 
    


print(pairs)