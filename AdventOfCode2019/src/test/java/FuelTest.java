
import de.cpelzer.adventofcode.adventofcode2019.dayone.rocket.FuelUtilities;
import org.junit.Assert;
import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

public class FuelTest {

    @Test
    public void testFuelForMass() {
        Assert.assertEquals(2, FuelUtilities.calculateFuelForMass(12));
        Assert.assertEquals(2, FuelUtilities.calculateFuelForMass(14));
        Assert.assertEquals(654, FuelUtilities.calculateFuelForMass(1969));
        Assert.assertEquals(33583, FuelUtilities.calculateFuelForMass(100756));
    }

    @Test
    public void testFuelForMultipleModules() {
        List<Double> list = new ArrayList<>();
        list.add(12d);
        list.add(14d);
        list.add(1969d);
        list.add(100756d);

        Assert.assertEquals(34241, FuelUtilities.calculateFuelForModules(list));
    }

    @Test
    public void testFuelInception() {
        Assert.assertEquals(2, FuelUtilities.calculateFuelForMassAndFuel(12));
        Assert.assertEquals(2, FuelUtilities.calculateFuelForMassAndFuel(14));
        Assert.assertEquals(966, FuelUtilities.calculateFuelForMassAndFuel(1969));
        Assert.assertEquals(50346, FuelUtilities.calculateFuelForMassAndFuel(100756));
    }

    @Test
    public void testFuelInceptionWithMultipleModules() {
        List<Double> list = new ArrayList<>();

        list.add(12d);
        list.add(14d);
        list.add(1969d);
        list.add(100756d);

        Assert.assertEquals(51316, FuelUtilities.calculateFuellForAllModulesWithFuelInception(list));
    }
}