# 1. 피연산자가 나오면 그대로 출력한다.
# 2. 연산자가 들어오면, 그보다 우선순위가 높거나 같은 연산자들을 스택에서 pop 한 뒤 새로 들어온 연산자를 push 한다.
# 3. 열린 괄호 '('가 들어오면, 스택에 push 한다.
# 4. 닫힌 괄호 ')'가 들어오면, 스택에서 '('가 나올 때까지 모두 pop 해준다.
# 5. 모든 수식을 다 읽었다면, 스택에 남아있는 것들을 pop 한다.

# 참고 : https://velog.io/@cria2000/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A0%84%EC%9C%84prefix-%EC%A4%91%EC%9C%84infix-%ED%9B%84%EC%9C%84postfix-%ED%91%9C%EA%B8%B0%EB%B2%95-%EB%B3%80%ED%99%98-%EB%B0%8F-%EA%B3%84%EC%82%B0
# https://reakwon.tistory.com/62

# 여는 괄호는 우선순위가 가장 낮게 설정해, 2번 규칙에 의해 멈추도록 한다.

infix = input()
cal = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

result = ""
stack = []
for k in infix:
    # 피연산자
    if k.isalpha():
        result += k

    # 연산자
    else:
        if k == '(':
            stack.append(k)

        # '(' 만날 때까지 더하기
        elif k == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        # 현재 우선순위가 높은 경우 (/, *)
        elif stack and cal[k] > cal[stack[-1]]:
            stack.append(k)

        # 현재 우선순위가 낮은 경우 (-, +)
        else:
            # 현재 우선순위보다 같거나 높은 연산자들 모두 pop()
            while stack and cal[stack[-1]] >= cal[k]:
                result += stack.pop()
            stack.append(k)



while stack:
    result += stack.pop()

print(result)