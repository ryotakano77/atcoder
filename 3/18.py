import math

T = int(input())
L, X, Y = tuple(map(int, input().split()))
B = (X, Y, 0)
R = L / 2
Q = int(input())
q = []
for _ in range(Q):
    q.append(int(input()))

def get_angle(t):
    theta = -((t / T) * 2 * math.pi) - (math.pi * (1 / 2))
    return theta

def get_vector(angle):
    dy = R * math.cos(angle)
    dz = R * math.sin(angle)
    return 0, dy, dz

def get_position(vector):
    y = vector[1]
    z = R + vector[2]
    return 0, y, z

def calc_procudt(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def calc_abs(a):
    return math.sqrt(a[0]**2 + a[1]**2 + a[2]**2)

def calc_dist(a, b):
    diff_vec = (a[0]-b[0], a[1]-b[1], a[2]-b[2])
    return calc_abs(diff_vec)

def calc_cos(a, b):
    return calc_procudt(a, b) / (calc_abs(a) * calc_abs(b))

for t in q:
    angle = get_angle(t)
    vector = get_vector(angle)
    A = get_position(vector)
    dist = calc_dist(A, B)
    sin = A[2] / dist
    # print(f"t:{t} vec:{vector} A: {A}")
    print(math.degrees(math.asin(sin)))