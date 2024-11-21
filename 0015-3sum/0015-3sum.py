class Solution:
    def threeSum(self, lst: List[int]) -> List[List[int]]:
        # Necessary for using two pointers
        lst = sorted(lst)
        # Set to ensure no duplicates
        unique_triplets = set()
        target = 0


        for i in range(len(lst)):
            # lst[i] is the offset, if it's larger than target - no point in searching further
            if lst[i] > target:
                break
            # Move on to the next iteration if two adjacent nums are the same - skip duplicates
            if i > 0 and lst[i] == lst[i-1]:
                continue

            # Initializing front and back pointers
            fp, bp = i + 1, len(lst) - 1

            # While loop to find triplets with two pointers
            while fp < bp:
                # Sum of the current triplet
                summary = lst[i] + lst[fp] + lst[bp]
                # If the sum matches the target - add the triplet to the set
                if target == summary:
                    unique_triplets.add((lst[i], lst[fp], lst[bp]))
                    # Move pointers inwards after finding a valid triplet
                    fp, bp = fp + 1, bp - 1

                    # Skip duplicate elements for the fp
                    while fp < bp and lst[fp] == lst[fp - 1]:
                        fp += 1

                    # Skip duplicate elements for bp
                    while fp < bp and lst[bp] == lst[bp + 1]:
                        bp -= 1

                # If the sum is less than the target, move the fp forward (increase the sum)
                elif summary < target:
                    fp += 1

                # If the sum is greater than the target, move the bp backward (decrease the sum)
                else:
                    bp -= 1

        return list(unique_triplets)