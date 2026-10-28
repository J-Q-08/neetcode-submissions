class Solution:

    def encode(self, strs: List[str]) -> str:
        send = ""
        for word in strs:
            send += str(len(word)) + "#" + word
        return send

    def decode(self, s: str) -> List[str]:
        decoded = []
        num = ""

        for _ in range(len(s)):
            if not s:
                break

            if s[0] == "#":
                length = int(num)
                decoded.append(s[1:1 + length])
                s = s[1 + length:]
                num = ""
            else:
                num += s[0]
                s = s[1:]

        return decoded

        