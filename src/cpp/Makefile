## binomial.make
#

main:		main.o Binomial.o
			g++ -o main main.o Binomial.o

main.o:	    main.cpp Binomial.cpp
	        g++ -c main.cpp

test:		test.o Binomial.o
			g++ -o test test.o Binomial.o

test.o:		test.cpp Binomial.cpp
			g++ -c test.cpp

Binomial.o:	Binomial.cpp Binomial.hpp
	        g++ -c Binomial.cpp

clean:
	        rm -f *.o main test
			
