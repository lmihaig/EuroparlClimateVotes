with open("train.csv", "r") as f:
    print(f.readline())
    data=f.read()
data=data.split("\n")

def do_skip(line):
    if "Agenda of " in line:
        return True
    return False

print(len(data))
data=[line for line in data if not do_skip(line)]
print(len(data))
data1, data2=data[:len(data)//2], data[len(data)//2:]
print(len(data1))
print(len(data2))

data1="\n".join(data1)
data2="\n".join(data2)

with open("train1.csv", "w") as f:
    f.write("name,\n")
    f.write(data1)

with open("train2.csv", "w") as f:
    f.write("name,\n")
    f.write(data2)
