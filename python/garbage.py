import sys, gc

def make_cycle():
1 = { }
1[0] = 1

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
