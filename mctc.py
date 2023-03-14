import random


### markov_chain. Input the sample text and how long the chain will be. 
### outputs generated string
def markov_chain_text(text, chain_length):

    words = text.split()

    chain = {}

    for i in range(len(words) - chain_length):

        current_chain = tuple(words[i:i+chain_length])

        next_word = words[i+chain_length]

        if current_chain not in chain:
            chain[current_chain] = []
        chain[current_chain].append(next_word)

    current_chain = random.choice(list(chain.keys()))

    output = " ".join(current_chain)
    for i in range(100):
        if current_chain not in chain:
            break
        next_word = random.choice(chain[current_chain])
        output += " " + next_word
        current_chain = tuple(output.split()[-chain_length:])
    return output

text = "The quick brown fox jumps over the lazy dog"
chain_length = 4
print(markov_chain_text(text, chain_length))