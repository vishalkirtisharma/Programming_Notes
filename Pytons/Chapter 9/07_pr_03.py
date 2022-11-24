def tables(n):
    file= open("table.txt","w")
    for i in range(1,n+1):
        file.write(f"{n} * {i} = {n*i} \n")
    file.close()


tables(10)