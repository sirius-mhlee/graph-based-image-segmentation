import sys
import cv2
import random as rand

import numpy as np

import GraphOperator as go

def generate_image(ufset, width, height):
    random_color = lambda: (int(rand.random() * 255), int(rand.random() * 255), int(rand.random() * 255))
    color = [random_color() for i in range(width * height)]

    save_img = np.zeros((height, width, 3), np.uint8)

    for y in range(height):
        for x in range(width):
            color_idx = ufset.find(y * width + x)
            save_img[y, x] = color[color_idx]

    return save_img

def main():
    sigma = float(sys.argv[1])
    k = float(sys.argv[2])
    min_size = float(sys.argv[3])

    img = cv2.imread(sys.argv[4])
    float_img = np.asarray(img, dtype=float)

    gaussian_img = cv2.GaussianBlur(float_img, (5, 5), sigma)
    b, g, r = cv2.split(gaussian_img)
    smooth_img = (r, g, b)

    height, width, channel = img.shape
    graph = go.build_graph(smooth_img, width, height)

    weight = lambda edge: edge[2]
    sorted_graph = sorted(graph, key=weight)

    ufset = go.segment_graph(sorted_graph, width * height, k)
    ufset = go.remove_small_component(ufset, sorted_graph, min_size)

    save_img = generate_image(ufset, width, height)
    cv2.imwrite(sys.argv[5], save_img)

if __name__ == '__main__':
    main()
