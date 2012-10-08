"""Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:

Rule 1: S(B) != S(C); that is, sums of subsets cannot be equal.
Rule 2: If B contains more elements than C then S(B) > S(C).
For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.

Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A1, A2, ..., Ak, and find the value of S(A1) + S(A2) + ... + S(Ak).

NOTE: This problem is related to problems 103 and 106."""

import itertools
f = file('sets.txt', 'r').readlines()

#
def generate_all_subsets(set):
  subsets = []
  for i in xrange(1, len(set)):
    subsets += list(itertools.combinations(set, i))
  return subsets

def verify_rule_1(subsets):
  """Rule 1: S(B) != S(C); that is, sums of subsets cannot be equal."""
  return len(set(map(lambda k: sum(k), subsets))) == len(subsets)

def verify_rule_2(subset_1, subset_2):
  """If B contains more elements than C then S(B) > S(C)."""
  l1, l2, s1, s2 = len(subset_1), len(subset_2), sum(subset_1), sum(subset_2)
  if l1 > l2:
    return s1 > s2
  elif l2 > l1:
    return s2 > s1
  return True

def generate_subset_pairs(subsets):
  return set(itertools.combinations(subsets, 2))

if __name__ == '__main__':
  total_sum = 0
  for line in f:
    print "On line: ", line
    current_set = set(map(lambda k: int(k), line.strip().split(',')))
    all_subsets = generate_all_subsets(current_set)
    if not verify_rule_1(all_subsets):
      continue
    broken_rule = False
    for pair in generate_subset_pairs(all_subsets):
      if not verify_rule_2(pair[0], pair[1]):
        broken_rule = True
        break
    if broken_rule:
      continue
    total_sum += sum(current_set)
  print total_sum
