import copy

format = dict()
tickets = list()

with open('day16Input.txt', 'r') as f:
    stage = 1
    skipLine = False
    for line in f.readlines():
        if skipLine == True:
            skipLine = False
        elif line == '\n':
            skipLine = True
            stage += 1
        elif stage == 1:
            s = line.strip().split(':')
            ranges = s[1].split(' or ')
            r1 = ranges[0].split('-')
            r2 = ranges[1].split('-')
            r1 = [int(r1[0]), int(r1[1])]
            r2 = [int(r2[0]), int(r2[1])]
            format[s[0]] = range(r1[0], r1[1] + 1), (range(r2[0], r2[1] + 1))
        elif stage == 2:
            my_ticket = list(map(int, line.strip().split(',')))
        else: # stage == 3
            tickets.append(list(map(int, line.strip().split(','))))

all_ranges = [r for value in format.values() for r in value]
def has(x):
    for r in all_ranges:
        if x in r:
            return True
    return False

# print([r for value in format.values() for r in value])
sum_ = 0
for ticket in tickets:
    for item in ticket:
        if not has(item):
            sum_ += item

print(sum_)

# part two: 
# Create a function which checks if a ticket is valid
# Remove these tickets
# create a function that checks if a ticket position satisfies a ticket field
# Use this to create a bipartite graph
# Use FF to find a bipartite matching

def is_valid(ticket):
    for item in ticket:
        if not has(item):
            return False
    return True

valid_tickets = []
for ticket in tickets:
    if is_valid(ticket):
        valid_tickets.append(ticket)

def satisfies_field(pos, r):
    for ticket in valid_tickets:
        if not (ticket[pos] in r[0] or ticket[pos] in r[1]):
            return False
    return True

n = len(format)

g = [] # first n nodes are ticket positions, next n nodes are ticket fields
for i in range(2*n):
    g.append([])

for i in range(n):
    for j, r in enumerate(format.values()):
        if satisfies_field(i, r):
            g[i].append(j+n)
            g[j+n].append(i)

# Take undirected bipartite graph g and create a flow graph fg
def make_flow_graph(g):
    s = 2 * n
    t = 2 * n + 1
    fg = [] # [0, n-1] are first half, [n, 2n-1] are 2nd half, 2n is s, 2n+1 is t
    for i in range(2*n + 2):
        fg.append({})
    for i in range(n):
        fg[s][i] = 1
        fg[i+n][t] = 1
        for j in g[i]:
            fg[i][j] = 1
    return fg


def dfs(g, s, t):
    '''
    Finds an s-t path in g and returns the reverse of this path and the bottleneck value
    '''
    n = len(g)
    visited = [False] * n
    parent = [-1] * n
    visited[s] = True

    stack = list()
    stack.append(s)
    while stack:
        u = stack.pop()
        for v in g[u].keys():
            if v == t:
                bottleneck = g[u][t]
                path = [t, u]
                while parent[u] != -1:
                    bottleneck = min(bottleneck, g[parent[u]][u])
                    path.append(parent[u])
                    u = parent[u]
                return path, bottleneck
            elif not visited[v]:
                stack.append(v)
                visited[v] = True
                parent[v] = u
    return None, 0

def ff(fg, s, t):
    '''
    Runs the Ford Fulkerson algorithm. Returns a max flow and its value.
    '''
    gr = copy.deepcopy(fg)
    path, bottleneck = dfs(gr, s, t)
    while path != None:
        u = path.pop()
        while path:
            v = path.pop()
            if gr[u][v] == bottleneck:
                del gr[u][v]
            else:
                gr[u][v] -= bottleneck
            if u in gr[v]:
                gr[v][u] += bottleneck
            else:
                gr[v][u] = bottleneck
            u = v
        path, bottleneck = dfs(gr, s, t)
    for u, d in enumerate(fg):
        for v in d.keys():
            if v in gr[u]:
                fg[u][v] = max(0, fg[u][v] - gr[u][v])
    return fg, sum(fg[s].values())
    
def find_matching(max_flow, n):
    matching = []
    for i in range(n):
        for j in max_flow[i]:
            if max_flow[i][j] == 1:
                matching.append((i, j-n))
    return matching

fg = make_flow_graph(g)
max_flow, value = ff(fg, 2 * n, 2 * n + 1)

print(n, value)

matching = find_matching(max_flow, n)

prod = 1
for (i, j) in matching:
    if j in range(0, 6):
        prod *= my_ticket[i]

print(prod)






        
        






