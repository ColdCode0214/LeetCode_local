class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set([])
        for name in emails:
            local, zone = name.split('@')
            local = local.split('+')[0]
            local = ''.join(local.split('.'))
            real = local + '@' + zone
            if real not in seen:
                seen.add(real)
        return len(seen)