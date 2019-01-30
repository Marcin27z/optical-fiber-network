import Network
import random
from PlotGenerator import PlotGenerator
from Chromosome import ChromosomeCreator
from Chromosome import ChromosomeUtils
from Parameters import Parameters, OpticalFibersCapacity
from Algorithm import Algorithm


def alg1_usa():
    print("Problem alokacji dla sieci amerykanskiej " + str(Parameters.optical_fiber_capacity_usa))
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_usa))
    print("Przepustowosc: " + str(Parameters.optical_fiber_capacity_usa.value))
    network = Network.generate_network_with_admissible_paths(Parameters.number_of_adm_paths_to_choose_from,
                                                             'Resources/net-us.xml')
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_semi_random(network, Parameters.amount_of_chromosomes_usa)
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
    print("Problem alokacji dla sieci polskiej " + str(Parameters.optical_fiber_capacity_pol))
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_pol))
    print("Przepustowosc: " + str(Parameters.optical_fiber_capacity_pol.value))
    from Network import Network
    network = Network.load_from_file('Resources/net-pl.xml', structure=True, demands=True, admissible_paths=3)

    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_semi_random(network, Parameters.amount_of_chromosomes_pol)
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
    print("Problem minimalizaji kosztu dla sieci polskiej")
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_pol))
    print("Przepustowosc: " + str(OpticalFibersCapacity.L96.value))
    from Network import Network
    network = Network.load_from_file('Resources/net-pl.xml', structure=True, demands=True, admissible_paths=2)
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_usa(network, 20 * Parameters.amount_of_chromosomes_pol)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.pick_bests(chromosomes, chromosome_utils.get_network_transponders_cost,
                                       Parameters.amount_of_chromosomes_pol, OpticalFibersCapacity.L96)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm2_pol()
    print(algorithm.results)
    plot_gen = PlotGenerator(algorithm.results)
    plot_gen.show_plot()

    best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_cost, 1,
                                                  OpticalFibersCapacity.L96)[0]
    for key in sorted(best_chromosome.paths_dict):
        print("{} -> ".format(key))
        for demand, path in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key]):
            print("{} {}".format(demand, chromosome_utils.get_transponders_cost2(demand)), end="")
            print("{} ".format(path))
        print()


def alg2_usa():
    print("Problem minimalizacji kosztu dla sieci amerykanskiej")
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_usa))
    print("Przepustowosc: " + str(OpticalFibersCapacity.L96.value))
    network = Network.generate_network_with_admissible_paths(Parameters.number_of_adm_paths_to_choose_from,
                                                             'Resources/net-us.xml')
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_semi_random(network,
                                                                      20 * Parameters.amount_of_chromosomes_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.pick_bests(chromosomes, chromosome_utils.get_network_transponders_cost,
                                       Parameters.amount_of_chromosomes_usa, Parameters.optical_fiber_capacity_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm2_usa()
    print(algorithm.results)
    plot_gen = PlotGenerator(algorithm.results)
    plot_gen.show_plot()

    best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_cost, 1,
                                                  Parameters.optical_fiber_capacity_usa)[0]
    for key in sorted(best_chromosome.paths_dict):
        print("{} -> ".format(key))
        for demand, path in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key]):
            print("{} {}".format(demand, chromosome_utils.get_transponders_cost2(demand)), end="")
            print("{} ".format(path))
        print()


def alg3_usa():
    print("Problem alokacji dla sieci amerykanskiej z 2 sciezkami predefiniowanymi i 170 demand na kazdym")
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_usa))
    print("Przepustowosc: " + str(OpticalFibersCapacity.L96.value))
    network = Network.generate_network_with_admissible_paths2(Parameters.number_of_adm_paths_to_choose_from,
                                                              'Resources/net-us.xml')
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_usa(network, Parameters.amount_of_chromosomes_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm1_usa()
    print(algorithm.results)

    for chromosome in chromosomes:
        cost = chromosome_utils.get_network_cost_100(chromosome, Parameters.optical_fiber_capacity_usa)
        if cost == 0:
            print(cost)
            for key in chromosome.paths_demand:
                for demand in chromosome.paths_demand[key]:
                    print(demand, end=' ')
                print()

            print()


def alg4_usa():
    print("Problem minimalizacji kosztu dla sieci amerykanskiej z 2 sieczkami predefiniowanymi i 170 demand na kazdym")
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_usa))
    print("Przepustowosc: " + str(OpticalFibersCapacity.L96))
    network = Network.generate_network_with_admissible_paths2(Parameters.number_of_adm_paths_to_choose_from,
                                                              'Resources/net-us.xml')
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_usa(network, Parameters.amount_of_chromosomes_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.pick_bests(chromosomes, chromosome_utils.get_network_transponders_cost,
                                       Parameters.amount_of_chromosomes_usa, Parameters.optical_fiber_capacity_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm2_usa()
    print(algorithm.results)
    plot_gen = PlotGenerator(algorithm.results)
    plot_gen.show_plot()

    best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_cost, 1,
                                                  Parameters.optical_fiber_capacity_usa)[0]
    for key in sorted(best_chromosome.paths_dict):
        print("{} -> ".format(key))
        for demand, path in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key]):
            print("{} {}".format(demand, chromosome_utils.get_transponders_cost2(demand)), end="")
            print("{} ".format(path))
        print()


def usa_90():
    print("Problem minimalizacji kosztu dla sieci amerykanskiej z 2 sieczkami predefiniowanymi i 90 demand na kazdym")
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_usa))
    print("Przepustowosc: " + str(OpticalFibersCapacity.L96.value))
    network = Network.generate_network_with_admissible_paths2(Parameters.number_of_adm_paths_to_choose_from,
                                                              'Resources/net-us.xml')
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_usa_90(network, Parameters.amount_of_chromosomes_usa)

    # algorithm = Algorithm(chromosomes, network)
    # chromosomes = algorithm.pick_bests(chromosomes, chromosome_utils.get_network_transponders_cost,
    #                                    Parameters.amount_of_chromosomes_usa, Parameters.optical_fiber_capacity_usa)
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm_usa_90(Parameters.optical_fiber_capacity_usa)
    print(algorithm.results)
    plot_gen = PlotGenerator([[algorithm.results, 'g--']])
    plot_gen.show_plot()

    best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_configuration_cost, 1,
                                                  Parameters.optical_fiber_capacity_usa)[0]
    for key in sorted(best_chromosome.paths_dict):
        print("{} -> ".format(key))
        for demand, path, transponders in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key],
                                              best_chromosome.transponders_used[key]):
            print("{} {}".format(demand, chromosome_utils.get_transponders_configuration_cost(transponders)), end="")
            print("{} {} ".format(path, transponders))
        print()

    t1, t2, t3 = 0, 0, 0
    for key in sorted(best_chromosome.paths_dict):
        for transponders in best_chromosome.transponders_used[key]:
            t1 += transponders[0]
            t2 += transponders[1]
            t3 += transponders[2]
    print("10:{} 40:{} 100:{}".format(t1*2, t2*2, t3*2))


def pol_170():
    print("Problem minimalizaji kosztu dla sieci polskiej")
    print("Chromosomy: " + str(Parameters.amount_of_chromosomes_pol))
    print("Przepustowosc: " + str(OpticalFibersCapacity.L32.value))
    from Network import Network
    network = Network.load_from_file('Resources/net-pl.xml', structure=True, demands=True, admissible_paths=4)
    chromosome_creator = ChromosomeCreator()
    chromosome_utils = ChromosomeUtils()
    chromosomes = chromosome_creator.generate_chromosomes_pol_170(network, 20 * Parameters.amount_of_chromosomes_pol)

    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.pick_bests(chromosomes, chromosome_utils.get_network_transponders_configuration_cost,
                                       Parameters.amount_of_chromosomes_pol, Parameters.optical_fiber_capacity_pol)
    #
    # best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_configuration_cost, 1,
    #                                               Parameters.optical_fiber_capacity_pol)[0]
    # for key in sorted(best_chromosome.paths_dict):
    #     print("{} -> ".format(key))
    #     for demand, path, transponders in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key],
    #                                           best_chromosome.transponders_used[key]):
    #         print("{} {}".format(demand, chromosome_utils.get_transponders_configuration_cost(transponders)), end="")
    #         print("{} {} ".format(path, transponders))
    #     print()
    # return
    algorithm = Algorithm(chromosomes, network)
    chromosomes = algorithm.algorithm_pol_170(Parameters.optical_fiber_capacity_pol)
    print(algorithm.results)
    plot_gen = PlotGenerator([[algorithm.results, 'g--']])
    plot_gen.show_plot()

    best_chromosome = algorithm.pick_bests_sorted(chromosomes, chromosome_utils.get_network_transponders_configuration_cost, 1,
                                                  Parameters.optical_fiber_capacity_pol)[0]
    for key in sorted(best_chromosome.paths_dict):
        print("{} -> ".format(key))
        for demand, path, transponders in zip(best_chromosome.paths_demand[key], best_chromosome.paths_dict[key],
                                              best_chromosome.transponders_used[key]):
            print("{} {}".format(demand, chromosome_utils.get_transponders_configuration_cost(transponders)), end="")
            print("{} {} ".format(path, transponders))
        print()

    t1, t2, t3 = 0, 0, 0
    for key in sorted(best_chromosome.paths_dict):
        for transponders in best_chromosome.transponders_used[key]:
            t1 += transponders[0]
            t2 += transponders[1]
            t3 += transponders[2]
    print("10:{} 40:{} 100:{}".format(t1*2, t2*2, t3*2))


def test():
    # # 170
    # transponders = [[i, j, k] for i in range(0, 2) for j in range(0, 6) for k in range(0, 3) if
    #                 200 >= 10 * i + 40 * j + 100 * k >= 170]
    # print(transponders)
    # # 90
    # transponders = [[i, j, k] for i in range(0, 2) for j in range(0, 4) for k in range(0, 2) if
    #                 120 >= 10 * i + 40 * j + 100 * k >= 90]
    # print(transponders)
    #
    # print(random.choice(transponders))


    tab = [i for i in range(0, 110)]
    tab2 = [i for i in range(100, 0, -2)]

    plot_generator = PlotGenerator([[tab, 'g--'], [tab2, 'r--']])
    plot_generator.show_plot()
    #print(tab)


def main():
    usa_90()

    #pol_170()
    # Problem alokacji dla sieci polskiej
    # alg1_pol()
    # Problem minimalizaji kosztu dla sieci polskiej
    # alg2_pol()
    # Problem alokacji dla sieci amerykanskiej
    # alg1_usa()
    # Problem minimalizacji kosztu dla sieci amerykanskiej
    # alg2_usa()
    # Problem alokacji dla sieci amerykanskiej z 2 sciezkami predefiniowanymi i 170 demand na kazdym
    # alg3_usa()
    # Problem minimalizacji kosztu dla sieci amerykanskiej z 2 sieczkami predefiniowanymi i 170 demand na kazdym
    # alg4_usa()
    #test()


if __name__ == '__main__':
    main()
