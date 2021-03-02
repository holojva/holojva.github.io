import pickle

inp = input("Your aaaaa file... ")
with open(f"{inp}.aaaaa", "r") as lf :
   load_data = lf.read()
code = load_data.split()
isitvalid = list(load_data)
for i in isitvalid :
    if i in """qwertyuiop[]sdfghjkl'\zxcvbnm,./z1234567890-=!@#$%^&*()_+QWERTYUIOP{}ASDFGHJKL:"|ZXCVBNM<>?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЁЯЧСМИТЬБЮ?><"№%:,.;±§""" :
        print("Not_a_Error: it is another letter!")
word = 0
for i in range(1000000) :
    if word > len(code) - 1 :
        break
    if len(code[word]) == 1 :
        with open(f"{len(code[word - 1])}.dat", "wb") as sf :
            if code[word + 1] != "aaa" :
                pickle.dump(code[word + 1], sf)
            else :
                ifon = []
                for i in range(100) :
                    if len(code[word + 2 + i]) != 3 :
                        ifon.append(code[word + 2 + i])
                    else :
                        pickle.dump(" ".join(ifon), sf)
                        break
                    

    elif len(code[word]) == 2 :
        with open(f"{code[word + 1]}.dat", "rb") as lf :
            print(pickle.load(lf))
    word += 1

