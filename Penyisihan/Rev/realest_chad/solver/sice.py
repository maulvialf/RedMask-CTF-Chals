val = [84, 102, 134, 12, 47, 198, 230, 174, 234, 152, 70, 20, 245, 24, 125, 10, 42, 99, 192, 83, 31, 114, 252, 7, 80, 119, 204, 34, 187, 4, 136, 66]
pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16]

val_ = [187, 119, 198, 42, 192, 31, 24, 252, 99, 84, 234, 102, 12, 134, 20, 152, 136, 204, 245, 125, 34, 70, 66, 80, 174, 47, 10, 4, 7, 114, 230, 83]
pos_ = [19, 22, 5, 31, 29, 27, 13, 25, 30, 0, 8, 1, 3, 2, 11, 9, 17, 21, 12, 14, 20, 10, 16, 23, 7, 4, 15, 18, 24, 26, 6, 28]

for i in range(32):
    k = pos_.index(pos[i])
    pos_[i], pos_[k] = pos_[k], pos_[i]
    val_[i], val_[k] = val_[k], val_[i]

print(pos_)
print(val_ == val)

from pwn import xor
what = xor(b"chad_breaking_into_real_mode___}", val)

print([i for i in what])
