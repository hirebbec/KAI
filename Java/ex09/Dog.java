class Dog {
    private String breed;
    private String size;
    private int age;
    
    public Dog(String breed, String size, int age) {
        this.breed = breed;
        this.size = size;
        this.age = age;
//        this.weight = 5.0F;
    }
        
    public void setBreed(String breed) {
        this.breed = breed;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getBreed() {
        return breed;
    }

    public String getSize() {
        return size;
    }

    public int getAge() {
        return age;
    }
}