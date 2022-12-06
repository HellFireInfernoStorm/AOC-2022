with open('input.txt') as f:
    dataStream = f.read().strip()

n = len(dataStream)
for i in range(n-13):
    data_buffer = set(dataStream[i:i+14])
    if len(data_buffer) == 14:
        print(i+14)
        break