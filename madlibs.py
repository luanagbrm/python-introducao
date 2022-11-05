# Concatenação e interação com usuário

past_verb = input("Verbo na 1ª pessoa do passado:\n")
nome1 = input("\nNome:\n")
nome2 = input("\nNome:\n")
place = input("\nLugar:\n")
subst = input("\nSubstantivo no plural:\n")

madlib = f"\nEstávamos {nome1}, {nome2} e eu {past_verb} no {place} quando {subst} aos montes \
começaram a cair do céu"

print(madlib)