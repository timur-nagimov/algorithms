class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for number in tokens:
            if number == '+':
                n1 = numbers.pop()
                n2 = numbers.pop()
                numbers.append(n2+n1)
            elif number == '-':
                n1 = numbers.pop()
                n2 = numbers.pop()
                numbers.append(n2-n1)
            elif number == '/':
                n1 = numbers.pop()
                n2 = numbers.pop()
                numbers.append(int(n2 / n1))
            elif number == '*':
                n1 = numbers.pop()
                n2 = numbers.pop()
                numbers.append(n2*n1)
            else:
                numbers.append(int(number))

        return numbers[0]
