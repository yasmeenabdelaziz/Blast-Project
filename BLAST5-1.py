# -- coding: utf-8 --
"""Bio-Blast.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pz24Rnq4RYeO3uur0KqyH4277cAHn0W4
"""

# -- coding: utf-8 --
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pz24Rnq4RYeO3uur0KqyH4277cAHn0W4
"""

blosum62 = {
    'C': {'C': 9, 'S': -1, 'T': -1, 'P': -3, 'A': 0, 'G': -3, 'N': -3, 'D': -3, 'E': -4, 'Q': -3, 'H': -3, 'R': -3,
          'K': -3, 'M': -1, 'I': -1, 'L': -1, 'V': -1, 'F': -2, 'Y': -2, 'W': -2},
    'S': {'C': -1, 'S': 4, 'T': 1, 'P': -1, 'A': 1, 'G': 0, 'N': 1, 'D': 0, 'E': 0, 'Q': 0, 'H': -1, 'R': -1, 'K': 0,
          'M': -1, 'I': -2, 'L': -2, 'V': -2, 'F': -2, 'Y': -2, 'W': -3},
    'T': {'C': -1, 'S': 1, 'T': 4, 'P': 1, 'A': -1, 'G': 1, 'N': 0, 'D': 1, 'E': 0, 'Q': 0, 'H': 0, 'R': -1, 'K': 0,
          'M': -1, 'I': -2, 'L': -2, 'V': -2, 'F': -2, 'Y': -2, 'W': -3},
    'P': {'C': -3, 'S': -1, 'T': 1, 'P': 7, 'A': -1, 'G': -2, 'N': -1, 'D': -1, 'E': -1, 'Q': -1, 'H': -2, 'R': -2,
          'K': -1, 'M': -2, 'I': -3, 'L': -3, 'V': -2, 'F': -4, 'Y': -3, 'W': -4},
    'A': {'C': 0, 'S': 1, 'T': -1, 'P': -1, 'A': 4, 'G': 0, 'N': -1, 'D': -2, 'E': -1, 'Q': -1, 'H': -2, 'R': -1,
          'K': -1, 'M': -1, 'I': -1, 'L': -1, 'V': -2, 'F': -2, 'Y': -2, 'W': -3},
    'G': {'C': -3, 'S': 0, 'T': 1, 'P': -2, 'A': 0, 'G': 6, 'N': -2, 'D': -1, 'E': -2, 'Q': -2, 'H': -2, 'R': -2,
          'K': -2, 'M': -3, 'I': -4, 'L': -4, 'V': 0, 'F': -3, 'Y': -3, 'W': -2},
    'N': {'C': -3, 'S': 1, 'T': 0, 'P': -2, 'A': -2, 'G': 0, 'N': 6, 'D': 1, 'E': 0, 'Q': 0, 'H': -1, 'R': 0, 'K': 0,
          'M': -2, 'I': -3, 'L': -3, 'V': -3, 'F': -3, 'Y': -2, 'W': -4},
    'D': {'C': -3, 'S': 0, 'T': 1, 'P': -1, 'A': -2, 'G': -1, 'N': 1, 'D': 6, 'E': 2, 'Q': 0, 'H': -1, 'R': -2, 'K': -1,
          'M': -3, 'I': -3, 'L': -4, 'V': -3, 'F': -3, 'Y': -3, 'W': -4},
    'E': {'C': -4, 'S': 0, 'T': 0, 'P': -1, 'A': -1, 'G': -2, 'N': 0, 'D': 2, 'E': 5, 'Q': 2, 'H': 0, 'R': 0, 'K': 1,
          'M': -2, 'I': -3, 'L': -3, 'V': -3, 'F': -3, 'Y': -2, 'W': -3},
    'Q': {'C': -3, 'S': 0, 'T': 0, 'P': -1, 'A': -1, 'G': -2, 'N': 0, 'D': 0, 'E': 2, 'Q': 5, 'H': 0, 'R': 1, 'K': 1,
          'M': 0, 'I': -3, 'L': -2, 'V': -2, 'F': -3, 'Y': -1, 'W': -2},
    'H': {'C': -3, 'S': -1, 'T': 0, 'P': -2, 'A': -2, 'G': -2, 'N': 1, 'D': 1, 'E': 0, 'Q': 0, 'H': 8, 'R': 0, 'K': -1,
          'M': -2, 'I': -3, 'L': -3, 'V': -2, 'F': -1, 'Y': 2, 'W': -2},
    'R': {'C': -3, 'S': -1, 'T': -1, 'P': -2, 'A': -1, 'G': -2, 'N': 0, 'D': -2, 'E': 0, 'Q': 1, 'H': 0, 'R': 5, 'K': 2,
          'M': -1, 'I': -3, 'L': -2, 'V': -3, 'F': -3, 'Y': -2, 'W': -3},
    'K': {'C': -3, 'S': 0, 'T': 0, 'P': -1, 'A': -1, 'G': -2, 'N': 0, 'D': -1, 'E': 1, 'Q': 1, 'H': -1, 'R': 2, 'K': 5,
          'M': -1, 'I': -3, 'L': -2, 'V': -3, 'F': -3, 'Y': -2, 'W': -3},
    'M': {'C': -1, 'S': -1, 'T': -1, 'P': -2, 'A': -1, 'G': -3, 'N': -2, 'D': -3, 'E': -2, 'Q': 0, 'H': -2, 'R': -1,
          'K': -1, 'M': 5, 'I': 1, 'L': 2, 'V': -2, 'F': 0, 'Y': -1, 'W': -1},
    'I': {'C': -1, 'S': -2, 'T': -2, 'P': -3, 'A': -1, 'G': -4, 'N': -3, 'D': -3, 'E': -3, 'Q': -3, 'H': -3, 'R': -3,
          'K': -3, 'M': 1, 'I': 4, 'L': 2, 'V': 1, 'F': 0, 'Y': -1, 'W': -3},
    'L': {'C': -1, 'S': -2, 'T': -2, 'P': -3, 'A': -1, 'G': -4, 'N': -3, 'D': -4, 'E': -3, 'Q': -2, 'H': -3, 'R': -2,
          'K': -2, 'M': 2, 'I': 2, 'L': 4, 'V': 3, 'F': 0, 'Y': -1, 'W': -2},
    'V': {'C': -1, 'S': -2, 'T': -2, 'P': -2, 'A': 0, 'G': -3, 'N': -3, 'D': -3, 'E': -2, 'Q': -2, 'H': -3, 'R': -3,
          'K': -2, 'M': 1, 'I': 3, 'L': 1, 'V': 4, 'F': -1, 'Y': -1, 'W': -3},
    'F': {'C': -2, 'S': -2, 'T': -2, 'P': -4, 'A': -2, 'G': -3, 'N': -3, 'D': -3, 'E': -3, 'Q': -3, 'H': -1, 'R': -3,
          'K': -3, 'M': 0, 'I': 0, 'L': 0, 'V': -1, 'F': 6, 'Y': 3, 'W': 1},
    'Y': {'C': -2, 'S': -2, 'T': -2, 'P': -3, 'A': -2, 'G': -3, 'N': -2, 'D': -3, 'E': -2, 'Q': -1, 'H': 2, 'R': -2,
          'K': -2, 'M': -1, 'I': -1, 'L': -1, 'V': -1, 'F': 3, 'Y': 7, 'W': 2},
    'W': {'C': -2, 'S': -3, 'T': -3, 'P': -4, 'A': -3, 'G': -2, 'N': -4, 'D': -4, 'E': -3, 'Q': -2, 'H': -2, 'R': -3,
          'K': -3, 'M': -1, 'I': -3, 'L': -2, 'V': -3, 'F': 1, 'Y': 2, 'W': 11}
}


# 1st step
def Database(filename):
    file = open(filename)  # create text file for the database
    DB = []  # list of database
    for line in file:
        DB.append(line.rstrip())  # strings in python are immutable , meaning that they can not be modified
    file.close()
    return DB


# one sequence in one line
def Query(filename):
    file = open(filename)
    Seq = (file.read())
    file.close()
    return Seq


def GetWords(seq):
    Words = []  # list to store words after splitting the sequence
    for i in range(len(seq)):
        if len(seq[i:i + 3]) < 3:
            continue
        else:
            Words.append(seq[i:i + 3])
    return Words


def GetNeighborhood(Words, T):
    amino_acids = ['C', 'S', 'T', 'P', 'A', 'G', 'N', 'D', 'E', 'Q', 'H', 'R', 'K', 'M', 'I', 'L', 'V', 'F', 'Y', 'W']
    Neighborhood = []  # list to store the 60 possible for each word
    Seeds = {}  # list to store the words that have score > threshold value
    seed_list = []

    for x in range(len(Words)):  # x -> index of words
        for y in range(len(Words[x])):  # y -> index of each letter in the word
            for z in range(len(amino_acids)):  # z-> index of letters in the list (each amino acid)
                score = 0
                prob = Words[x].replace(Words[x][y], amino_acids[z])  # variable to store each possible word
                if len(prob) == 3 and prob not in Neighborhood:  # condition to check words are not repeated in neighborhood
                    for i in range(len(prob)):
                        score += blosum62[prob[i]][Words[x][i]]  # calculate score for each word with it's neighborhood
                    # print("word",Words[i],"probalities of words",prob,"score",score)
                    Neighborhood.append(prob)
                    if score >= T:
                        Seeds[Words[x]] = score
                        seed_list.append((Words[x]))
                        # print(seed_list)
    filtered_seed_list = list(dict.fromkeys(seed_list))
    return Seeds, filtered_seed_list

def Hit (Seeds , DB) :
    Hit = []
    for x in range(len(Seeds)):
        for i in range(len(Db)):
            if Seeds[x] == Db [i : i+3] :
                Hit = Seeds[x]
    return Hit


def extedn(DB, Hit, Words, Seq , threShold):
    left_score = 10
    prev_left_score = 0
    prev_right_score = 0
    right_score = 0
    g = 0
    HSP = []
    newHSP = []
    j = 0
    mm = 2
    seq_right_extend = ""
    right_extend=""
    seq_left_extend=""
    left_extend =""

    for x in range(len(list_seed)):
        for i in range(len(Db)):
          for n in range(len(DB[i])):
            if Hit[x]  != Db[i] [n : j+3] :
              j = n
              continue
            elif Hit[x] == Db[i][n : j+3] and j+3 != len(Db[i]):
                 j = n
                right_extend = Db[i] [j+4]
                left_extend = Db[i][n-1]
                for i in range(len(Seq)):
                   if Hit[x] != Seq[ i : mm +1 ] :
                     mm += 1
                   elif Hit[x] == Seq[ i : mm+1 ] and mm+1 < len(Seq) :
                      seq_left_extend += Seq[i-1 ]
                      seq_right_extend += Seq[mm+2]
                      prev_left_score = left_score
                      prev_right_score = right_score
                      right_score += blosum62[right_extend][seq_right_extend]
                      left_score += blosum62[left_extend][seq_left_extend]
                      if right_score < prev_right_score:
                         HSP.append(prev_right_score)
                         if left_score < prev_left_score:
                           HSP.append(prev_left_score)

    for i in range(len(HSP)) :
      if HSP[i]> threShold :
        newHSP[g] = HSP[i]

    print("the final HSP : " , HSP)


Db = Database("ProteinDatabase.txt")
Seq = Query("Protein.txt")
Words = GetWords(Seq)
hit=Hit(list_seed,Db)
dic_seed, list_seed = GetNeighborhood(Words, 13)
HSPcheck = extedn(Db, list_seed, Words, Seq,6)
# print(dic_seed)
#print("the final HSP : " , HSPcheck)
print (list_seed)
print(Hit)
print(Db)
print(Seq)
print("Words : ",Words)
print("Neighbours :",neighborhood)
print(len(neighborhood))
