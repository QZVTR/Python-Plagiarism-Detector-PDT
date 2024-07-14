import pygame
import numpy as np
import heapq


# Comment 1
def convertGridToGraph(grid, startCoords, endCoords, obstaclesCoords):
    gridWidth, gridHeight = grid
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def isValid(x, y):
        return 0 <= x < gridWidth and 0 <= y < gridHeight

    graph = {}

    for x in range(gridWidth):
        for y in range(gridHeight):
            if (x, y) not in obstaclesCoords:
                neighbors = []

                for dx, dy in movements:
                    newX, newY = x + dx, y + dy

                    if isValid(newX, newY) and (newX, newY) not in obstaclesCoords:
                        neighbors.append((newX, newY))

                graph[(x, y)] = neighbors
    # print(graph)
    return graph


# Comment 2
def dijkstra(start, finish, obstacles):
    graph = convertGridToGraph([800 // 20, 600 // 20], start, finish, obstacles)
    # Initialize distances with infinity for all nodes except the start node
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0

    # Initialize priority queue with the start node
    pq = [(0, start)]
    # Initialize dictionary to keep track of previous nodes in the shortest path
    previous = {node: None for node in graph}

    while pq:
        # Pop node with the smallest distance from the priority queue
        current_distance, current_node = heapq.heappop(pq)

        # If current node is the finish node, we have found the shortest path
        if current_node == finish:
            break

        # Check distances to neighbors and update if shorter path is found
        for neighbor in graph[current_node]:
            distance = current_distance + 1  # Assuming uniform edge weights of 1
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                previous[neighbor] = current_node  # Update previous node
    # Comment 3
    # Reconstruct the shortest path
    path = []
    current = finish
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()

    # Return the shortest distance and the shortest path
    return distances[finish], path


def aStar(start, finish):
    return


# Comment 4


def bfs(start, finish):
    return


# Comment 5


def dfs(start, finish):
    return


# Comment 6
def drawGrid(screen, colour):
    blockSize = 20
    for i in range(0, 800, blockSize):
        for j in range(0, 600, blockSize):
            rect = pygame.Rect(i, j, blockSize, blockSize)
            pygame.draw.rect(screen, colour, rect, 1)


def drawButton(
    screen, x, y, width, height, text, action, startPoint, finishPoint, obstacles
):
    # print(f"Drawing: {text}")

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    font = pygame.font.SysFont("arial", 12)

    gray = (200, 200, 200)
    white = (255, 255, 255)
    black = (0, 0, 0)

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pygame.draw.rect(screen, gray, (x, y, width, height))
        if click[0] == 1:
            action(startPoint, finishPoint, obstacles)
    else:
        pygame.draw.rect(screen, white, (x, y, width, height))

    textSurface = font.render(text, 1, black)
    textRect = textSurface.get_rect(center=(x + width / 2, y + height / 2))
    screen.blit(textSurface, textRect)


# Comment 7


def isInsideGrid(x, y):
    return 0 <= x < 800 and 0 <= y < 600


def main():
    pygame.init()
    pygame.font.init()

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    lime = (0, 255, 0)
    black = (0, 0, 0)
    orange = (255, 165, 0)

    LEFT = 1
    RIGHT = 3

    screen = pygame.display.set_mode((800, 700))
    pygame.display.set_caption("Algolizer")
    screen.fill(white)
    pygame.display.flip()

    startPoint = None
    finishPoint = None
    startSet = False
    finishSet = False
    obstacles = set()
    running = True
    isDrawing = False

    while running:
        drawGrid(screen, black)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                gridX = x // 20
                gridY = y // 20
                if isInsideGrid(x, y):
                    if event.button == LEFT and not startSet:
                        print("Left click (Start Point)")
                        startPoint = (gridX, gridY)
                        startSet = True
                    elif event.button == RIGHT and not finishSet:
                        print("Right click (Finish Point)")
                        finishPoint = (gridX, gridY)
                        finishSet = True
                    elif event.button == LEFT and startSet:
                        print("Added obstacle")
                        isDrawing = True
                        obstacles.add((gridX, gridY))
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == LEFT:
                    isDrawing = False

        if isDrawing:
            x, y = pygame.mouse.get_pos()
            gridX = x // 20
            gridY = y // 20
            if isInsideGrid(x, y):
                obstacles.add((gridX, gridY))
        # Comment 8
        drawButton(
            screen,
            50,
            600,
            50,
            50,
            "Dijkstra",
            dijkstra,
            startPoint,
            finishPoint,
            obstacles,
        )
        drawButton(
            screen, 200, 600, 50, 50, "A*", aStar, startPoint, finishPoint, obstacles
        )
        drawButton(
            screen, 350, 600, 50, 50, "BFS", bfs, startPoint, finishPoint, obstacles
        )
        drawButton(
            screen, 500, 600, 50, 50, "DFS", dfs, startPoint, finishPoint, obstacles
        )

        if startPoint:
            pygame.draw.rect(
                screen, red, (startPoint[0] * 20, startPoint[1] * 20, 20, 20)
            )
        if finishPoint:
            pygame.draw.rect(
                screen, blue, (finishPoint[0] * 20, finishPoint[1] * 20, 20, 20)
            )

        for obstacle in obstacles:
            pygame.draw.rect(
                screen, orange, (obstacle[0] * 20, obstacle[1] * 20, 20, 20)
            )

        # Visualize shortest path if start and finish points are set
        if startPoint and finishPoint:
            distance, path = dijkstra(startPoint, finishPoint, obstacles)
            for node in path:
                pygame.draw.rect(screen, lime, (node[0] * 20, node[1] * 20, 20, 20))

        pygame.display.update()


if __name__ == "__main__":
    main()
