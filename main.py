import spacy

nlp = spacy.load("en_core_web_sm")

def identify_continuous_tenses(text):
    token = nlp(text)

    obj_idx = 2

    cont_aux_single = {'is', 'was', 'has been'}
    cont_aux_plural = {'were', 'are', 'have been'}

    single_pron = {'he', 'she', 'it'}
    plural_pron = {'you', 'they', 'we'}

    aux_tags = {'VBZ', 'VBD', 'VB', 'VBP'}

    lower_aux = token[1].text.lower()
    lower_sub = token[0].text.lower()

    if lower_aux == 'has' or lower_aux == 'have':
        obj_idx = 3
        lower_aux += (' ' + token[2].text)

    is_subj_name = token[0].pos_ == 'PROPN' or \
                   token[0].pos_ == 'NOUN'

    is_singular = lower_sub in single_pron or is_subj_name

    right_aux = lower_aux in cont_aux_single if is_singular \
                else lower_aux in cont_aux_plural

    right_sub = token[0].pos_ == 'PRON' or is_subj_name

    if lower_sub == 'i':
        right_aux = lower_aux == 'am'  or \
                    lower_aux == 'was' or \
                    lower_aux == 'have been'

    # print()
    # print(right_sub)
    # print(token[1].tag_ in aux_tags)
    # print(right_aux)
    # print(token[obj_idx].tag_ == 'VBG')

    return                  right_sub and \
            token[1].tag_ in aux_tags and \
                            right_aux and \
             token[obj_idx].tag_ == 'VBG'

############################################################

sentences = [
                "You were turning.",
                "It were wearing.",
                "He is seeing.",
                "She was seeing.",
                "We were working.",
                "She was cooking.",
                "You is walking.",
                "Ahmad is cooking.",
                "They was washing.",
                "We is marking.",
                "It was driving.",
                "They are wishing.",
                "I was driving.",
                "You are erupting.",
                "He is working.",
                "They are working.",
                "They were driving.",
                "They are washing.",
                "She were seeing.",
                "He was observing.",
                "You were waterning.",
                "I is waterning.",
                "They were arranging.",
                "We was sleeping."
            ]

for sentence in sentences:
    # sentence = "I has been going"
    continuous_tenses = identify_continuous_tenses(sentence)

    if continuous_tenses:
        print(f"CORRECT:   {sentence}👍")
    else:
        print(f"INCORRECT: {sentence}❌")
