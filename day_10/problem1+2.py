pairs = {'{': '}',
         '[': ']',
         '<': '>',
         '(': ')'
         }
scores = {')': 3,
          ']': 57,
          '}':1197,
          '>':25137
          }
complete_scores = {')': 1,
          ']': 2,
          '}':3,
          '>':4
          }

error_score = 0
complete_score = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        error = False
        pipe = []
        for c in line.strip():
            if c in pairs.keys():
                pipe.append(c)
            else:
                if len(pipe) == 0:
                    error = True
                    break
                elif pairs[pipe[-1]] != c:
                    error = True
                    error_score += scores[c]
                    break
                pipe = pipe[:-1]
        if not error:
            complete = [pairs[c] for c in reversed(pipe)]
            score = 0
            for c in complete:
                score = score*5 + complete_scores[c]
            complete_score.append(score)
                    
print(f'error score is {error_score}')
complete_score = sorted(complete_score)
print(f'complete score is {complete_score[len(complete_score)//2]}')