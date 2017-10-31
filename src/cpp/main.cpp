#include <iostream>
#include "Binomial.hpp"

int main()
{
  double n = 10.0;
  double p = 0.5;

  for(double x = 1.0; x <= 10.0; x++)
  {
    std::cout << dbinom(x, n, p) << std::endl;
  }

  return 0;
}
