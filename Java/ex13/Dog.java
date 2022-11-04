class NegativeAgeException extends Exception{

    private int value;

    public NegativeAgeException(int value) {
        this.value = value;
    }

    @Override
    public String toString() {

        String msg = "EXCEPTION: value of age: " + value + " is negative" ;
        return msg;
    }
}

class Dog {

    private String breed;
    private String size;
    private int age;

    public Dog(String breed, String size, int age) throws NegativeAgeException {
        this.breed = breed;
        this.size = size;
        if (age < 0) {
            throw new NegativeAgeException(age);
        }
        this.age = age;
    }

    void getInfo(){
        System.out.printf("breed:%s, size:%s, age:%d\n", breed, size, age);
    }
}