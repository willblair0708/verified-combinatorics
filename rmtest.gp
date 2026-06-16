f = 9*x^6 + 64*x^5 - 200*x^3 + 64*x + 144;
bad = [2,3,5,139,349];
{forprime(p = 7, 200,
  if(!vecsearch(bad, p),
    P = hyperellcharpoly(Mod(f, p));
    a = -polcoeff(P, 3);
    b = polcoeff(P, 2);
    disc = a^2 - 4*(b - 2*p);
    print(p, "  a=", a, " b=", b, "  disc=", disc, "  core=", if(disc==0, 0, core(disc)))));}
