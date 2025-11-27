def dfs(maze, x, y, end_x, end_y, path):
    
    # Überprüfe, ob die aktuelle Position außerhalb der Grenzen des Labyrinths liegt oder ob sie eine Wand ist, oder ob sie mit 'X' bereits markiert wurde
    if (x < 0 or x >= len(maze) or
        y < 0 or y >= len(maze[0]) or
        maze[x][y] == '#' or
        maze[x][y] == 'X'):
        return False
    # Überprüfe, ob die aktuelle Position das Ziel ist
    if x == end_x and y == end_y:
        path.append((x, y))
        return True
    # Überprüfe, ob die aktuelle Zelle schon Teil des Pfades ist oder als besucht markiert wurde mit '.' oder 'X'
    if maze[x][y] == '.' or (x, y) in path:
        return False
    # Markiere die aktuelle Zelle als besucht, indem du sie mit '.' markierst
    maze[x][y] = '.'
    # Füge die aktuelle Position zum Pfad hinzu
    path.append((x, y))

    # Rekursive DFS-Suche in alle vier Richtungen (unten, oben, rechts, links)
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        if dfs(maze, x + dx, y + dy, end_x, end_y, path):
            return True
    # Entferne die aktuelle Position vom Pfad
    path.pop()
    # Ersetzt die aktuelle Zelle mit 'X', um sie als Sackgasse zu markieren
    maze[x][y] = 'X'
    return False    
