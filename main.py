import Network
from PlotGenerator import PlotGenerator
from Chromosome import ChromosomeCreator
from Chromosome import ChromosomeUtils
from Parameters import Parameters, OpticalFibersCapacity
from Algorithm import Algorithm


def alg1_usa():
    network = Network.generate_network_with_admissible_paths2(Parameters.number_of_adm_paths_to_choose_from,
                                                             'Resources/net-us.xml')
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_usa(network, Parameters.amount_of_chromosomes_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm1_usa()
    print(algorithm.results)
    plot_gen = PlotGenerator(algorithm.results)
    plot_gen.show_plot()

    for chromosome in chromosomes:
        cost = chromosome_utils.get_network_cost_100(chromosome, Parameters.optical_fiber_capacity_usa)
        if cost == 0:
            print(cost)
            for key in chromosome.paths_demand:
                for demand in chromosome.paths_demand[key]:
                    print(demand, end=' ')
                print()

            print()


def alg1_pol():
    from Network import Network
    network = Network.load_from_file('Resources/net-pl.xml', structure=True, demands=True, admissible_paths=3)

    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_all_in_one(network, Parameters.amount_of_chromosomes_pol)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm1_pol()
    print(algorithm.results)

    for chromosome in chromosomes:
        cost = chromosome_utils.get_network_cost_100(chromosome, Parameters.optical_fiber_capacity_pol)
        if cost == 0:
            print(cost)
            for key in chromosome.paths_demand:
                for demand in chromosome.paths_demand[key]:
                    print(demand, end=' ')
                print()

            print()


def alg2_pol():
    from Network import Network

    network = Network.load_from_file('Resources/net-pl.xml', structure=True, demands=True, admissible_paths=3)
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_semi_random(network, 20 * Parameters.amount_of_chromosomes_pol)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.pick_bests(chromosomes, chromosome_utils.get_network_transponders_cost, Parameters.amount_of_chromosomes_pol, OpticalFibersCapacity.L96)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm2_pol()
    print(algorithm.results)
    plot_gen = PlotGenerator(algorithm.results)
    plot_gen.show_plot()

    best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_cost, 1, OpticalFibersCapacity.L96)[0]
    for key in sorted(best_chromosome.paths_dict):
        print("{} -> ".format(key))
        for demand, path in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key]):
            print("{} {}".format(demand, chromosome_utils.get_transponders_cost2(demand)), end="")
            print("{} ".format(path))
        print()


def alg2_usa():

    network = Network.generate_network_with_admissible_paths2(Parameters.number_of_adm_paths_to_choose_from,
                                                             'Resources/net-us.xml')
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_usa(network, 20 * Parameters.amount_of_chromosomes_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.pick_bests(chromosomes, chromosome_utils.get_network_transponders_cost, Parameters.amount_of_chromosomes_usa, Parameters.optical_fiber_capacity_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm2_usa()
    print(algorithm.results)
    plot_gen = PlotGenerator(algorithm.results)
    plot_gen.show_plot()

    best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_cost, 1, Parameters.optical_fiber_capacity_usa)[0]
    for key in sorted(best_chromosome.paths_dict):
        print("{} -> ".format(key))
        for demand, path in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key]):
            print("{} {}".format(demand, chromosome_utils.get_transponders_cost2(demand)), end="")
            print("{} ".format(path))
        print()


def test():
    l = [195, 158, 174, 101, 198, 158, 182, 154, 175, 122, 114, 179, 117, 105, 159, 198, 189, 166, 142, 137, 163, 131,
         159, 164, 128, 195, 130, 105, 173, 157, 194, 125, 110, 132, 159, 109, 126, 100, 124, 106, 136, 144, 168, 119,
         127, 105, 147, 140, 198, 104, 113, 169, 187, 196, 193, 151, 106, 125, 194, 194, 123, 181, 193, 181, 195, 141]
    s = 0
    c = ChromosomeUtils()
    for d in l:
        s += c.get_transponders_cost2(d)
    print(s * 2)


def main():
    alg1_usa()

if __name__ == '__main__':
    main()

