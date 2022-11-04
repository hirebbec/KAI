class Dog {
    private String breed;
    private String size;
    private int age;

    public Dog(String breed, String size, int age) {
        this.breed = breed;
        this.size = size;
        this.age = age;
    }

    public void getInfo() {
        System.out.printf("breed:%s, size:%s, age:%d\n", breed, size, age);
    }

    public int eat(int carbohydrates, int squirrels, int fats) {
        return carbohydrates * 4 + squirrels * 4 + fats * 9;
    }
}