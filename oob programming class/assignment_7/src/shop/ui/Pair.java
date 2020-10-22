package shop.ui;

public class Pair<T1, T2> {
	final private T1 a;
    final private T2 b;

    Pair(T1 arg1, T2 arg2){
        this.a = arg1;
        this.b =arg2;
    }
    public T1 getPrompt() {return a;}
    public T2 getTest() {return b;}
    public T2 getAction() {return b;}
}
