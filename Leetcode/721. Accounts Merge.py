class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        num_accounts = len(accounts)
        parent = list(range(num_accounts))
        
        def find(account_id):
            if account_id != parent[account_id]:
                parent[account_id] = find(parent[account_id])  # Path compression
            return parent[account_id]
        
        def union(account1, account2):
            root1 = find(account1)
            root2 = find(account2)
            if root1 != root2:
                parent[root2] = root1
        
        # Dictionary to map each email to the corresponding account index
        email_to_account = {}
        for account_index, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    union(account_index, email_to_account[email])
                email_to_account[email] = account_index
        
        # Dictionary to collect emails for each root account
        emails_by_root = collections.defaultdict(list)
        for email, account_index in email_to_account.items():
            root_account = find(account_index)
            emails_by_root[root_account].append(email)
        
        # Prepare the merged accounts result
        merged_accounts = []
        for root_account, emails in emails_by_root.items():
            merged_accounts.append([accounts[root_account][0]] + sorted(emails))
        
        return merged_accounts
