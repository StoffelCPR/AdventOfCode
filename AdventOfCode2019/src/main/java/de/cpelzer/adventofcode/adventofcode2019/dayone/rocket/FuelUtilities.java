package de.cpelzer.adventofcode.adventofcode2019.dayone.rocket;

import java.util.List;

public class FuelUtilities {

    private FuelUtilities() {}

    /**
     * Method for calculating the fuel needed for one module w/o the weight of the fuel
     * @param moduleMass The mass of the module
     * @return the fuel needed to fuel the module alone
     */
    public static int calculateFuelForMass(double moduleMass) {
        return ((int)moduleMass/3) -2;
    }

    /**
     * Template method for calculating the fuel needed forall modules w/o calculating the added fuel into it.
     * @param moduleMasses A list of masses of all modules
     * @return The fuel needed to fuel all modules.
     */
    public static int calculateFuelForModules(List<Double> moduleMasses) {
        int fuelForAllModules = 0;

        for (double d : moduleMasses) {
            fuelForAllModules += calculateFuelForMass(d);
        }

        return fuelForAllModules;
    }

    /**
     *  This method calculates the fuel needed for the mass of a module and the mass added by the fuel needed recursively.
     * @param moduleMass The mass of a given module
     * @return the complete fuel w/ the fuel needed to fuel the fuel. (:D)
     */
    public static int calculateFuelForMassAndFuel(double moduleMass) {
        int reqFuel = ((int)moduleMass/3)-2;

        if (reqFuel <= 0) {
            return 0;
        }

        return reqFuel + calculateFuelForMassAndFuel(reqFuel);
    }

    /**
     * Template method for calculating the fuel for the fuel for all modules
     * @param moduleMasses a list of the masses of all modules
     * @return The amount of fuel needed w/ the fuel needed to fuel the fuel.
     */
    public static int calculateFuellForAllModulesWithFuelInception(List<Double> moduleMasses) {
        int requiredFuel = 0;
        for (double d : moduleMasses) {
            requiredFuel += calculateFuelForMassAndFuel(d);
        }
        return requiredFuel;
    }

}