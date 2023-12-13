package tpdeux;

import java.util.ArrayList;
import java.util.List;

public class Order {
    private String owner;
    private String target;
    private List<String> cocktails;

    public Order() {
        this.owner = null;
        this.target = null;
        this.cocktails = new ArrayList<>();
    }

    public void declareOwner(String owner) {
        this.owner = owner;
    }
    public void declareTarget(String target) {
        this.target = target;
    }
    public String getOwner() {
        return owner;
    }
    public String getTarget() {
        return target;
    }

    public void addCocktail(int nb) {
        for (int i = 0; i < nb; i++) {
            this.cocktails.add("cocktail");
        }
    }

    public List<String> getCocktails() {
        return this.cocktails;
    }
}
