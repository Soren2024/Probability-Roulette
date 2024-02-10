import maths.bayes

def main() -> int:
    print('- Probability-Roulette -')
    print('Use probabilistic Buckshot Roulette to win. (Use Spaces to separate.)')
    B, E, S = map(int, input('Total bullets, Number of blanks, Hit count: ').split())
    R = maths.bayes.bayes(B,E,S)
    print('Result: {}'.format(R))
if __name__ == '__main__':
    raise SystemExit(main())