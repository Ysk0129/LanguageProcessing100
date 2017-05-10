from functools import reduce

if __name__ == "__main__":
    police_car = "パトカー"
    taxi = "タクシー"
    answer = "".join(reduce(lambda x,y: x+y,zip(police_car, taxi)))

    print(answer)
