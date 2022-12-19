import datetime
import random
from Components import Components
from random import randrange
import pronouncing
from CBB_Mailer import send_cbb_email
"""
S - Sentence
NP - Noun Phrase
VP - Verb Phrase
Det - Determiner: 'the, a'
Aux - Auxiliary (verb): 'can, will'
N - Noun: 'man, ball'
V - Verb: 'hit, see'
"""


def assemble_components(*args):
    return " ".join(args)


def verb(aux, v):
    return assemble_components(aux, v)


def np(det, n):
    return assemble_components(det, n)


def vp(v, aux):
    return assemble_components(v, aux)


def sentence(np, vp):
    return assemble_components(np, vp)


def create_new_sentence(noun_for_rhyme="null"):
    V = com.get_v()
    Aux = com.get_aux()
    N = com.get_n()

    if noun_for_rhyme == "null":
        N_for_verb_creation = com.get_n()
    else:
        N_for_verb_creation = noun_for_rhyme
    Det = com.get_det()
    Verb = verb(Aux, V)

    if randrange(0, 100) < 50:
        # Make sentence structure look like SentenceStructureVisual01.png
        NP_for_verb_creation = np(Det, N_for_verb_creation)
    else:
        # Make sentence structure look like SentenceStructureVisual02.png
        if noun_for_rhyme == "null":
            NP_for_NP_Creation = np(com.get_det(), com.get_n())
        else:
            NP_for_NP_Creation = np(com.get_det(), noun_for_rhyme)
        NP_for_verb_creation = "by " + NP_for_NP_Creation

    NP = np(Det, N)
    VP = vp(Verb, NP_for_verb_creation)
    S = sentence(NP, VP)
    return S


def create_new_catchphrase():
    # Create the catchphrase.
    rhyme_found = False
    while not rhyme_found:
        # 1. Create first sentence. (Can enter noun if you want.)
        s1 = create_new_sentence()
        # 2. Find word that rhymes with the final noun in the catchphrase.
        index_of_last_space = 0
        for i in range(0, len(s1)):
            if s1[i] == ' ' : index_of_last_space = i
        last_word_of_first_sentence = s1[index_of_last_space + 1:]
        if (len(pronouncing.rhymes(last_word_of_first_sentence))) > 0:
            rhyming_word = pronouncing.rhymes(last_word_of_first_sentence)[0]
            rhyme_found = True
        else:
            rhyme_found = False
    # 3. Create second sentence using thee word from step 2.
    s2 = create_new_sentence(rhyming_word)
    # 4. Combing the sentences, polish it and return the catch phrase.
    catch_phrase = polish_catchphrase(s1 + ", " + s2)
    return catch_phrase


def polish_catchphrase(cp):
    # 1. Capitalize the first letter.
    catch_phrase = cp[:2].capitalize() + cp[2:]
    # 2. Add punctuation.
    punctuations = [".", "?", "!"]
    catch_phrase += random.choice(punctuations)
    # 3. If 'a' is in the sentence decide with it should be changed to 'an'
    index_of_as = []
    if catch_phrase[0] == 'A' and catch_phrase[1] == ' ': index_of_as.append(0)
    for i in range(1, len(catch_phrase) - 2):
        if catch_phrase[i - 1] == ' ' and  catch_phrase[i] == 'a' and  catch_phrase[i + 1] == ' ': index_of_as.append(i)

    vowels = ['a', 'e', 'i', 'o', 'u']
    for num in index_of_as:
        if catch_phrase[num + 2] in vowels:
            catch_phrase = catch_phrase[:num+1] + "n" + catch_phrase[num+1:]

    return catch_phrase


def output_to_txt_file(file_name, cbb_cp):
    file1 = open(file_name, "a")
    file1.write(cbb_cp)
    file1.close()


# Run the Script
if __name__ == "__main__":
    com = Components()
    s = create_new_catchphrase()
    print(s)
    output_to_txt_file("CBB_Log", "\n" + str(datetime.date.today()) + " " + s)
    send_cbb_email('kevohaston@gmail.com', "CBB Daily Catchphrases", s)
