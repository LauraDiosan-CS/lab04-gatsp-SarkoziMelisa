import ga
import greedy


def inputScan(fileName):
    d = {}
    f = open(fileName, "r")
    line = f.readline().strip()
    d["n"] = int(line)
    matrix = []
    for i in range(d["n"]):
        line = f.readline().strip()
        nrs = []
        for nr in line.split(" "):
            nrs.append(int(nr))
        matrix.append(nrs)
    d["matrix"] = matrix
    line = f.readline().strip()
    d["startNode"] = int(line)
    return d


def printOutput(drumMinim, traseu):
    print("Drumul minim determinat este ", drumMinim)
    st = "\nTraseul este: "
    for x in traseu:
        st += str(x) + " "
    st += str(traseu[0])
    print(st)


def run():
    fileName = input("Dati numele fisierului cu datele de intrare: ")
    d = inputScan(fileName)
    print("Introduceti algoritmul dorit pentru rezolvarea problemei:\n\t1 - Greedy\n\t2 - Algoritmi evolutivi")
    alg = int(input())
    if alg == 1:
        drumMinim, traseu = greedy.drumMinimGreedy(d["startNode"] - 1, d["startNode"] - 1, d["matrix"], d["n"])
        printOutput(drumMinim, traseu)
    elif alg == 2:
        d["dimensiunePopulatie"] = 15
        d["nrIteratii"] = 500
        # drumMinim, visited = ga.mainGA(d)
        # printOutput(drumMinim, visited)
        traseu, drumMinim = ga.mainGA(d)
        printOutput(drumMinim, traseu)


run()
