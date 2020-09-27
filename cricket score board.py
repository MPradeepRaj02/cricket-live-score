#25 SEP 2020
#PROGRAM TO GET LIVE SCORES OF CRICKET MATCHES
#       ------ M.P.R -------

from pycricbuzz import Cricbuzz

c = Cricbuzz()
match = c.matches()

score = c.livescore(match[0]['id'])         #to get live score
commentary = c.commentary(match[0]['id'])   #to get commentary of the live matches
score_board = c.scorecard(match[0]['id'])   #to get whole score card of the live matches

for a in score :
    print(a)
    for b in score[a] :
        print(b,':',score[a][b])

print(commentary)
print(score_board)

#       THE FAUCETER =>>  https://www.youtube.com/channel/UCqmC9XrDnoihqqiiCOnPwDg