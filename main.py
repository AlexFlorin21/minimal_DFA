class DFA:
    def __init__(self, stari, alfabet, tranzitii, stare_start, stari_de_iesire):
        self.stari = stari
        self.alfabet = alfabet
        self.tranzitii = tranzitii
        self.stare_start = stare_start
        self.stari_de_iesire = stari_de_iesire

def min_dfa(dfa):
    def partitii(P, T):
        r= []
        for p in P:
            split = {}
            for stare in p:
                key = tuple(T[stare][char] in p for char in dfa.alfabet)
                if key not in split:
                    split[key] = []
                split[key].append(stare)
            r.extend(split.values())
        return r

    P = [set(dfa.stari_de_iesire), dfa.stari - set(dfa.stari_de_iesire)]
    T = {stare: {char: dfa.tranzitii[stare][char] for char in dfa.alfabet} for stare in dfa.stari}
    while True:
        new_P = partitii(P, T)
        if len(new_P) == len(P):
            break
        P = new_P

    stare_m = {stare: i for i, partition in enumerate(P) for stare in partition}
    new_stari = set(stare_m.values())
    new_alfabet = dfa.alfabet
    new_tranzitii = {stare: {char: stare_m[T[stare][char]] for char in new_alfabet} for stare in new_stari}
    new_stare_start = stare_m[dfa.stare_start]
    new_stari_de_iesire = {stare_m[stare] for stare in dfa.stari_de_iesire}

    return DFA(new_stari, new_alfabet, new_tranzitii, new_stare_start, new_stari_de_iesire)

def print_dfa(dfa):
    print(f"States: {dfa.stari}")
    print(f"Alphabet: {dfa.alfabet}")
    print(f"Transition function:")
    for stare in dfa.stari:
        for char in dfa.alfabet:
            print(f"  {stare} --{char}--> {dfa.tranzitii[stare][char]}")
    print(f"Start state: {dfa.stare_start}")
    print(f"Accept states: {dfa.stari_de_iesire}")

# Exemplu de automat finit determinist (DFA):
stari = {0, 1, 2, 3}
alfabet = {'a', 'b'}
tranzitii = {
    0: {'a': 1, 'b': 0},
    1: {'a': 2, 'b': 0},
    2: {'a': 2, 'b': 3},
    3: {'a': 2, 'b': 0},
}
stare_start = 0
stari_de_iesire = {2, 3}

dfa = DFA(stari, alfabet, tranzitii, stare_start, stari_de_iesire)
print("DFA initial:")
print_dfa(dfa)

min_dfa = min_dfa(dfa)
print("\nDFA minimal:")
print_dfa(min_dfa)


