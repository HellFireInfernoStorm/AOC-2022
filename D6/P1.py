with open('input.txt') as f:
    dataStream = f.read().strip()

n = len(dataStream)
for i in range(n-3):
    data_buffer = set(dataStream[i:i+4])
    if len(data_buffer) == 4:
        print(i+4)
        break