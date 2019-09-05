def Rotate(mag, dir):
    if dir == -1:
        temp = mag[0]
        del mag[0]
        mag.append(temp)

    if dir == 1:
        mag.insert(0, mag[7])
        del mag[8]

def Same(w, v, dir):
    x = mag[w - 1]
    y = mag[v - 1]
    if w < v:
        if x[2+dir] != y[6]:
            Rotate(y, -dir)
            return True
        else: return False
    else:
        if x[6+dir] != y[2]:
            Rotate(y, -dir)
            return True
        else: return False

N = int(input())
for i in range(N):
    rot_times = int(input())
    mag = [[x] for x in range(4)]
    mag[0] = list(map(int,input().split()))
    mag[1] = list(map(int,input().split()))
    mag[2] = list(map(int,input().split()))
    mag[3] = list(map(int,input().split()))
    for _ in range(rot_times):
        rot_n_mag, rot_dir = list(map(int, input().split()))
        rot_mag = mag[rot_n_mag - 1]
        Rotate(rot_mag, rot_dir)
        if rot_mag == mag[0]:
            if Same(1, 2, rot_dir):
                if Same(2, 3, -rot_dir):
                    Same(3, 4, rot_dir)
        elif rot_mag == mag[1]:
            Same(2, 1, rot_dir)
            if Same(2, 3, rot_dir):
                Same(3, 4, -rot_dir)
        elif rot_mag == mag[2]:
            Same(3, 4, rot_dir)
            if Same(3, 2, rot_dir):
                Same(2, 1, -rot_dir)
        elif rot_mag == mag[3]:
            if Same(4, 3, rot_dir):
                if Same(3, 2, -rot_dir):
                    Same(2, 1, rot_dir)
    print('#%d %d' %(i+1, mag[0][0] + 2 * mag[1][0] + 4 * mag[2][0] + 8 * mag[3][0]))