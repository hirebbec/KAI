abstract class Animal{

    private String size;
    private int age;

    public void setSize(String size) {
        this.size = size;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getSize() {
        return size;
    }

    public int getAge() {
        return age;
    }

    public Animal(String size, int age) {
        this.size = size;
        this.age = age;
    }
}

class Dog extends Animal {

    private String breed;

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public String getBreed() {
        return breed;
    }

    public Dog(String breed, String size, int age) {
        super(size, age);
        this.breed = breed;
    }
}