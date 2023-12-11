package hellocucumber;

import io.cucumber.java.sv.*;
import static org.junit.jupiter.api.Assertions.assertEquals;

class IsItFriday {
    static String isItFriday(String today) {
        return today.equals("fredag") ? "Ja" : "Nej";
    }
}

public class StepDefinitions {
    // Variable to store the current day
    private String today;
    // Variable to store the actual answer obtained during testing
    private String actualAnswer;

    // Step definition for setting the current day
    @Givet("att idag är {string}")
    public void att_idag_är(String day) {
        // Set the value of the 'today' variable to the provided day
        today = day;
    }

    // Step definition for asking if it's Friday
    @När("jag frågar om det redan är fredag")
    public void i_ask_whether_it_s_friday_yet() {
        // Call the isItFriday method from IsItFriday class and store the result in 'actualAnswer'
        actualAnswer = IsItFriday.isItFriday(today);
    }

    // Step definition for verifying the expected answer
    @Så("bör jag få svaret {string}")
    public void i_should_be_told(String expectedAnswer) {
        // Compare the expected answer with the actual answer obtained during testing
        assertEquals(expectedAnswer, actualAnswer);
    }

    // Step definition for setting the current day to Sunday
    @Givet("att idag är söndag")
    public void att_idag_är_söndag() {
        // Set the value of the 'today' variable to "söndag" (Sunday)
        today = "söndag";
    }
}