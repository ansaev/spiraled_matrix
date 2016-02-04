import pytest
from random import randint as rand
from main import spiraled_matrix_representative


class Tests:
    @pytest.fixture(params=[
        # matrix 1x1
        {'data': [1, 1], "answer": [[0, 0]]},
        # matrix 3x3
        {'data': [3, 3], "answer": [[1, 1], [1, 0], [0, 0], [0, 1], [0, 2], [1, 2], [2, 2], [2, 1], [2, 0]]},
        # matrix 5x5
        {'data': [5, 5], "answer": [
            [2, 2], [2, 1], [1, 1], [1, 2], [1, 3], [2, 3], [3, 3], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0],
            [0, 1], [0, 2], [0, 3], [0, 4], [1, 4], [2, 4], [3, 4], [4, 4], [4, 3], [4, 2], [4, 1], [4, 0]
        ]},
    ])
    def matrix(self, request):
        left_side = 1
        right_side = 10
        dims = request.param['data']
        # init matrix with random int numbers between left_side and right_side
        matrix_rez = [[rand(left_side, right_side) for j in xrange(dims[1])] for i in xrange(dims[0])]
        request.param['data'] = matrix_rez
        return request.param

    def test_spir(self, matrix):
        rez = spiraled_matrix_representative(matrix['data'])
        assert rez == matrix["answer"]
