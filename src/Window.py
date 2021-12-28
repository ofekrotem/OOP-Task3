import random

import pygame

from src import DiGraph, GraphAlgo

# Declare Constants like screen size, colors etc.
HEIGHT = 750
WIDTH = 1000
RADIUS = 15
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
GRAY = (169, 169, 169)
DARK_GRAY = (43, 45, 47)
YELLOW = (255, 255, 0)
FPS = 60

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("EX3 - Directed Graphs")
font = pygame.font.SysFont('comicsans', 17)


def draw_window(graph: DiGraph, center_node: int, node_pos: dict):
    # minX, maxX, minY, maxY = float('inf'), float('-inf'), float('inf'), float('-inf')
    # for n in graph.nodes:
    #     if node_pos[n][0] < minX:
    #         minX = node_pos[n][0]
    #     if node_pos[n][0] > maxX:
    #         maxX = node_pos[n][0]
    #     if node_pos[n][1] < minY:
    #         minY = node_pos[n][1]
    #     if node_pos[n][1] > maxY:
    #         maxY = node_pos[n][1]
    size = graph.get_min_max()
    minX = size[0]
    maxX = size[1]
    minY = size[2]
    maxY = size[3]
    for k, e in graph.get_allEdges().items():
        pygame.draw.line(window, BLUE, (((node_pos[e.src][0] - minX) / (maxX - minX)) * (WIDTH - 50) + 25,
                                        ((node_pos[e.src][1] - minY) / (maxY - minY)) * (HEIGHT - 150) + 100), (
                             ((node_pos[e.dest][0] - minX) / (maxX - minX)) * (WIDTH - 50) + 25,
                             ((node_pos[e.dest][1] - minY) / (maxY - minY)) * (HEIGHT - 150) + 100))
        newX = node_pos[e.dest][0] - ((node_pos[e.dest][0] - node_pos[e.src][0]) / 4)
        newY = node_pos[e.dest][1] - ((node_pos[e.dest][1] - node_pos[e.src][1]) / 4)
        weight_text = font.render("{:.3f}".format(e.weight), True, MAGENTA)
        window.blit(weight_text, (
            ((newX - minX) / (maxX - minX)) * (WIDTH - 50) + 25,
            ((newY - minY) / (maxY - minY)) * (HEIGHT - 150) + 100))

    for n in graph.nodes:
        if n == center_node:
            node_color = YELLOW
        else:
            node_color = RED
        if len(graph.nodes) == 1:
            pygame.draw.circle(window, node_color, (WIDTH // 2, HEIGHT // 2), RADIUS)
            id_text = font.render(str(n), True, GREEN)
            window.blit(id_text, (WIDTH // 2 - 5, HEIGHT // 2 - 11))
        else:
            pygame.draw.circle(window, node_color, (((node_pos[n][0] - minX) / (maxX - minX)) * (WIDTH - 50) + 25,
                                                    ((node_pos[n][1] - minY) / (maxY - minY)) * (HEIGHT - 150) + 100),
                               RADIUS)
            id_text = font.render(str(n), True, GREEN)
            window.blit(id_text, (((node_pos[n][0] - minX) / (maxX - minX)) * (WIDTH - 50) + 25 - 5,
                                  ((node_pos[n][1] - minY) / (maxY - minY)) * (HEIGHT - 150) + 100 - 11))
    pygame.display.update()


def run(ga: GraphAlgo):
    active = False
    user_text = ''
    text_box = 'WELCOME!'
    button_selected = 0
    center_node = -1
    node_pos = {n.id: (n.get_x(), n.get_y()) if n.get_x() and n.get_y() is not None else (
        random.uniform(35, 36), random.uniform(32, 33)) for
                n in ga.graph.nodes.values()}
    clock = pygame.time.Clock()
    run = True
    while run:
        window.fill(WHITE)

        button1 = pygame.Rect(0 * WIDTH // 9, 0, WIDTH // 9, 30)
        button2 = pygame.Rect(1 * WIDTH // 9, 0, WIDTH // 9, 30)
        button3 = pygame.Rect(2 * WIDTH // 9, 0, WIDTH // 9, 30)
        button4 = pygame.Rect(3 * WIDTH // 9, 0, WIDTH // 9, 30)
        button5 = pygame.Rect(4 * WIDTH // 9, 0, WIDTH // 9, 30)
        button6 = pygame.Rect(5 * WIDTH // 9, 0, WIDTH // 9, 30)
        button7 = pygame.Rect(6 * WIDTH // 9, 0, WIDTH // 9, 30)
        button8 = pygame.Rect(7 * WIDTH // 9, 0, WIDTH // 9, 30)
        button9 = pygame.Rect(8 * WIDTH // 9, 0, WIDTH // 9, 30)
        request_text_box = pygame.Rect(0, 30, WIDTH // 3 * 2, 30)
        request_input_box = pygame.Rect(WIDTH // 3 * 2, 30, WIDTH // 3, 30)

        pygame.draw.rect(window, GRAY, button1)
        pygame.draw.rect(window, DARK_GRAY, button1, 2)
        window.blit(font.render("Load", True, BLACK), (0 * WIDTH // 9 + WIDTH // 9 / 3, 5))
        pygame.draw.rect(window, GRAY, button2)
        pygame.draw.rect(window, DARK_GRAY, button2, 2)
        window.blit(font.render("Save", True, BLACK), (1 * WIDTH // 9 + WIDTH // 9 / 3, 5))
        pygame.draw.rect(window, GRAY, button3)
        pygame.draw.rect(window, DARK_GRAY, button3, 2)
        window.blit(font.render("Add Node", True, BLACK), (2 * WIDTH // 9 + WIDTH // 9 / 3 - 15, 5))
        pygame.draw.rect(window, GRAY, button4)
        pygame.draw.rect(window, DARK_GRAY, button4, 2)
        window.blit(font.render("Remove Node", True, BLACK), (3 * WIDTH // 9 + WIDTH // 9 / 3 - 25, 5))
        pygame.draw.rect(window, GRAY, button5)
        pygame.draw.rect(window, DARK_GRAY, button5, 2)
        window.blit(font.render("Add Edge", True, BLACK), (4 * WIDTH // 9 + WIDTH // 9 / 3 - 15, 5))
        pygame.draw.rect(window, GRAY, button6)
        pygame.draw.rect(window, DARK_GRAY, button6, 2)
        window.blit(font.render("Remove Edge", True, BLACK), (5 * WIDTH // 9 + WIDTH // 9 / 3 - 25, 5))
        pygame.draw.rect(window, GRAY, button7)
        pygame.draw.rect(window, DARK_GRAY, button7, 2)
        window.blit(font.render("Shortest Path", True, BLACK), (6 * WIDTH // 9 + WIDTH // 9 / 3 - 30, 5))
        pygame.draw.rect(window, GRAY, button8)
        pygame.draw.rect(window, DARK_GRAY, button8, 2)
        window.blit(font.render("Center Point", True, BLACK), (7 * WIDTH // 9 + WIDTH // 9 / 3 - 25, 5))
        pygame.draw.rect(window, GRAY, button9)
        pygame.draw.rect(window, DARK_GRAY, button9, 2)
        window.blit(font.render("TSP", True, BLACK), (8 * WIDTH // 9 + WIDTH // 9 / 3, 5))
        pygame.draw.rect(window, GRAY, request_text_box)
        pygame.draw.rect(window, DARK_GRAY, request_text_box, 2)
        window.blit(font.render(text_box, True, BLACK), (10, 35))
        pygame.draw.rect(window, WHITE, request_input_box)
        if active:
            pygame.draw.rect(window, RED, request_input_box, 2)
        else:
            pygame.draw.rect(window, DARK_GRAY, request_input_box, 2)
        window.blit(font.render(user_text, True, BLACK), (WIDTH // 3 * 2 + 10, 35))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button1.collidepoint(event.pos):
                    button_selected = 1
                    text_box = 'Enter Path of JSON to load:'
                    active = True
                elif button2.collidepoint(event.pos):
                    button_selected = 2
                    text_box = 'Enter Path of location to save this graph:'
                    active = True
                elif button3.collidepoint(event.pos):
                    button_selected = 3
                    text_box = "Enter id, x coordinate, y coordinate of Node to add with a separation of ',':"
                    active = True
                elif button4.collidepoint(event.pos):
                    button_selected = 4
                    text_box = 'Enter id of Node to remove:'
                    active = True
                elif button5.collidepoint(event.pos):
                    button_selected = 5
                    text_box = "Enter source, destination, weight of Edge to add with a separation of ',':"
                    active = True
                elif button6.collidepoint(event.pos):
                    button_selected = 6
                    text_box = "Enter source, destination of Edge to remove with a separation of ',':"
                    active = True
                elif button7.collidepoint(event.pos):
                    button_selected = 7
                    text_box = "Enter source Node id, destination Node id with a separation of ',':"
                    active = True
                elif button8.collidepoint(event.pos):
                    button_selected = 8
                elif button9.collidepoint(event.pos):
                    button_selected = 9
                    text_box = "Enter Node ids to be included in the cities list with a separation of ',':"
                    active = True
                else:
                    active = False
                    text_box = 'WELCOME!'
                    button_selected = 0
                    user_text = ''
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if button_selected == 1:
                            if ga.load_from_json(user_text):
                                text_box = 'LOADED'
                                node_pos = {n.id: (n.pos.x, n.pos.y) if n.pos is not None else (
                                    random.uniform(35, 36), random.uniform(32, 33)) for n in ga.graph.nodes.values()}
                                center_node = -1
                            else:
                                text_box = 'FAILED TO LOAD'
                        if button_selected == 2:
                            if ga.save_to_json(user_text):
                                text_box = 'SAVED'
                            else:
                                text_box = 'FAILED TO SAVE'
                        if button_selected == 3:
                            try:
                                info = user_text.split(',')
                                if len(info) == 3 and ga.graph.add_node(int(info[0]), (float(info[1]), float(info[2]))):
                                    node_pos[int(info[0])] = (float(info[1]), float(info[2]))
                                    text_box = 'NODE ADDED'
                                elif len(info) == 1 and ga.graph.add_node(int(info[0])):
                                    node_pos[int(info[0])] = (random.uniform(35, 36), random.uniform(32, 33))
                                    text_box = 'NODE ADDED'
                                else:
                                    text_box = 'INVALID INPUT!'
                            except:
                                text_box = 'INVALID INPUT!'
                        if button_selected == 4:
                            try:
                                if ga.graph.remove_node(int(user_text)):
                                    node_pos.pop(int(user_text))
                                    text_box = 'NODE REMOVED'
                                else:
                                    text_box = 'INVALID INPUT!'
                            except:
                                text_box = 'INVALID INPUT!'
                        if button_selected == 5:
                            try:
                                info = user_text.split(',')
                                if ga.graph.add_edge(int(info[0]), int(info[1]), float(info[2])):
                                    text_box = "EDGE ADDED"
                                else:
                                    text_box = 'INVALID INPUT!'
                            except:
                                text_box = 'INVALID INPUT!'
                        if button_selected == 6:
                            try:
                                info = user_text.split(',')
                                if ga.graph.remove_edge(int(info[0]), int(info[1])):
                                    text_box = "EDGE REMOVED"
                                else:
                                    text_box = 'INVALID INPUT!'
                            except:
                                text_box = 'INVALID INPUT!'
                        if button_selected == 7:
                            try:
                                info = user_text.split(',')
                                w, path = ga.shortest_path(int(info[0]), int(info[1]))
                                if w != float('inf'):
                                    text_box = f'Weight: {w}, Shortest Path: {path}'
                                else:
                                    text_box = f'There is no path between {int(info[0])} and {int(info[1])}'
                            except:
                                text_box = 'INVALID INPUT!'
                        if button_selected == 9:
                            try:
                                info = user_text.split(',')
                                cities = []
                                for id in info:
                                    cities.append(int(id))
                                path, w = ga.TSP(cities)
                                text_box = f'Weight: {w}, Shortest Path: {path}'
                            except:
                                text_box = 'INVALID INPUT!'
                        user_text = ''
                        active = False
                    else:
                        user_text += event.unicode
            if button_selected == 8:
                center, eccentricity = ga.centerPoint()
                if eccentricity != float('inf'):
                    text_box = f'Center Node id: {center}, Eccentricity: {eccentricity}'
                else:
                    text_box = 'There is no center Node because the graph is not connected'
                center_node = center
                user_text = ''
                active = False
        draw_window(ga.graph, center_node, node_pos)
        clock.tick(FPS)
