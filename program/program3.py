text = [1,2,3,4]

it = iter(text)

while True:
    try :
        print(list(it))
        print(next(it))

    except StopIteration:
        break


