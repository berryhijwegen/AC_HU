from Flumph import Flumph

toestanden1 = {
    0 : 'Hongerig',
    1 : 'Tevreden',
    2 : 'Opgejaagd'
}
chances1 = [
    [0.8, 0.1, 0.1],
    [0.4, 0.5, 0.1],
    [0.6, 0.2, 0.2]
]
chanceVector1 = [0.1, 0.7, 0.2]

toestanden2 = {
    0 : 'Hongerig',
    1 : 'Tevreden',
    2 : 'Opgejaagd',
    3 : 'Overleden'
}
chances2 = [
    [0.72, 0.1, 0.1, 0.08],
    [0.38, 0.5, 0.1, 0.02],
    [0.56, 0.2, 0.2, 0.04],
    [ 0.0, 0.0, 0.0,  1.0]
]
chanceVector2 = [0.1, 0.65, 0.2, 0.05]
   
flumph3 = Flumph(toestanden1, chances1, chanceVector1)

flumph4 = Flumph(toestanden2, chances2, chanceVector2)
 
flumph3.plotChances()
flumph4.plotChances()

print(flumph3.getTensorProduct(1))
print(flumph3.getTensorProduct(2))