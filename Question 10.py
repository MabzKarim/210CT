seq = [5,6,7,8,9,15,17,19]
#array of numbers

def search_max_subseq(x):
  """this function finds the maximum sub sequence in ascending order"""
  subseq = [x[0]]
  for i in x[1:]:
    #iterate through rest of numbers
    if subseq[-1] + 1 is i:
      subseq.append(i)
    if not len(subseq) > 1:
      subseq = [i]
    elif i < subseq[-1] and len(subseq) > 1:
      return subseq
  return subseq

print (search_max_subseq(seq))
