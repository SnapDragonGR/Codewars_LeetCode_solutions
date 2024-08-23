class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for account in accounts:
            account_value = sum(account)
            if account_value > richest:
                richest = account_value
        return richest