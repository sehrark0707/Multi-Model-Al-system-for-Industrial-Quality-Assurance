import numpy as np

def apply_convolution(input_matrix, filter_weights, step=1):
    mat_h, mat_w = input_matrix.shape
    f_h, f_w = filter_weights.shape
    out_h = (mat_h - f_h) // step + 1
    out_w = (mat_w - f_w) // step + 1
    output_map = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            row_start = i * step
            col_start = j * step
            region = input_matrix[row_start:row_start + f_h, col_start:col_start + f_w]
            output_map[i, j] = np.sum(region * filter_weights)
    return output_map

def apply_max_pooling(activation_map, size=2, step=2):
    act_h, act_w = activation_map.shape
    out_h = (act_h - size) // step + 1
    out_w = (act_w - size) // step + 1
    pooled_map = np.zeros((out_h, out_w))

    for i in range(out_h):
        for j in range(out_w):
            row_start = i * step
            col_start = j * step
            region = activation_map[row_start:row_start + size, col_start:col_start + size]
            pooled_map[i, j] = np.max(region)
    return pooled_map

def apply_relu(matrix):
    return np.maximum(0, matrix)

if __name__ == "__main__":
    data_grid = np.array([
        [0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 0],
        [0, 2, 2, 2, 2, 2, 0],
        [0, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 5, 5, 5, 5, 5, 0],
        [0, 5, 5, 5, 5, 5, 0]
    ])

    horizontal_filter = np.array([
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ])

    print("--- Input Grid ---")
    print(data_grid)

    conv_result = apply_convolution(data_grid, horizontal_filter)
    print("\n--- After Convolution (Horizontal Edge) ---")
    print(conv_result)

    relu_result = apply_relu(conv_result)
    print("\n--- After ReLU ---")
    print(relu_result)

    pooled_result = apply_max_pooling(relu_result, size=2, step=2)
    print("\n--- After Max Pooling (2x2) ---")
    print(pooled_result)

    print("\nGrid shape:", data_grid.shape)
    print("Conv output shape:", conv_result.shape)
    print("Pooled output shape:", pooled_result.shape)
