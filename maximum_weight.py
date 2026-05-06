# -*- coding: utf-8 -*-
from math import ceil

def complete(sg,new_gen,g):
  """
  This method inputs a semi group truncated up to 2g and a new generator to
  update the semi group.

  Input:    A sorted list       sg
            The new generator   new_gen
            A positive integer  g

  Output:   A sorted list       new_sg
  """

  if new_gen in sg:
    return sg
  n=new_gen
  new_sg=set(sg)
  while n<=2*g:
    new_sg.add(n)
    for elem in sg:
      if elem+n<=2*g:
        new_sg.add(elem+n)
      else:
        break
    n+=new_gen
  new_sg=list(new_sg)
  new_sg.sort()
  return new_sg

def Weight(L):
  """
  This method inputs the gap sequence   {gamma_k}_k   of a point in Noether gaps
  theorem and outputs the weight of the point defined as    sum_k (gamma_k - k)

  Input:    A sorted list           L

  Output:   A non negative integer  w
  """

  w=0
  g=int(len(L)/2)
  for i in range(len(L)):
    # print(L[i])
    w+=L[i]-i-1
  return w

def find_max_weight(g,sg=[],n=3):
  """
  Computes the maximum possible weight of a point on a non-hyperellpitic curve
  of genus g. It tries with all possible gap sequences of a point given by the
  Noether gaps theorem.

  The non-gaps form a semi-group so the algorithm starts with a blank list and
  in every step adds a new generator for the semi group (truncated up to 2g)
  until its lenght is precisely g. If the lenght of the list is more than g it
  discards and tries with the new step. If the lenght is g then it computes the
  weight and tries with a new step until it tries with every possible sequence
  and chooses the one with the maximum weight.

  Input:  The genus g of the curve...
              find_max_weight(g)
          If needed it can be specified that there exists a meromorphic function
          of degree n_f with only a pole on the point...
              find_max_weight(g,n=n_f)

  Output: The maximum weight of a hypothetical point in genus g and the
          complement of its gap-sequence...
              find_max_weight(5)      ----->    (5, [3, 6, 7, 9, 10], 3)
              find_max_weight(5,n=5)  ----->    (4, [5, 6, 7, 8, 10], 5)

  ***If wished, it can compute the maximum weight in a hyperellpitic curve
  using n=2 but this gap-sequence is well-known.
  """

  if len(sg)==g:
    gaps=list(range(1,2*g+1))
    for i in sg:
      gaps.remove(i)
    w=Weight(gaps)
    return w,sg,n
  if len(sg)>g:
    return -1,sg,n
  w_max=0
  sg_max=[]
  for i in range(n,2*g+1):
    if i in sg:
      pass
    else:
      new_sg=complete(sg,i,g)
      w2,sg2=find_max_weight(g,new_sg,i)[:2]
      if w_max<w2:
        w_max=w2
        sg_max=sg2
  return w_max,sg_max,n



### Main
print(find_max_weight(5))
print(find_max_weight(5,n=5))
