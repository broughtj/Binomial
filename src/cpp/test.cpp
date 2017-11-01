#include <iostream>
#include "Binomial.hpp"

int main()
{
  double n = 10.0;
  double p = 0.5;
  long m = 1000000;

  for(long i = 0; i <= m; ++i)
  {
	for(double x = 1.0; x <= 10.0; x++)
	{
		dbinom(x, n, p);
	}
  }

  return 0;
}
