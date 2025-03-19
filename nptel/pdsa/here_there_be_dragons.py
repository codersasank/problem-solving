r, c, k, d = map(int, input().split())
locations = list()
for i in range(d):
    row, col = map(int, input().split())
    locations.append( (row, col) )

locations.sort( key = lambda x:x[0])
dragon_columns = [None for i in range(r)]
locations.sort(key=lambda x:x[0]) 
distances = [[0 for slain in range(d+1)] for loc in range(d)]

for loc in range(d):
    distances[loc][1] = locations[loc][0] + locations[loc][1]

for slain in range(2, d+1):
    for loc in range(slain-1, d):
        row, col = locations[loc]
        prev_row, prev_col = locations[loc-1]
        min_dist = distances[loc-1][slain-1] + (row-prev_row) + abs(col-prev_col)
        for j in range(loc-2, slain-3, -1):
            prev_row, prev_col = locations[j]
            dist = distances[j][slain-1] + (row-prev_row) + abs(col-prev_col)
            if dist < min_dist:
                min_dist = dist
        distances[loc][slain] = min_dist
        
min_dist = distances[k-1][k]
for loc in range(k, d):
    dist = distances[loc][k]
    if dist < min_dist:
        min_dist = dist
print ( min_dist )
    
        
