from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError('empty string is not valid path')

    path_name = []

    if path[0] == '/':
        path_name.append('/')

    for token in (token for token in path.split('/') if token not in ['.', '']):
        if token == '..':
            if not path_name or path_name[-1] == '..':
                path_name.append(token)
            else:
                if path_name[-1] == '/':
                    raise ValueError('Path Error')
                path_name.pop()
        else:
            path_name.append(token)

    result = '/'.join(path_name)
    return result[result.startswith('//'):  ]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
