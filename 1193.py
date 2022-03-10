N = int(input())
seq = 0
count = 0
while N > seq:
    count += 1
    seq += count
seq -= count
whole = count +1

if count % 2:
    top = whole -(N-seq)
    bot = (N-seq)
else:
    bot = whole -(N-seq)
    top = (N-seq)

print(f'{top}/{bot}')