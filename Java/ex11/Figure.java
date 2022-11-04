abstract class Figure {

   private float x;
   private float y;

    public void setX(float x) {
        this.x = x;
    }

    public void setY(float y) {
        this.y = y;
    }

    public float getX() {
        return x;
    }

    public float getY() {
        return y;
    }

    public Figure(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public abstract float getPerimeter();

}
class Circle extends Figure {

    private float radius;
    private final float PI = 3.14159f;

    public Circle(float x, float y, float radius) {
        super(x, y);
        this.radius = radius;
    }

    @Override
    public float getPerimeter() {
        return 2 * PI * radius;
    }
}

class Rectangle extends Figure {

    private float width;
    private float height;

    public void setWidth(float width) {
        this.width = width;
    }

    public void setHeight(float height) {
        this.height = height;
    }

    public float getWidth() {
        return width;
    }

    public float getHeight() {
        return height;
    }

    public Rectangle(float x, float y, float width, float height) {
        super(x, y);
        this.width = width;
        this.height = height;
    }

    @Override
    public float getPerimeter() {
        return 2 * (width + height);
    }
}