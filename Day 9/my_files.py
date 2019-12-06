def main():

    # WRITE FILE
    # file = open("sample.txt" , "W+")

    # for i in range(20):
    #     file.write("I learn python %d \n" %(i))
    # file.close()

#   READ FILE
    # file = open("sample.txt" , "r")
    # if file.mode == "r":
    #     fileC = file.read()
    #     print(fileC)

# FILE EXCEPTIONS
    try:
        file = open("sampl.txt" , "r")
        print("Sucssecsfully done")
    except IOError:
        print("Files does not exit")

    print("done")

if __name__ == "__main__":
    main()