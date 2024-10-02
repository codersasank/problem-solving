class Solution:
    def toh(self, n, from_, to, aux):
        if n<=0:
            return 0
        num_moves = self.toh(n-1, from_, aux, to)
        print("move disk", n, "from rod", from_, "to rod", to)
        num_moves += self.toh(n-1, aux, to, from_)
        return 1 + num_moves
