from random import Random
from time import time
from inspyred import ec
from inspyred.ec import terminators
import numpy as np

#gerador de população
def generate_(random, args):
    size = args.get('num_inputs', 12) 
    return [random.randint(0, 16000) for i in range(size)] 

#função para avaliar soluções
def evaluate_(candidates, args):
    fitness = []
    for cs in candidates:
        fit = perform_fitness(cs[0], cs[1], cs[2], cs[3], cs[4], cs[5], cs[6], cs[7], cs[8], cs[9], cs[10], cs[11])
        fitness.append(fit)
    return fitness

#função para calcular o fitness
def perform_fitness(cs1, cs2, cs3, cs4, cs5, cs6, cs7, cs8, cs9, cs10, cs11, cs12):
    cd1 = np.round(cs1)
    cc1 = np.round(cs2)
    ct1 = np.round(cs3)
    cd2 = np.round(cs4)
    cc2 = np.round(cs5)
    ct2 = np.round(cs6)
    cd3 = np.round(cs7)
    cc3 = np.round(cs8)
    ct3 = np.round(cs9)
    cd4 = np.round(cs10)
    cc4 = np.round(cs11)
    ct4 = np.round(cs12)
    fit = float(((cd1 * 0.31) + (cc1 * 0.31) + (ct1 * 0.31) + (cd2 * 0.38) + (cc2 * 0.38) + (ct2 * 0.38) + (cd3 * 0.35) + (cc3 * 0.35) + (ct3 * 0.35) + (cd4 * 0.285) + (cc4 * 0.285) + (ct4 * 0.285)) / 42565.92)
  
    #restrições
    cargaTotal = cd1 + cd2 + cd3 + cd4 + cc1 + cc2 + cc3 + cc4 + ct1 + ct2 + ct3 + ct4
    num = 14

    #máximo de 10000kg na dianteira
    h1 = np.maximum(0, float((cd1 + cd2 + cd3 + cd4) - 10000)) / (10000 / num)

    #máximo de 16000kg na central
    h2 = np.maximum(0, float((cc1 + cc2 + cc3 + cc4) - 16000)) / (16000 / num)

    #máximo de 8000kg na traseira
    h3 = np.maximum(0, float((ct1 + ct2 + ct3 + ct4) - 8000)) / ( 8000 / num)

    #máximo de 18000kg da carga 1
    h4 = np.maximum(0, float((cd1 + cc1 + ct1) - 18000))/ (18000 / num)

    #máximo de 15000kg da carga 2
    h5 = np.maximum(0, float((cd2 + cc2 + ct2) - 15000)) / (15000 / num)

    #máximo de 23000kg da carga 3
    h6 = np.maximum(0, float((cd3 + cc3 + ct3) - 23000)) / (23000 / num)

    #máximo de 12000kg da carga 4
    h7 = np.maximum(0, float((cd4 + cc4 + ct4) - 12000))/ (12000 / num)

    #máximo de 6800m³ na dianteira
    h8 = np.maximum(0, float(((cd1 * 0.48) + (cd2 * 0.65) + (cd3 * 0.58) + (cd4 * 0.39)) - 6800)) / (6800 / num )

    #máximo de 8700m³ na central
    h9 = np.maximum(0, float(((cc1 * 0.48) + (cc2 * 0.65) + (cc3 * 0.58) + (cc4 * 0.39)) - 8700)) / (8700 / num)

    #máximo de 5300m³ na traseira
    h10 = np.maximum(0, float(((ct1 * 0.48) + (ct2 * 0.65) + (ct3 * 0.58) + (ct4 * 0.39)) - 5300)) / (5300 / num)

    #proporção da carga dianteira
    h11 = np.maximum(0, float((((cd1 + cd2 + cd3 + cd4) / cargaTotal) - 0.29411764706))) / (0.29411764706 / num)

    #proporção da carga central
    h12 = np.maximum(0, float((((cc1 + cc2 + cc3 + cc4) / cargaTotal) - 0.47058823529))) / (0.47058823529 / num)
    
    #proporção da carga traseira
    h13 = np.maximum(0, float((((ct1 + ct2 + ct3 + ct4) / cargaTotal) - 0.23529411765))) / (0.23529411765 / num)

    #peso total no avião
    h14 = np.maximum(0, float(cargaTotal - 34000)) / (34000 / num)

    fit = fit - (h1 + h2 + h3 + h4 + h5 + h6 + h7 + h8 + h9 + h10 + h11 + h12 + h13 + h14)
    return fit


def solution_evaluation(CD1, CC1, CT1, CD2, CC2, CT2, CD3, CC3, CT3, CD4, CC4, CT4):
    CD1 = np.round(CD1)
    CD2 = np.round(CD2)
    CD3 = np.round(CD3)
    CD4 = np.round(CD4)
    CT1 = np.round(CT1)
    CT2 = np.round(CT2)
    CT3 = np.round(CT3)
    CT4 = np.round(CT4)
    CC1 = np.round(CC1)
    CC2 = np.round(CC2)
    CC3 = np.round(CC3)
    CC4 = np.round(CC4)

    volumeDianteiro = float((CD1*0.48)+(CD2*0.65)+(CD3*0.58)+(CD4*0.39))
    volumeCentral = float((CC1*0.48)+(CC2*0.65)+(CC3*0.58)+(CC4*0.39))
    volumeTraseiro = float((CT1*0.48)+(CT2*0.65)+(CT3*0.58)+(CT4*0.39))
    pesoDianteiro = float(CD1 + CD2 + CD3 + CD4)
    pesoCentral = float(CC1 + CC2 + CC3 + CC4)
    pesoTraseiro = float(CT1 + CT2 + CT3 + CT4)
    pesoTotal = pesoDianteiro + pesoCentral + pesoTraseiro

    lucro1 = float((CD1*0.31)+(CC1*0.31)+(CT1*0.31))
    lucro2 = float((CD2*0.38)+(CC2*0.38)+(CT2*0.38))
    lucro3 = float((CD3*0.35)+(CC3*0.35)+(CT3*0.35))
    lucro4 = float((CD4*0.285)+(CC4*0.285)+(CT4*0.285))

    print("")
    print("RESUMO DA EXECUÇÃO")
    print("")
    print("Lucro total: ", (lucro1 + lucro2 + lucro3 + lucro4))
    print("Compartimento dianteiro: Peso = ", pesoDianteiro, "kg - ", (pesoDianteiro/pesoTotal)*100, '%  |  Volume = ', volumeDianteiro)
    print("Compartimento central: Peso = ", pesoCentral, "kg - ", (pesoCentral/pesoTotal)*100, '%  |  Volume = ', volumeCentral)
    print("Compartimento traseiro: Peso = ", pesoTraseiro, "kg - ", (pesoTraseiro/pesoTotal)*100, '%  |  Volume = ', volumeTraseiro)
    print("Total de peso: ", pesoTotal, "kg | Total volumétrico: ", (volumeDianteiro + volumeCentral + volumeTraseiro))
    print("")
    print("Carga 1 no compartimento dianteiro: ", CD1)
    print("Carga 1 no compartimento central: ", CC1)
    print("Carga 1 no compartimento traseiro: ", CT1)
    print("Total da carga 1: ", CD1 + CC1 + CT1)
    print("Lucro carga 1: ", lucro1)
    print("")
    print("Carga 2 no compartimento dianteiro: ", CD2)
    print("Carga 2 no compartimento central: ", CC2)
    print("Carga 2 no compartimento traseiro: ", CT2)
    print("Total da carga 2: ", CD2 + CC2 + CT2)
    print("Lucro carga 2: ", lucro2)
    print("")
    print("Carga 3 no compartimento dianteiro: ", CD3)
    print("Carga 3 no compartimento central: ", CC3)
    print("Carga 3 no compartimento traseiro: ", CT3)
    print("Total da carga 3: ", CD3 + CC3 + CT3)
    print("Lucro carga 3: ", lucro3)
    print("")
    print("Carga 4 no compartimento dianteiro: ", CD4)
    print("Carga 4 no compartimento central: ", CC4)
    print("Carga 4 no compartimento traseiro: ", CT4)
    print("Total da carga 4: ", CD4 + CC4 + CT4)
    print("Lucro carga 4: ", lucro4)

def main():
    rand = Random()
    rand.seed(int(time()))

    ea = ec.GA(rand)
    ea.selector = ec.selectors.tournament_selection
    ea.variator = [ec.variators.uniform_crossover,
                   ec.variators.gaussian_mutation]

    ea.replacer = ec.replacers.steady_state_replacement

    ea.terminator = terminators.generation_termination

    ea.observer = [ec.observers.stats_observer, ec.observers.file_observer]

    final_pop = ea.evolve(generator=generate_,
                          evaluator=evaluate_,
                          pop_size=10000,
                          maximize=True,
                          bounder=ec.Bounder(0, 16000),
                          max_generations=2000,
                          num_inputs= 12,
                          crossover_rae = 1.0,
                          num_crossover_points = 1,
                          mutation_rate = 0.6,
                          num_elites = 1,
                          num_selected = 12,
                          tournament_size = 12,
                          statistics_file=open("plane_stats.csv", "w"),
                          individuals_file=open("plane_individuais.csv", "w"))

    final_pop.sort(reverse=True) 
    print(final_pop[0])

    perform_fitness(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7], final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])
    solution_evaluation(final_pop[0].candidate[0], final_pop[0].candidate[1], final_pop[0].candidate[2], final_pop[0].candidate[3], final_pop[0].candidate[4], final_pop[0].candidate[5], final_pop[0].candidate[6], final_pop[0].candidate[7], final_pop[0].candidate[8], final_pop[0].candidate[9], final_pop[0].candidate[10], final_pop[0].candidate[11])

main()
