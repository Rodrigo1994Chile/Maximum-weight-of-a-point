# Python routine for computing theoretical weights on points of algebraic curves

This repository contains a Python routine related to the study of Weierstrass points on algebraic curves.

Current functionality includes:

- Computation of the maximum weight of a point on a non-hyperelliptic curve of genus g

This routine was developed for research purposes and are primarily
intended for experiments in algebraic geometry.

## Mathematical background

For a point p on an algebraic curve of genus g there exist precisely g integers 1<n_1< ... < n_2g <2g+1
such that there doesn't exist a function f_k which has a pole on p and it is regular everywhere
else. These integers are called the gap-sequence at p; similarly its complement are the non-gaps.

For any non-gap there exists a meromorhpic function with the aforementioned property, so they form a semi group.

The weight of a point is defined as $\sum (n_k - k)$. A Weierstrass point is such that its weight is possible.

Only on a hyperelliptic curve the Weierstrass points have maximum weight g(g-1)/2 . 

The routines computes the (theoretical) maximum weight of a point on a non-hyperelliptic curve.

## Requirements

- Python 3

Clone the repository and load the desired routines inside Python or equivalent.

## Files

maximum_weight.py includes functions:

    complete
        inputs a semigroup and a new generator and outputs a bigger semigroup.
    
    Weight
        inputs a gap-sequence and outputs the corresponding weight.

    find_max_weight
        inputs the genus of the curve and visits every possible gap-sequence until it finds the one with maximum weight avoiding the hyperelliptic sequence.
    
## References

Farkas V., Kra I. Riemann surfaces, Graduate Texts in Mathematics 71, Springer-Verlag, New York-Berlin. (1980)

Miranda, R. Algebraic curves and Riemann surfaces (Graduate Studies in Mathematics, Vol 5). American Mathematical Society. (1995)


### Example

print(find_max_weight(5))
