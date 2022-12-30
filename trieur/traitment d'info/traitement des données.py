chemin = "C:/Users/yaosi/Desktop/Prog/g.txt"
 
with open (chemin, "r") as f:
    contenu = f.read().splitlines()
 
prenoms_desordonnes = []
for line in contenu:
    prenoms_desordonnes.extend(line.split())
 
prenoms_final = [prenom.strip(",. ") for prenom in prenoms_desordonnes]
 
with open(chemin, "w") as f:
    f.write("\n".join(sorted(prenoms_final)))