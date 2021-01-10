package de.cpelzer.adventofcode.adventofcode2019.dayone;

import de.cpelzer.adventofcode.adventofcode2019.dayone.rocket.FuelUtilities;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Main {
    private static final Logger LOGGER = Logger.getLogger(Main.class.getName());

    public static void main(String[] args) {
        File inputFile = new File("AdventOfCode2019/src/main/resources/day1.txt");
        try(BufferedReader reader = new BufferedReader(new FileReader(inputFile))) {

            String line = "";
            List<Double> allModuleMasses = new ArrayList<>();

            while ((line = reader.readLine()) != null) {
                if ("".equals(line)) {
                    continue;
                }
                allModuleMasses.add(Double.valueOf(line));

            }
            LOGGER.log(Level.INFO, "PART 1: Fuel needed for all Modules w/o the fuel needed for the fuel: {0}"
                    , FuelUtilities.calculateFuelForModules(allModuleMasses));

            LOGGER.log(Level.INFO, "PART 2: Fuel needed for all Moduels w/ the fuel for the fuel: {0}"
                    , FuelUtilities.calculateFuellForAllModulesWithFuelInception(allModuleMasses));
        } catch (IOException e) {
            LOGGER.log(Level.SEVERE, "An Error occured while opening the files", e);
        }
    }
}
