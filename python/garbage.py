import sys, gc

def make_cycle():
    x = { }
    x[0] = x    

def main():
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)
    
    print "Creating cycles..."
    for i in range(10):
        make_cycle()
    collected = gc.collect()
    print "Garbage collector: collected %d objects." % (collected)

if __name__ == "__main__":
    ret = main()
    sys.exit(ret)
