class Dog {
    private String breed;
    private String size;
    private int age;
    private float weight;

    public Dog(String breed, String size, int age) {
        this.breed = breed;
        this.size = size;
        this.age = age;
        this.weight = 5.0F;
    }

    public void getInfo() {
        System.out.printf("breed:%s, size:%s, age:%d\n", breed, size, age);
    }

    public int eat(int carbohydrates, int squirrels, int fats) {
        return carbohydrates * 4 + squirrels * 4 + fats * 9;
    }

    public Dog(String breed, String size, int age, float weight) {
        this.breed = breed;
        this.size = size;
        this.age = age;
        this.weight = weight;
    }

    public String checkCalories(int calories){
        float norm = 53.5F * weight;
        if (Math.abs(norm - calories) < 30) {
            return "good";
        } else if (calories - norm < -30) {
            return "bad";
        } else if (calories - norm > 30) {
            return "overate";
        }
        return null;
    }
}