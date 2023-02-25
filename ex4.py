SP =67836.43
RJ=36678.66
MG=29229.88
ES=27165.48
Outros=19849.53
soma=SP+RJ+MG+ES+Outros
for i in range(1):
    perc=SP*100/soma
    print("SP:",perc)
    
    perc=RJ*100/soma
    print("RJ:",perc)

    perc=MG*100/soma
    print("MG:",perc)

    perc=ES*100/soma
    print("ES:",perc)

    perc=Outros*100/soma
    print("Outros:",perc)
    
