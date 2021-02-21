def sing(): 
    song = []
    for i in range(99, 0, -1) :
        j = i - 1
        if i > 1 :
            song.append(f"{i} bottles of beer on the wall, {i} bottles of beer."
            song.append(f"Take one down and pass it around, {j} bottles of beer on the wall.")
        elif i < 2 and i > 0 :
            song.append(f"{i} bottles of beer on the wall, {i} bottles of beer."
            song.append("Take one down and pass it around, no more bottles of beer on the wall.")
        else : 
            song.append(f"{i} bottles of beer on the wall, {i} bottles of beer."
            song.append("Take one down and pass it around, no more bottles of beer on the wall.")
            song.append("Go to the store and buy some more, 99 bottles of beer on the wall.")
    return song
            
        
