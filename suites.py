# Afin de définir la suite, veuillez y rentrez la formule la ou il est marqué juste en dessous. Pour exprimer une puissance utilisez ** devant la puissane, exemple : 2 puissance 5 est égal à 2**5

def suite(n = None):
  #Mettez votre formule avec n juste en dessous
  return VOTRE_FORMULE

#Quelques exemples

def suite_test(n = None):
  #Mettez votre formule avec n juste en dessous
  return 2**n + 4

print(suite_test(7))

#Pareil qu'avant sauf que cette fois vous aurez un étalonnage n_min et n_max qui définit la plage à parcourir (cette fois ci n'utilisez pas print mais directement la fonction) et mettez la formule dans la parenthèse

def suite_plage(n_min, n_max):
  for n in range(n_min, n_max):
    print("U" + n + " = " + (VOTRE_FORMULE))

#Quelques exemples

def suite_plage_test(n_min, n_max):
  for n in range(n_min, n_max):
    print("U" + str(n) + " = " + str(2**n + 4))

suite_plage_test(0,10)

#En espèrant que cela puisse vous aidez pour calculez plus facilement vos suites
