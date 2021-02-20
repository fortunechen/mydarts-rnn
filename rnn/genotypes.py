from collections import namedtuple

Genotype = namedtuple('Genotype', 'recurrent concat')

PRIMITIVES = [
    'none',
    'tanh',
    'relu',
    'sigmoid',
    'identity'
]
STEPS = 8
CONCAT = 8

ENAS = Genotype(
    recurrent = [
        ('tanh', 0),
        ('tanh', 1),
        ('relu', 1),
        ('tanh', 3),
        ('tanh', 3),
        ('relu', 3),
        ('relu', 4),
        ('relu', 7),
        ('relu', 8),
        ('relu', 8),
        ('relu', 8),
    ],
    concat = [2, 5, 6, 9, 10, 11]
)

DARTS_V1 = Genotype(recurrent=[('relu', 0), ('relu', 1), ('tanh', 2), ('relu', 3), ('relu', 4), ('identity', 1), ('relu', 5), ('relu', 1)], concat=range(1, 9))
DARTS_V2 = Genotype(recurrent=[('sigmoid', 0), ('relu', 1), ('relu', 1), ('identity', 1), ('tanh', 2), ('sigmoid', 5), ('tanh', 3), ('relu', 5)], concat=range(1, 9))

DARTS = DARTS_V2

s1_1 = Genotype(recurrent=[('relu', 0), ('sigmoid', 1), ('relu', 2), ('tanh', 0), ('identity', 4), ('sigmoid', 4), ('sigmoid', 5), ('tanh', 3)], concat=range(1, 9))
s1_2 = Genotype(recurrent=[('tanh', 0), ('tanh', 0), ('identity', 0), ('sigmoid', 2), ('identity', 4), ('identity', 5), ('identity', 6), ('identity', 7)], concat=range(1, 9))
s1_3 = Genotype(recurrent=[('tanh', 0), ('tanh', 0), ('identity', 2), ('sigmoid', 2), ('identity', 4), ('identity', 5), ('identity', 6), ('identity', 7)], concat=range(1, 9))

s2_1 = Genotype(recurrent=[('relu', 0), ('relu', 1), ('sigmoid', 2), ('identity', 1), ('relu', 2), ('relu', 1), ('identity', 2), ('tanh', 3)], concat=range(1, 9))
s2_2 = Genotype(recurrent=[('relu', 0), ('relu', 1), ('identity', 1), ('identity', 1), ('relu', 2), ('identity', 1), ('tanh', 4), ('identity', 4)], concat=range(1, 9))
# s2_3 = Genotype(recurrent=[('relu', 0), ('relu', 1), ('identity', 1), ('identity', 1), ('relu', 2), ('identity', 1), ('tanh', 4), ('identity', 4)], concat=range(1, 9))


s3_1 = Genotype(recurrent=[('identity', 0), ('relu', 1), ('identity', 0), ('identity', 2), ('sigmoid', 4), ('tanh', 0), ('sigmoid', 1), ('identity', 6)], concat=range(1, 9))
s3_2 = Genotype(recurrent=[('relu', 0), ('identity', 1), ('identity', 0), ('identity', 3), ('identity', 0), ('identity', 4), ('identity', 1), ('relu', 4)], concat=range(1, 9))
s3_3 = Genotype(recurrent=[('relu', 0), ('relu', 1), ('identity', 0), ('identity', 0), ('tanh', 1), ('identity', 1), ('identity', 1), ('relu', 4)], concat=range(1, 9))


s4_1 = Genotype(recurrent=[('sigmoid', 0), ('tanh', 0), ('relu', 0), ('tanh', 2), ('sigmoid', 2), ('relu', 2), ('tanh', 4), ('relu', 0)], concat=range(1, 9))
s4_2 = Genotype(recurrent=[('identity', 0), ('identity', 1), ('relu', 2), ('identity', 3), ('relu', 3), ('identity', 3), ('identity', 0), ('identity', 3)], concat=range(1, 9))
s4_3 = Genotype(recurrent=[('identity', 0), ('identity', 1), ('relu', 2), ('tanh', 0), ('relu', 3), ('identity', 3), ('identity', 0), ('identity', 0)], concat=range(1, 9))

