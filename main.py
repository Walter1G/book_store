def main():
    try:
       #initialize empty list
       booksList=[]
       
       infile=open("theBooksList.txt","r")
       line=infile.readline()
       while line:
           booksList.append(line.rstrip("\n").split(","))
           line=infile.readline()
       infile.close()
    except FileNotFoundError:
        print("the <Bookslist.txt> file is not found")
        print("starting a new Books List")
        booksList=[]
        
        
    choice=0
    print("*** Books Manager  ***")
    while choice!=4:          
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display a book")
        print("4) Quit")   
        choice= int(input())
        
        if choice==1:
            print("Add a book....")
            nbook=input("Enter the name of the book >>> ")
            nAuthor=input("Enter the name of the Author >>> ")
            npages=input("Enter the number of pages >>> ")        
            booksList.append([nbook,nAuthor,npages])
            print("Added successfully...")
        elif choice==2:
            print("Looking up for a book...")
            print(f"Booklist has {len(booksList)} records")
            keyword=input("Enter Search Term: ")
            for book in booksList:
                if keyword in book:
                    print(book)
        elif choice==3:
            print("Displaying all books")
            print(f"Booklist has {len(booksList)} records")
            print("")
            print("")
            print("----------------------------------------------------------")
            
            for i in range(len(booksList)):
                print(booksList[i])
        elif choice==4:
            print("Quiting Program")
    print("Program Terminated!")
    
    #Saving to external TXT file
    outfile=open("theBooksList.txt","w")
    for book in booksList:
        outfile.write(",".join(book)+ "\n")
    
    outfile.close()
    
        
    
    
if __name__=="__main__":
    main()