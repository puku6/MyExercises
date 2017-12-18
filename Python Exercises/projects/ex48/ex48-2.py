lexicon = {}
for directions in ['north', 'south', 'east', 'west', 'down', 
                   'up', 'left', 'right', 'back']:
    lexicon.update({directions: 'direction'})
for verbs in ['go', 'stop', 'kill', 'eat']:
    lexicon.update({verbs: 'verb'})
for stops in ['the', 'in', 'of', 'from', 'at', 'it']:
    lexicon.update({stops: 'stop'})
for nouns in ['door', 'bear', 'princess', 'cabinet']:
    lexicon.update({nouns: 'noun'})



stuff = raw_input('> ')
words = stuff.lower().split()

def scan(sentence):
    words = sentence.split()
    pairs = []
    for word in words:
        try:
            k = word.lower()
            pairs.append((lexicon[k], word))
        except KeyError:
            if convert_number(word) != None:
                 pairs.append(('number', int(word)))
            else:
                pairs.append(('error', word))
    return pairs

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None
