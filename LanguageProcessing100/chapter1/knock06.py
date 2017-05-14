from knock05 import create_ngram

if __name__ == "__main__":
    # character bigram of "paraparaparadise"
    X = set(create_ngram("paraparaparadise", 2))
    print(X)
    
    # character bigram of "paragraph"
    Y = set(create_ngram("paragraph", 2))
    print(Y)

    # union of X and Y
    print(X | Y)

    # intersection of X and Y
    print(X & Y)

    # difference set of X and Y
    print(X - Y)

    # whether "se" is included in set X
    print("se" in X)

    # whether "se" is included in set Y
    print("se" in Y)
