
# 리스트

ear = [' ','      /) /)',' 　/)⋈/)','⠀   ᕱ🎀ᕱ','⠀   ∧,,,∧','    ᘏ▸◂ᘏ','    ⌒__⌒','   Δ~~~Δ']
face = [' ','    ( ̳• ·̫ • ̳)♡','“ପ(„ơ ᴗ ơ„)ଓ”',' 　(⠀*•‧̫•*⠀)','   (  ̳• · • ̳)','  ꒰ ɞ̴̶̷ ·̮ ɞ̴̶̷ ꒱','꒰ ⸝⸝ɞ̴̶̷ ·̮ ɞ̴̶̷ ⸝⸝꒱','   ( ˶ᵕ ﻌ ᵕ˶ )','    ( ・8・ )','    (  ・∀・ )']
body = [' ','   ⠀∪ ∪','  ..c(,_uuﾉ','    /    づ♡','    / >♥c\ ♡','  *ଘ_(")("）','  *ଘ_(")("）┄┄♡゛','    ଘ ੭♡੭ ✩‧₊˚➳','     ⊃♡⊂','   (")∪∪(")']


# 프로그램 소개

print('☆동물 이모티콘 만들기☆')
print('귀, 얼굴, 몸 파츠를 차례대로 골라주세요 (숫자만 입력 후 엔터)')

# 프로그램 코드

while True:
    a = int(input("""
< 귀 >
1: /) /)
2: /)⋈/)
3: ᕱ🎀ᕱ
4: ∧,,,∧
5: ᘏ▸◂ᘏ
6: ⌒__⌒
7: Δ~~~Δ
"""))
    if a > 7 or a < 1:
        print('존재하지 않는 번호입니다. 파츠를 다시 골라주세요.')
        continue
    else:
        break

while True:
    b = int(input("""
< 얼굴 >
1:( ̳• ·̫ • ̳)♡
2:“ପ(„ơ ᴗ ơ„)ଓ”
3: (⠀*•‧̫•*⠀)
4: (  ̳• · • ̳)
5: ꒰ ɞ̴̶̷ ·̮ ɞ̴̶̷ ꒱
6: ꒰ ⸝⸝ɞ̴̶̷ ·̮ ɞ̴̶̷ ⸝⸝꒱
7: ( ˶ᵕ ﻌ ᵕ˶ )
8: ( ・8・ )
9: (  ・∀・ )
"""))
    if b > 9 or b < 1:
        print('존재하지 않는 번호입니다. 파츠를 다시 골라주세요.')
        continue
    else:
        break

while True:
    c = int(input("""
< 몸 >
0: 생략
1: ∪ ∪
2: ..c(,_uuﾉ
3: /    づ♡
4: / >♥c\ ♡
5: *ଘ_(")("）
6: *ଘ_(")("）┄┄♡
7: ଘ ੭♡੭ ✩‧₊˚➳
8: ⊃♡⊂
9: (")∪∪(")
"""))
    if c > 9 or c < 0:
        print('존재하지 않는 번호입니다. 파츠를 다시 골라주세요.')
        continue
    else:
        break

# 실행 결과

print("""
완성된 이모티콘입니다.
""")
print(ear[a])
print(face[b])
print(body[c])
