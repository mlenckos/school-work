package shop.ui;

public interface Menu {
    public int size();
    public String getHeading();
    public String getPrompt(int i);
    public void runAction(int i);
}
