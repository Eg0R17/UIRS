def task(w,n,c):
    if (w=="Monday"):
        name = "James"
        c=n*c
    elif (w=="Tuesday"):
        name = "John"
        c=n*c
    elif (w=="Wednesday"):
        name = "Robert"
        c=n*c
    elif (w=="Thursday"):
        name = "Michael"
        c=n*c
    elif (w=="Friday"):
        name = "William"
        c=n*c
    return ('It is {} today, {}, you have to work, you must spray {} trees and you need {} dollars to buy liquid'.format(w,name,n,c))