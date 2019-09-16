class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for email in emails:
            name, domain = email.split("@")
            s.add(name.split("+")[0].replace(".", "") + "@" + domain)
        return len(s)
        
